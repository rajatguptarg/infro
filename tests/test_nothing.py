#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""

from nose.tools import assert_equals, assert_not_equal
import infro    # noqa


__all__ = ['TestNothing']


class TestNothing(object):
    """
    Test class to check whether the tests are running or not
    """

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_0000_should_pass_for_equal_objects(self):
        assert_equals(2, 2)

    def test_0000_should_pass_for_unequal_objects(self):
        assert_not_equal(3, 2)
