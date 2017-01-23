#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: A flask api server
"""

import logging
from flask import Flask
from logging import Formatter

# import views
from api.aws.views.api_help import AWSHelpView
from api.aws.views.home import HelpView


APP = Flask(__name__, static_folder='static', static_url_path='')


log_handler = logging.StreamHandler()

log_handler.setFormatter(Formatter(
    '\n-------------------------------------\n'
    'TIME: %(asctime)s \n'
    'LEVEL: %(levelname)s \n'
    'MESSAGE: %(message)s \n'
    'FILE: %(pathname)s \n'
    'LINE: %(lineno)d'
    '\n-------------------------------------\n'))

APP.logger.addHandler(log_handler)
APP.jinja_env.autoescape = True


# pragma mark - home
HelpView.register(APP)

# pragma mark - aws_api
AWSHelpView.register(APP)
