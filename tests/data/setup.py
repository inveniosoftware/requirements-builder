# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Build requirements files from setup.py requirements."""

from setuptools import setup

requirements = [
    'click>=5.0.0',
    'mock>=1.3.0',
    'invenio-db[versioning]>=1',
    'invenio-db[versioning,mysql]>=1',
    'invenio-db[versioning,postgresql]>=1',
]

setup(
    name='testpkh',
    install_requires=requirements,
)
