# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2017 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.
#
"""Build requirements files from setup.py requirements."""

import testpkh
from setuptools import setup

requirements = [
    'click>=5.0.0',
]

extras_require = {
    'docs': ['Sphinx>=1.4.2'],
}

if __name__ == "__main__":
    setup(
        name='testpkh',
        version=testpkh.__version__,
        install_requires=requirements,
        extras_require=extras_require,
    )
