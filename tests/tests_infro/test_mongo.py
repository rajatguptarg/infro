#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: Test module for mongo engine
"""

from infro.engine import MongoEngine
from nose.tools import assert_equals


__all__ = ['TestMongoClient']


class TestMongoClient(object):

    def setup(self):
        self.engine = MongoEngine(uri="mongodb://127.0.0.1:27017/infro-test")
        self.engine.connect()

    def teardown(self):
        self.engine.disconnect()

    def test_0010_should_insert_record_in_db(self):
        result = self.engine.insert_record(None, None)
        assert_equals(result, True)
