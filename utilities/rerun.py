#!/usr/bin/python
#
import os, glob, time, sys
import dircache

oldDateTime = 0

def isModified(OldDateTime):
    for thefile in dircache.listdir('.'):
        if not thefile in ['rerun.py', 'log', 'utilities.cfg', 'utilities.cfg.sample', 'generic_utility.pyc']:
            stats = os.stat(thefile)
            if time.localtime(stats[8]) > OldDateTime:
                print 'restart: ' + thefile + ' '  + time.strftime("%m/%d/%y %H:%M:%S", time.localtime(stats[8]))
                os.system('python ' + thefile)
                return time.localtime(stats[8])
    return OldDateTime

while True:
    oldDateTime = isModified(oldDateTime)
    time.sleep(5)