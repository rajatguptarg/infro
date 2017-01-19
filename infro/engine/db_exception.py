#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: DB Exceptions modules
"""

__all__ = ['DBConnectionException', 'DBOperationException']


class DBConnectionException(Exception):
    """
    Exception class for db connection failure
    """
    pass


class DBOperationException(Exception):
    """
    Exception class for db CRUD operation failure
    """
    pass
