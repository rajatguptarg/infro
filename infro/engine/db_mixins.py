#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: Mixin module for database connections
"""

import logging
from logging.config import dictConfig
from abc import ABCMeta, abstractmethod
from .db_exception import DBConnectionException


__all__ = ['DBMixin']


class DBMixin(object):
    """
    Abstract Mixin class for the DB Engines
    """

    __metaclass__ = ABCMeta

    logging_config = dict(
        version=1,
        formatters={
            'f': {'format':
                  '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
        handlers={
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.DEBUG}
        },
        root={
            'handlers': ['h'],
            'level': logging.DEBUG,
        },
    )

    dictConfig(logging_config)
    logger = logging.getLogger(__name__)

    @abstractmethod
    def connect(self):      # pragma: no cover
        raise DBConnectionException("Unable to connect to DB")

    @abstractmethod
    def disconnect(self):   # pragma: no cover
        raise DBConnectionException("Unable to disconnect to DB")
