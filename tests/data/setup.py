# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015, 2016 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Build requirements files from setup.py requirements."""

from setuptools import setup

import os

dirname = os.path.dirname(__file__)

requirements = [
    'click>=5.0.0',
    'mock>=1.3.0',
]

setup(
    name='testpkh',
    install_requires=requirements,
)
