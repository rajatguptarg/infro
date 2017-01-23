#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: Flask blueprint for the HTTP Errors
"""

from flask import Blueprint
from api.aws.responses import HTTPErrorResponse


http_error = HTTPErrorResponse()
api_errors = Blueprint('api_errors', __name__)


@api_errors.app_errorhandler(400)
def bad_request(e):
    """
    Handle 400 Errors
    """
    data = [{
        "error": "Bad Request.",
        "details": str(e)
    }]
    return http_error.build_json_response(data, 400)
