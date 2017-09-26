import re
from elementtree.ElementTree import XML, tostring
import pdb

def header(in_text):
    """change header text into xml elements attibutes"""
    outstr = re.sub('&', '&amp;', in_text)
    outstr = re.sub('<HONG KONG>', '(HONG KONG)', outstr)
    outstr = re.sub('\'', '&apos;', outstr)
    outstr = re.sub('"', '', outstr)
    # unclosed tags get turned into attributes
    alltags = re.findall('<(.*?)>', outstr)
    closedtags = []
    for tag in alltags:
        if tag.find('/') != -1 and tag not in closedtags:
            closedtags.append(tag.replace('/',''))
            closedtags.append(tag)
    for tag in alltags:
        if closedtags.count(tag) == 0:
            regex = re.compile( '<' + tag + '>(.*)')
            outstr = regex.sub(r'' + tag + '="\g<1>"', outstr)    
    # ITEMS, REFERENCES - duplicates break parser so drop them
    regex = re.compile('ITEMS=".*?"')
    outstr = regex.sub(r'', outstr)
    regex = re.compile('REFERENCES-429=".*?"')
    outstr = regex.sub(r'', outstr)
    regex = re.compile('PUBLIC-REFERENCE-ACC=".*?"')
    outstr = regex.sub(r'', outstr)
    # GROUP-MEMBERS - duplicates break parser but keep them
    regex = re.compile('GROUP-MEMBERS="(.*?)"')
    outstr = regex.sub( \
        r'<GROUP-MEMBER GROUP-MEMBER-NAME="\g<1>"></GROUP-MEMBER>', outstr)
    # valid xml needs a root node
    outstr = "<SUBMISSION> " + outstr + "</SUBMISSION>\n"
    closedtags.append('SUBMISSION')
    # move the closing ">" to the right of the attributes
    for tag in closedtags:
        regex = re.compile( '<' + tag + '>(.*?)<', re.DOTALL)
        outstr = regex.sub(r'<' + tag + ' \g<1>><', outstr)
    try:
        outstr = xmltidy(outstr)
    except:
        outstr = ''
    return outstr
    
def ownershipDocument(in_text):
    """change ownershipDocument xml elements into attibutes, tidy xml"""
    outlist = []
    outstr = re.sub('&quot;', '', in_text)
    outstr = xmltidy(outstr)
    regex = re.compile( '<(.*?)>(.*)<.*?/.*?>')
    #change elements closed on the same line to attributes
    for line in outstr.split('\n'):
        line = regex.sub(r' \g<1>="\g<2>" \n', line.strip())
        outlist.append(line)
    regex = re.compile( '(<.*?)(>)(.*?)(<.*?/.*?>)', re.DOTALL)
    outstr = regex.sub(r'\g<1> \n\g<3>\g<2>\g<4> \n', ''.join(outlist))
    regex = re.compile('(\n)(>)', re.DOTALL)
    outstr = regex.sub(r'\g<2>\g<1>', outstr)
    outstr = re.sub('/ >', '/>', outstr)
    # the stuff above broke footnotes: footnote id="F2"="Repre...
    regex = re.compile('footnote id="(.*?)"="(.*?)"')
    outstr = regex.sub('<footnote id="\g<1>" text="\g<2>" />', outstr)
    outstr = re.sub('/> >', '/> ', outstr)
    regex = re.compile('<footnotes *\n *<')
    outstr = regex.sub('<footnotes>\n<', outstr)
    # and we broke "remarks" actually these were funky from the start...
    regex = re.compile(' remarks=(.*?)>')
    outstr = regex.sub('<remarks text=\g<1> />', outstr)
    # this is a remark without an = sign
    regex = re.compile('<remarks(.*?)></remarks>', re.DOTALL)
    outstr = regex.sub('<remarks text="\g<1>" />', outstr)
    # and we dissappeared a ">" on some close tags
    regex = re.compile('</(\w*?) *?>*?\W*?\n')
    outstr = regex.sub('</\g<1>>\n', outstr)
    # wacky footnote problems
    regex = re.compile('footnote id="(.*?)"> *?(.*?)</footnote>')
    outstr = regex.sub(r'footnote id="\g<1>" text="\g<2>" />', outstr)
    #<footnote id="F2"
    regex = re.compile('footnote id="(.*?)"\W*(.*?)></footnote>')
    outstr = regex.sub(r'footnote id="\g<1>" text="\g<2>" />', outstr)
    #OMFG some german without a zip code
    outstr = re.sub('<rptOwnerZipCode /\W*\n', ' rptOwnerZipCode=""\n', outstr)
    outstr = re.sub(' rptOwnerStateDescription="GERMANY" >\n', \
        ' rptOwnerStateDescription="GERMANY" />\n', outstr)
    outstr = re.sub('/>\n</reportingOwnerAddress>', '/>\n', outstr)
    outstr = re.sub('<rptOwnerStateDescription />', ' />\n', outstr)
    #OMFG2 street is empty
    outstr = re.sub('<rptOwnerStreet2 /\W*?\n', ' rptOwnerStreet2=""\n', outstr)
    outstr = re.sub('<rptOwnerStreet1\W*/>\n', ' rptOwnerStreet1=""\n', outstr)
    outstr = re.sub('<rptOwnerStreet1\W*/\W*\n', ' rptOwnerStreet1=""\n', outstr)
    outstr = re.sub('<rptOwnerCity\W*?/>\n', ' rptOwnerCity=""\n', outstr)
    outstr = re.sub('<rptOwnerState\W*?/>\n', ' rptOwnerState=""\n', outstr)
    outstr = re.sub('<footnotes /\W*\n', '', outstr)
    outstr = re.sub('>\W*?\n\W*?rptOwnerStreet2', '\n rptOwnerStreet2', outstr)

    # check for good syntax
    outstr = xmltidy(outstr)
    return outstr
        
def xmltidy(text):
    """send back good lookin' xml (basically a syntax checker)"""
    try:
        elem = XML(text)
        text = tostring(elem)
        return text
    except:
        #print text
        return ''
        
