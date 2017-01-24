#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""

import json
from flask import Response
from .resp_builder import HTTPResponse


class HTTP200Response(HTTPResponse):
    """
    http 200 reponse builder
    """

    def build_json_response(self, info, code=200):
        if not isinstance(info, list):
            info = [info]
        data = {
            "content": info
        }
        data = json.dumps(data)
        resp = Response(
            data, status=code, mimetype='application/json'
        )

        return resp
