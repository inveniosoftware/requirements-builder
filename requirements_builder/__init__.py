# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Build requirements files from setup.py requirements.

.. code-block:: console

   $ requirements-builder --help
   Usage: requirements-builder [OPTIONS] SETUP

     Calculate requirements for different purposes.

   Options:
     -l, --level [min|pypi|dev]  Specifies desired requirements level."min"
                                 requests the minimal requirement that is
                                 specified, "pypi" requests the maximum version
                                 that satisfies the constrains and is available
                                 in PyPi. "dev" includes experimental developer
                                 versions for VCSs.
     -e, --extras TEXT           Comma separated list of extras.
     -r, --req PATH              Requirements file.
     --help                      Show this message and exit.

TravisCI
--------
Following is an example of how to integrate Requirements-Builder with
TravisCI:

.. code-block:: yaml

   env:
     - REQUIREMENTS=lowest
     - REQUIREMENTS=release
     - REQUIREMENTS=devel

   python:
     - "2.7"
     - "3.3"
     - "3.4"
     - "3.5"

   before_install:
     - "travis_retry pip install --upgrade pip"
     - "travis_retry pip install requirements-builder"
     - "requirements-builder --level=min setup.py
        > .travis-lowest-requirements.txt"
     - "requirements-builder --level=pypi setup.py
        > .travis-release-requirements.txt"
     - "requirements-builder --level=dev --req requirements-devel.txt setup.py
        > .travis-devel-requirements.txt"

   install:
     - "travis_retry pip install -r .travis-$REQUIREMENTS-requirements.txt"
     - "pip install -e ."
"""

from __future__ import absolute_import, print_function

from .requirements_builder import iter_requirements
from .version import __version__

__all__ = ('__version__',)
