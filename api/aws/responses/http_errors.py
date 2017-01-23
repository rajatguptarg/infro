#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""

import json
from flask import Response
from .resp_builder import HTTPResponse


class HTTPErrorResponse(HTTPResponse):
    """
    http error reponse builder
    """

    def build_json_response(self, info, code):
        data = {
            "errors": info
        }
        data = json.dumps(data)
        resp = Response(
            data, status=code, mimetype='application/json'
        )

        return resp
