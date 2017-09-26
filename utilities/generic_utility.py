#!/usr/bin/python

# Copyright (c) 2009, Marvel Computing Company
# 411 N. 44th Street
# Seattle, WA 98103 USA
# 206-579-6409
# All Rights Reserved.

import ConfigParser
import logging
import logging.handlers
import sys

def getConfig(ConfigFile):
    config = ConfigParser.ConfigParser()
    config.read(ConfigFile)
    return config

def getLogger(config):
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    logger = logging.getLogger(config.get('Logging', 'logger_name'))
    logger.setLevel(LEVELS.get( config.get('Logging', 'log_level'), logging.NOTSET) )
    handler = logging.handlers.RotatingFileHandler( \
        config.get('Logging', 'log_file_dir') + '/' + config.get('Logging', 'log_file_name'), \
        maxBytes=config.get('Logging', 'logger_max_bytes'), \
        backupCount=config.get('Logging', 'logger_backup_count'), \
        )
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def __init__(self):
    config = getConfig(sys.argv[1])
    logger = getLogger(config)
