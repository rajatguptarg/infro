#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: Response builder for the HTTP requests
"""

from abc import ABCMeta, abstractmethod


__all__ = ['HTTPResponse']


class HTTPResponse(object):
    """
    Abstract class for the HTTP Responses
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def build_json_response(self, response, code):
        pass
