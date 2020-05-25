# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015, 2016, 2017 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.
#
"""CLI for requirements builder."""

from __future__ import absolute_import, print_function

import os.path

import click

from .requirements_builder import iter_requirements


@click.command()
@click.option(
    '--level',
    '-l',
    default='pypi',
    type=click.Choice(['min', 'pypi', 'dev']),
    help='Specifies desired requirements level.'
    '"min" requests the minimal requirement that is specified, '
    '"pypi" requests the maximum version that satisfies the '
    'constrains and is available in PyPi. '
    '"dev" includes experimental developer versions for VCSs.'
)
@click.option(
    '--extras',
    '-e',
    default='',
    help='Comma separated list of extras.',
    multiple=True
)
@click.option(
    '--req',
    '-r',
    default=None,
    help='Requirements file.',
    metavar='PATH',
    type=click.Path(
        exists=True, dir_okay=False, readable=True, resolve_path=True
    )
)
@click.option(
    '--output', '-o', default='-', help='Output file.', type=click.File('w')
)
@click.argument('setup', type=click.File('rb'), required=False)
@click.pass_context
def cli(ctx, level, extras, req, output, setup):
    """Calculate requirements for different purposes."""
    if level == 'dev' and not req:
        raise click.UsageError(
            "You must specify --req when using 'dev' level."
        )
    if not setup and not req:
        raise click.MissingParameter(
            ctx=ctx, param_hint='"setup"', param_type='argument'
        )
    extras = set(req.strip() for extra in extras for req in extra.split(','))

    # figure out the setup.cfg file
    setup_cfg = None

    if setup:
        cfg = os.path.splitext(setup.name)[0] + ".cfg"
        if os.path.exists(cfg):
            setup_cfg = file.open(cfg, 'r')

    try:
        lines = (
            '{0}\n'.format(req)
            for req in iter_requirements(level, extras, req, setup, setup_cfg)
        )
        output.writelines(lines)
    finally:
        if setup_cfg:
            setup_cfg.close()
