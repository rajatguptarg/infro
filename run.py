#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""

import uuid
from api import APP as app

if __name__ == '__main__':
        app.secret_key = str(uuid.uuid4())
        app.run(debug=True, port=8000, host='0.0.0.0')
