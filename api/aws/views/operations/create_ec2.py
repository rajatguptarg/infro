#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: View to manage creation of EC2 APIs
"""

from flask_classy import FlaskView
from flask import request, abort
from .inventory import http_200_response, ROUTE_BASE


__all__ = ['CreateEC2View']


class CreateEC2View(FlaskView):
    """
    View to manage the EC2 Instance creation
    """
    route_base = ROUTE_BASE + 'create-ec2'

    def post(self):
        """
        Request Params:
            - username
            - password
        """
        try:
            username = request.json['username']     # noqa
            password = request.json['password']     # noqa
        except:
            abort(400)
        return http_200_response.build_json_response(request.json)
