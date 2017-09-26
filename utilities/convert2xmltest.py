import unittest
import convert2xml
import re

class HeaderTest (unittest.TestCase):
    sampleText = """
    <TIMESTAMP>20090217:132500
    <PRIVATE-TO-PUBLIC>
    <ACCESSION-NUMBER>0000000000-07-051112
    <TYPE>UPLOAD
    <PUBLIC-DOCUMENT-COUNT>1
    <FILING-DATE>20071018
    <FILED-FOR>
    <COMPANY-DATA>
    <CONFORMED-NAME>MILLENNIUM GROUP WORLDWIDE INC
    <CIK>0001409327
    <ASSIGNED-SIC>8900
    <IRS-NUMBER>820540176
    <STATE-OF-INCORPORATION>FL
    <FISCAL-YEAR-END>1231
    </COMPANY-DATA>
    <FILING-VALUES>
    <FORM-TYPE>UPLOAD
    </FILING-VALUES>
    <BUSINESS-ADDRESS>
    <STREET1>2825 N. 10TH STREET
    <CITY>ST. AUGUSTINE
    <STATE>FL
    <ZIP>32084
    <PHONE>904-262-4899
    </BUSINESS-ADDRESS>
    <MAIL-ADDRESS>
    <STREET1>2825 N. 10TH STREET
    <CITY>ST. AUGUSTINE
    <STATE>FL
    <ZIP>32084
    </MAIL-ADDRESS>
    </FILED-FOR>
    <PUBLIC-REFERENCE-ACC>0001121781-07-000310"""
    def testheader(self):
        """header(text) should always send back something"""
        result = convert2xml.header(self.sampleText)

class OwnershipDocumentTest (unittest.TestCase):
    def testownershipDocument(self):
        """ownershipDocument(text) should always send back something"""
        filelist = ['0000003982-09-000006.nc']
        filelist.append('0000003982-09-000007.nc')
        filelist.append('0000014930-09-000039.nc')
        filelist.append('0000054473-09-000004.nc')
        filelist.append('0001019687-09-000534.nc')
        filelist.append('0001052192-09-000075.nc')
        filelist.append('0001225208-09-003817.nc')
        filelist.append('0001415448-09-000098.nc')
        filelist.append('0000038725-09-000001.nc')
        for filename in filelist:
            xfile = open('../work/' + str(filename), "r")
            try:
                linelist = []
                for line in xfile.readlines():
                    linelist.append(line)
                filetext = ''.join(linelist)
                ownershipDocuments = re.findall( \
                    '<ownershipDocument>.*</ownershipDocument>', filetext, \
                    re.DOTALL)
                for ownershipDocument in ownershipDocuments:
                    result = convert2xml.ownershipDocument(ownershipDocument)
            except:
                raise
            finally:
                xfile.close()

if __name__ == "__main__":
    unittest.main()   
