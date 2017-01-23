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

    def build_json_response(self, info):
        data = json.dumps(info)
        resp = Response(
            data, status=200, mimetype='application/json'
        )

        return resp
