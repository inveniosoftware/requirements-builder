# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015, 2016, 2017 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.
#
"""Build requirements files from setup.py requirements."""

from setuptools import setup

import os
import testpkh

dirname = os.path.dirname(__file__)

requirements = [
    'click>=5.0.0',
    'mock>=1.3.0',
    'CairoSVG<2.0.0,>=1.0.20',
    'functools32>=3.2.3-2; python_version=="2.7"',
]

extras_require = {
    'docs': ['Sphinx>=1.4.2'],
    'tests': ['pytest>=2.7'],
    'flask': ['Flask>=0.11'],
    ':python_version=="2.7"': [
        'ipaddr>=2.1.11'
    ]
}

setup(
    name='testpkh',
    version=testpkh.__version__,
    install_requires=requirements,
    extras_require=extras_require,
)
