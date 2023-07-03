#!/usr/bin/env python3
"""
Logging
"""
import logging
from logging import getLogger

LOGGING_LEVEL = logging.INFO


def get_logger(name):
    logger = getLogger(name)
    logger.setLevel(LOGGING_LEVEL)
    return logger
