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

import sys
from os.path import abspath, dirname, join

from requirements_builder import __version__, iter_requirements

REQ = abspath(join(dirname(__file__), "./fixtures/requirements.devel.txt"))
SETUP = abspath(join(dirname(__file__), "./fixtures/setup.txt"))


def _has_toml_lib():
    if sys.version_info.major == 3 and sys.version_info.minor < 11:
        return False
    else:
        return True


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
            expected = ['click==7.0', 'mock==1.3.0']
            if not _has_toml_lib():
                expected.append("tomli==2.0.0")
            assert list(iter_requirements("min", [], '', f, g)) == \
                expected

    # PyPI
    with open(setup) as f:
        with open(setup_cfg) as g:
            expected = ['click>=7.0', 'mock<4,>=1.3.0']
            if not _has_toml_lib():
                expected.append("tomli>=2.0.0")
            assert list(iter_requirements("pypi", [], '', f, g)) == \
                expected

    # Dev
    with open(setup) as f:
        with open(setup_cfg) as g:
            expected = ['click>=7.0', 'mock<4,>=1.3.0']
            if not _has_toml_lib():
                expected.append("tomli>=2.0.0")
            assert list(iter_requirements("dev", [], req, f, g)) == \
                expected


def test_iter_requirements_toml():
    """Test requirements-builder for
    pyproject.toml (pep621)."""

    setup_py = abspath(
        join(dirname(__file__), "fixtures", "setup_py_placeholder.txt")
        )
    pyproject_toml = abspath(
        join(dirname(__file__), "fixtures", "pyproject.toml")
        )
    req = abspath(join(dirname(__file__), "../requirements.devel.txt"))

    # Min
    with open(setup_py) as setup_py_fp:
        with open(pyproject_toml, 'rb') as pyproject_toml_fp:
            expected = ['click==7.0', 'mock==1.3.0']
            if not _has_toml_lib():
                expected.append("tomli==2.0.0")
            assert list(iter_requirements(
                    "min",
                    [],
                    '',
                    setup_fp=setup_py_fp,
                    pyproject_toml_fp=pyproject_toml_fp
                    )) == expected
    # # PyPI
    with open(setup_py) as setup_py_fp:
        with open(pyproject_toml, 'rb') as pyproject_toml_fp:
            expected = ['click>=7.0', 'mock<4,>=1.3.0']
            if not _has_toml_lib():
                expected.append("tomli>=2.0.0")
            assert list(iter_requirements(
                    "pypi",
                    [],
                    '',
                    setup_fp=setup_py_fp,
                    pyproject_toml_fp=pyproject_toml_fp
                    )) == expected

    # Dev
    with open(setup_py) as setup_py_fp:
        with open(pyproject_toml, 'rb') as pyproject_toml_fp:
            expected = ['click>=7.0', 'mock<4,>=1.3.0']
            if not _has_toml_lib():
                expected.append("tomli>=2.0.0")
            assert list(iter_requirements(
                    "dev",
                    [],
                    req,
                    setup_fp=setup_py_fp,
                    pyproject_toml_fp=pyproject_toml_fp
                    )) == expected
