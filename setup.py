#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description: Setup module
"""

import os
from distutils.core import setup


def get_files(root):
    for dirname, dirnames, filenames in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirname, filename)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


MODULE = "infro"
PREFIX = "platform"


setup(
    name='%s-%s' % (PREFIX, MODULE),
    packages=['infro'],
    url='https://github.com/rajatguptarg/infro',
    license='MIT',
    author='Rajat Gupta',
    version='0.1',
    author_email='rajat.gupta712@gmail.com',
    long_description=open('README.md', 'rt').read(),
    description='REST API framework for managing AWS Infrastructure',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Office/Business',
    ],
)
