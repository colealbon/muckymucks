#!/usr/bin/python

# Copyright (c) 2009, Marvel Computing Company
# 411 N. 44th Street
# Seattle, WA 98103 USA
# 206-579-6409
# All Rights Reserved.

from generic_utility import *
import sys
import os
import elementtree.ElementTree as etree
import dircache
config = getConfig(sys.argv[1])
sys.path.insert(2, config.get('MuckyMucks', 'site_packages_dir'))
sys.path.insert(2, config.get('MuckyMucks', 'django_app_dir'))
sys.path.insert(3, config.get('MuckyMucks', 'django_projects_dir'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from muckymucks import models
import copy
from django.db.models import get_app, get_apps, get_models
import psycopg2
from django.db import connection
import re

def importXMLFile(XMLFile):
    try:
        xmlfile = XMLFile
        extractDir = config.get('Extract', 'extract_dir')
        logger.debug('importXMLFile processing:' + extractDir + '/' + xmlfile)
        xmldoc = etree.parse(extractDir + '/' + xmlfile)
        root = xmldoc.getroot()
        walkTree(root, None, None)
        logger.debug('importXMLFile processed: ' + xmlfile)
    except:
        logger.debug('importXMLFile failed: ' + xmlfile)

def getModelInstance(ModelName, ModelID):
    a = get_app('muckymucks', {})
    for model in get_models(a):
        if str(model).replace(ModelName, '') != str(model):
            return model(id=ModelID)

def getModelID(Node):
    # enhanced version of create_or_save()  works with unique on multiple
    nodeName = Node.tag.title().replace('-','')
    a = get_app('muckymucks', {})
    filterStr = ''
    for model in get_models(a):
        if str(model).replace(nodeName, '') != str(model):
            modelInstance = model()
    for k, v in Node.attrib.items():
        setattr(modelInstance, k.title().replace('-',''), v.replace("'","").replace('\\',''))
        filterStr = filterStr + '"' + k.title().replace('-','') + '":"' + v.replace("'","").replace('\\','') + '",'
    try:
        modelInstance.save()
        logger.debug(str(modelInstance))
        return modelInstance.id, nodeName
    # except TypeError:
    #     return None, 'docroot'
    # except psycopg2.DataError:
    #     return None, 'docroot'
    # except UnboundLocalError:
    #     return None, 'docroot'
    except psycopg2.InternalError:
        # this works around a crash in trying to commit "unique on multiple" records
        # apparently django only checks primary keys before doing a save/insert operation
        connection.close()
        for model in get_models(a):
            if str(model).replace(nodeName, '') != str(model):
                for k, v in Node.attrib.items():
                    key = k.title().replace('-','')
                    val = v.replace("'","").replace('\\','')
                    for d in model.objects.values():
                        match = True
                        for x, y in d.items():
                            if x == key and y != val:
                                match = False
                                break
                        if match == True:
                            for z, id in d.items():
                                if z == 'id':
                                    return id, nodeName
    except psycopg2.IntegrityError:
        # this works around a crash in trying to commit "unique on multiple" records
        # apparently django only checks primary keys before doing a save/insert operation
        connection.close()
        model = None
        for model in get_models(a):
            if str(model).replace(nodeName, '') != str(model):
                for k, v in Node.attrib.items():
                    key = k.title().replace('-','')
                    val = v.replace("'","").replace('\\','')
                    for d in model.objects.values():
                        match = True
                        for x, y in d.items():
                            if x == key and y != val:
                                match = False
                                break
                        if match == True:
                            for z, id in d.items():
                                if z == 'id':
                                    return id, nodeName

def walkTree(node, ParentID, ParentNodeName):
    modelID, nodeName = getModelID(node)
    if ParentID != None and ParentNodeName != 'docroot':
        addManyManyRelationship(ParentNodeName, ParentID, nodeName, modelID)
    children = node.getchildren()
    for child in children:
        walkTree(child, modelID, nodeName)

def addManyManyRelationship (ModelNameLeft, IDLeft, ModelNameRight, IDRight):
    leftInstance = getModelInstance(ModelNameLeft, IDLeft)
    rightInstance = getModelInstance(ModelNameRight, IDRight)
    try:
        getattr(leftInstance, ModelNameRight.lower() + "_set").add(rightInstance)
    except AttributeError:
        try:
            getattr(rightInstance, ModelNameLeft.lower() + "_set").add(leftInstance)
        except AttributeError:
            pass
        # except psycopg2.ProgrammingError:
        #     pass
        # except psycopg2.IntegrityError:
        #     pass
    # except psycopg2.ProgrammingError:
    #     pass
    # except psycopg2.IntegrityError:
    #     pass

def renameXMLFile(XMLFile):
    xmlfile = XMLFile
    extractDir = config.get('Extract', 'extract_dir')
    try:
        os.rename(extractDir + '/' + xmlfile, extractDir + '/' + xmlfile + '.old')
        logger.debug('renameXMLFile removed: ' + xmlfile)
    except:
        logger.debug('renameXMLFile could not remove: ' + extractDir + '/' + xmlfile)

def getNextXMLFile():
    '''read the xml extract folder and send back the name of an xml file'''
    extractDir = config.get('Extract', 'extract_dir')
    dircache.reset()
    for xmlfile in dircache.listdir(extractDir):
        if os.path.splitext(xmlfile)[-1] == '.xml':
            return xmlfile
    return None

def run():
    logger.debug('Processing Started')
    xmlfile = getNextXMLFile()
    while xmlfile != None:
        logger.debug('importing' + xmlfile)
        importXMLFile(xmlfile)
        renameXMLFile(xmlfile)
        xmlfile = getNextXMLFile()
    logger.debug('Processing Complete')

if __name__ == "__main__":
    config = getConfig(sys.argv[1])
    logger = getLogger(config)
    run()
