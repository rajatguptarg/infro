#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: Test module for mongo engine
"""

from infro.engine import MongoEngine, DBOperationException
from nose.tools import assert_not_equals, raises


__all__ = ['TestMongoClient']


class TestMongoClient(object):

    def setup(self):
        self.engine = MongoEngine(uri="mongodb://127.0.0.1:27017/infro-test")
        self.engine.connect()

    def teardown(self):
        self.engine.disconnect()

    def test_0010_should_insert_record_in_db(self):
        record = {
            "name": "Rajat Gupta",
            "age": 23
        }

        result = self.engine.insert_record(record, 'infro.details')
        assert_not_equals(result.inserted_id, None)

    @raises(DBOperationException)
    def test_0020_should_throw_exception_if_db_is_not_found(self):
        record = {
            "name": "Rajat Gupta",
            "age": 23
        }
        self.engine._db = None
        self.engine.insert_record(record, 'infro.details')
