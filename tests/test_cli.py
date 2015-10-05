# -*- coding: utf-8 -*-
#
# This file is part of Requirements Builder
# Copyright (C) 2015 CERN.
#
# Requirements Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.


"""Tests for CLI module."""

import shutil
from os import getcwd
from os.path import abspath, dirname, join

from click.testing import CliRunner
from requirements_builder.cli import cli

DATA = abspath(join(dirname(__file__), "data/"))


def test_cli():
    """Test cli."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        shutil.copytree(DATA, abspath(join(getcwd(), "data/")))
        result = runner.invoke(cli, ['-l', 'min', 'data/setup.py'])
        assert result.exit_code == 0
        assert result.output == "click==5.0.0\nmock==1.3.0\n"

        result = runner.invoke(cli, ['-l', 'pypi', 'data/setup.py'])
        assert result.exit_code == 0
        assert result.output == "click>=5.0.0\nmock>=1.3.0\n"

        result = runner.invoke(cli, ['-l', 'dev', 'data/setup.py'])
        assert result.exit_code == 2

        result = runner.invoke(
            cli, ['-l', 'dev', '-r', 'data/req.txt', 'data/setup.py'])
        assert result.exit_code == 0
        assert result.output == \
            "-e git+https://github.com/mitsuhiko/click.git#egg=click\n" \
            "mock>=1.3.0\n"
