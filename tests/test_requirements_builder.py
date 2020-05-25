# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.
#
"""Tests for `requirements-builder` module."""

from os.path import abspath, dirname, join

from requirements_builder import __version__, iter_requirements

REQ = abspath(join(dirname(__file__), "./fixtures/requirements.devel.txt"))
SETUP = abspath(join(dirname(__file__), "./fixtures/setup.txt"))


def test_version():
    """Test requirements-builder."""
    assert __version__


def test_iter_requirements():
    """Test requirements-builder."""
    # Min
    with open(SETUP) as f:
        assert list(iter_requirements("min", [], '', f)) == \
            ['click==6.1.0', 'mock==1.3.0']

    # PyPI
    with open(SETUP) as f:
        assert list(iter_requirements("pypi", [], '', f)) == \
            ['click>=6.1.0', 'mock>=1.3.0']

    # Dev
    with open(SETUP) as f:
        assert list(iter_requirements("dev", [], REQ, f)) == \
            ['-e git+https://github.com/pallets/click.git#egg=click',
             'mock>=1.3.0']


def test_iter_requirements_cfg():
    """Test requirements-builder."""
    req = abspath(join(dirname(__file__), "../requirements.devel.txt"))
    setup = abspath(join(dirname(__file__), "../setup.py"))
    setup_cfg = abspath(join(dirname(__file__), "../setup.cfg"))

    # Min
    with open(setup) as f:
        with open(setup_cfg) as g:
            assert list(iter_requirements("min", [], '', f, g)) == \
                ['click==6.1.0', 'mock==1.3.0']

    # PyPI
    with open(setup) as f:
        with open(setup_cfg) as g:
            assert list(iter_requirements("pypi", [], '', f, g)) == \
                ['click>=6.1.0', 'mock<4,>=1.3.0']

    # Dev
    with open(setup) as f:
        with open(setup_cfg) as g:
            assert list(iter_requirements("dev", [], req, f, g)) == \
                ['click>=6.1.0', 'mock<4,>=1.3.0']
