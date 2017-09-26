#!/usr/bin/python

# Copyright (c) 2011, Cole B. Albon
# 333 Brahan Blvd.
# San Antonio, TX 78215-1045 USA
# 316-308-8073
# All Rights Reserved.

import base
import convert2xml
import dircache
import re
from tarfile import *
import sys

def convertTarballToXMLFile (Tarball):
    '''extracts stuff from a tarball to an xml file'''
    extractDir = config.get('Extract', 'extract_dir')
    downloadDir = config.get('Download', 'sec_feed_dir')
    tarball = Tarball
    logger.debug('convertHeaderFileToXMLFile Started ' + tarball )
    tfile = TarFile.open(downloadDir + '/' + Tarball, 'r:gz')
    tfiles = tfile.getnames()
    fileCount = len(tfiles)
    curCount = 0

    for filing in tfiles:
        curCount = curCount + 1
        if filing != './/':
	    if filing != '.':	
                logger.debug('extracting: ' + filing)
                xmlStr = []
                xmlStr.append('<Source file="' + filing + '">\n')
                xfile = TarFile.extractfile(tfile, TarFile.getmember(tfile, filing))
                xread = xfile.read()
                # HEADER
                headers = re.findall('<SUBMISSION>(.*?)<DOCUMENT>', \
                    xread, re.DOTALL)
                for header in headers:
                    xmlStr.append(convert2xml.header(header))
                # ownershipDocument (form 4 and others) 
                ownershipDocuments = re.findall( \
                    '<ownershipDocument>.*</ownershipDocument>', xread, re.DOTALL)
                for ownershipDocument in ownershipDocuments:
                    xmlStr.append( \
                        convert2xml.ownershipDocument(ownershipDocument))
                xfile.close()
                xmlStr.append('</Source>\n') 
                xml_export = open(extractDir + '/' + filing + '.xml',"w")
                try:
                    xml_export.writelines(''.join(xmlStr))
                except:
                    xml_export.writelines('')
                xml_export.close()
        logger.debug(str(curCount) + ' out of ' + str(fileCount))
    tfile.close()


def getNextTarball():
    '''returns the name of a file that is not already extracted'''
    downloadDir = config.get('Download', 'sec_feed_dir')
    extractDir = config.get('Extract', 'extract_dir')
    try:
        for tarball in dircache.listdir(downloadDir):
            if not tarball + '.xml' in dircache.listdir(extractDir) \
            and not tarball + '.xml.old' in dircache.listdir(extractDir):
                return tarball
        return None
    except:
        raise

def run():
    tarball = getNextTarball()
    while tarball != None:
        convertTarballToXMLFile(tarball)
        tarball = getNextTarball()
        tarball = None

if __name__ == "__main__":
    config = base.getConfig(sys.argv[1])
    config.set('Logging', 'logger_name', 'extract.py')
    logger = base.getLogger(config)
    run()
