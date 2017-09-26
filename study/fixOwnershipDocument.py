import re
file = open('ownershipDocument.xml')

inXmlString = ''
for line in file.readlines():
    inXmlString = inXmlString + line

for strLine in inXmlString.split('\n'):
    if strLine.strip() != '':
        p = re.compile( '<(.*?)>(.*)<.*?/.*?>')
        for strLine in inXmlString.split('\n'):
            if strLine.strip() != '':
                outXml.append(p.sub(r'    \g<1>="\g<2>"\n', strLine.strip()))
p = re.compile( '(<.*?)(>)(.*?)(<.*?/.*?>)', re.DOTALL)
outXmlStr = p.sub(r'\g<1>\n\g<3>\g<2>\g<4>\n', ''.join(outXml))
print outXmlStr

