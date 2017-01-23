#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""

from flask_classy import FlaskView
from .inventory import ROUTE_BASE, http_200_response


__all__ = ['AWSHelpView']


class AWSHelpView(FlaskView):
    """
    Help view for the aws
    """
    route_base = ROUTE_BASE

    def get(self):
        message = [{
            "api": "AWS",
            "description": "AWS Rest Framework API",
            "status": "OK"
        }]
        return http_200_response.build_json_response(message)
