#!/usr/bin/python

# Copyright (c) 2011, Cole B. Albon
# 333 Brahan Blvd.
# San Antonio, TX 78215-1045 USA
# 316-308-8073
# All Rights Reserved.

from generic_utility import *
from ftplib import FTP
import dircache
import os
import sys

def getNextTarball(Config, Logger, FTPSession):
    '''Download a list of tarball in the edgar Feed directory.
        check if we already have it.  If not return an older one '''
    ftp = FTPSession
    config = Config
    logger = Logger
    logger.debug('getNextTarball Started')
    downloadDir = config.get('Download', 'sec_feed_dir')
    try:
        for nlstitem in ftp.nlst():
            if nlstitem.endswith('tar.gz') \
            and nlstitem not in dircache.listdir(downloadDir) \
            and nlstitem + '.part' not in dircache.listdir(downloadDir):
                logger.debug('getNextTarball Ended - found a tarball: %' %str(nlstitem))
                return str(nlstitem)
        return None
    except:
        logger.error('getNextTarball crashed - ftp.sec.gov might be out of new tarballs')
        shutdown(config, logger)
        raise

def getFTPSession(Config, Logger):
    logger.debug('getFTPSession Started')
    try:
        ftp = FTP('ftp.sec.gov')
        ftp.login()
        ftp.cwd('edgar')
        ftp.cwd('Feed')
        return ftp
    except:
        logger.error('getFTPSession crashed - ftp.sec.gov might be down')
        raise

def downloadTarball(Config, Logger, FTPSession, Tarball):
    config = Config
    logger = Logger
    logger.debug('downloadTarball Started')
    ftp = FTPSession
    tarball = Tarball
    downloadDir = config.get('Download', 'sec_feed_dir')
    try:
        logger.info('downloadTarball starting ftp transfer ' + tarball + ' to ' + downloadDir + '/' + tarball + '.part')
        ftp.retrbinary('RETR ' + tarball, open(downloadDir + '/' + tarball + '.part', 'wb').write)
        os.system('/bin/mv ' + downloadDir + '/' + tarball + '.part ' + downloadDir + '/' + tarball)
        logger.info('downloadTarball ftp transfer complete ' + tarball + ' to ' + downloadDir + '/' + tarball)
        logger.debug('downloadTarball Ended')
    except:
        logger.error('downloadTarball failed - check the download directory permissions: ' + downloadDir)
        raise

def run(Config, Logger):
    try:
        config = Config
        logger = Logger
        logger.debug('Processing Started')
        ftp = getFTPSession(config, logger)
        tarball = getNextTarball(config, logger, ftp)
        while tarball != None:
            downloadTarball(config, logger, ftp, tarball)
            tarball = getNextTarball(config, logger, ftp)
    except:
        raise
    finally:
        ftp.quit()
        logger.debug('Processing Ended')

if __name__ == "__main__":
    config = getConfig(sys.argv[1])
    config.set('Logging', 'logger_name', 'download.py')
    logger = getLogger(config)
    #setup(config, logger)
    run(config, logger)
    #shutdown(config, logger)
