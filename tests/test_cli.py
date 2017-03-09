# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015, 2016, 2017 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.
#
"""Tests for CLI module."""

import shutil
import sys
from os import getcwd
from os.path import abspath, dirname, join

from click.testing import CliRunner
from requirements_builder.cli import cli

DATA = abspath(join(dirname(__file__), 'data/'))


def test_cli():
    """Test cli."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        shutil.copytree(DATA, abspath(join(getcwd(), 'data/')))
        result = runner.invoke(cli, ['-l', 'min', 'data/setup.py'])
        assert result.exit_code == 0
        if sys.version_info[:2] == (2, 7):
            assert result.output == \
                'click==5.0.0\n' \
                'functools32==3.2.3-2\n' \
                'ipaddr==2.1.11\n' \
                'mock==1.3.0\n'
        else:
            assert result.output == 'click==5.0.0\nmock==1.3.0\n'

        result = runner.invoke(cli, ['-l', 'pypi', 'data/setup.py'])
        assert result.exit_code == 0

        if sys.version_info[:2] == (2, 7):
            assert result.output == 'click>=5.0.0\n' \
                'functools32>=3.2.3-2\n' \
                'ipaddr>=2.1.11\n' \
                'mock>=1.3.0\n'
        else:
            assert result.output == 'click>=5.0.0\nmock>=1.3.0\n'

        result = runner.invoke(cli, ['-l', 'dev', 'data/setup.py'])
        assert result.exit_code == 2

        result = runner.invoke(
            cli, ['-l', 'dev', '-r', 'data/req.txt', 'data/setup.py']
        )
        assert result.exit_code == 0
        if sys.version_info[:2] == (2, 7):
            assert result.output == \
                '-e git+https://github.com/mitsuhiko/click.git#egg=click\n' \
                'Cython>=0.20\n' \
                'functools32>=3.2.3-2\n' \
                'ipaddr>=2.1.11\n' \
                'mock>=1.3.0\n'
        else:
            assert result.output == \
                '-e git+https://github.com/mitsuhiko/click.git#egg=click\n' \
                'Cython>=0.20\n' \
                'mock>=1.3.0\n'

        result = runner.invoke(
            cli, ['-l', 'min', '-o', 'requirements.txt', 'data/setup.py']
        )
        assert result.exit_code == 0
        assert result.output == ''
        with open(join(getcwd(), 'requirements.txt')) as f:
            if sys.version_info[:2] == (2, 7):
                assert f.read() == \
                    'click==5.0.0\n' \
                    'functools32==3.2.3-2\n' \
                    'ipaddr==2.1.11\n' \
                    'mock==1.3.0\n'
            else:
                assert f.read() == \
                    'click==5.0.0\nmock==1.3.0\n'


def test_cli_extras():
    """Test cli option extras."""
    runner = CliRunner()
    output = ['click==5.0.0', 'mock==1.3.0']
    if sys.version_info[:2] == (2, 7):
        output.append('functools32==3.2.3-2')
        output.append('ipaddr==2.1.11')
    with runner.isolated_filesystem():
        shutil.copytree(DATA, abspath(join(getcwd(), 'data/')))
        result = runner.invoke(
            cli, ['-l', 'min', '-e', 'docs', 'data/setup.py']
        )
        assert result.exit_code == 0
        assert set(result.output.split('\n')
                   ) == set(output + ['Sphinx==1.4.2', ''])

        result = runner.invoke(
            cli, ['-l', 'min', '-e', 'docs, tests', 'data/setup.py']
        )
        assert result.exit_code == 0
        assert set(result.output.split('\n')
                   ) == set(output + ['pytest==2.7', 'Sphinx==1.4.2', ''])

        result = runner.invoke(
            cli,
            ['-l', 'min', '-e', 'docs, tests', '-e', 'flask', 'data/setup.py']
        )
        assert result.exit_code == 0
        assert set(result.output.split('\n')) == set(
            output + ['pytest==2.7', 'Sphinx==1.4.2', 'Flask==0.11', '']
        )
