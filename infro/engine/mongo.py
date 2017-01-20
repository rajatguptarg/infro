#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: Mongo DB APIs
"""

from .db_mixins import DBMixin
from pymongo import MongoClient
from .db_exception import DBConnectionException, DBOperationException


__all__ = ['MongoEngine']


class MongoEngine(DBMixin):
    """
    Mongo DB Engine
    """
    _connection = None
    _db = None

    def insert_record(self, record, collection):
        try:
            collection = self._db[collection]
        except:
            raise DBOperationException("Unable to find collection")
        return collection.insert_one(record)

    def _connect_by_db_uri(self):
        return MongoClient(self.uri)

    def connect(self):  # pragma: no cover
        if self.uri:
            self._connection = self._connect_by_db_uri()
        try:
            self._db = self._connection.get_default_database()
        except:
            raise DBConnectionException("Unable to connect to DB")

    def disconnect(self):
        self._connection.close()

    def __init__(self, username=None, password=None, uri=None):
        self.username = username
        self.password = password
        self.uri = uri
