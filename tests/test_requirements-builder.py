# -*- coding: utf-8 -*-
#
# This file is part of Requirements Builder
# Copyright (C) 2015 CERN.
#
# Requirements Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.


"""Tests for `requirements-builder` module."""

from requirements_builder import __version__


def test_version():
    """Test requirements-builder."""
    assert __version__
