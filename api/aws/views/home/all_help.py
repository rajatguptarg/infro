#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""

from flask_classy import FlaskView
from .inventory import ROUTE_BASE, http_200_response


__all__ = ['HelpView']


class HelpView(FlaskView):
    """
    Help view for the aws
    """
    route_base = ROUTE_BASE

    def get(self):
        message = {
            "api_name": "AWS REST Framework",
            "status": "OK"
        }
        return http_200_response.build_json_response(message)
