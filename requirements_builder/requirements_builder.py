# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015, 2016, 2017 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.
#
"""Generate requirements from `setup.py` and `requirements-devel.txt`."""

from __future__ import absolute_import, print_function

import os
import re
import sys

import mock
import pkg_resources
import setuptools


def parse_set(string):
    """Parse set from comma separated string."""
    string = string.strip()
    if string:
        return set(string.split(","))
    else:
        return set()


def minver_error(pkg_name):
    """Report error about missing minimum version constraint and exit."""
    print(
        'ERROR: specify minimal version of "{0}" using '
        '">=" or "=="'.format(pkg_name),
        file=sys.stderr
    )
    sys.exit(1)


def parse_pip_file(path):
    """Parse pip requirements file."""
    # requirement lines sorted by importance
    # also collect other pip commands
    rdev = {}
    rnormal = []
    stuff = []

    try:
        with open(path) as f:
            for line in f:
                line = line.strip()

                # see https://pip.readthedocs.io/en/1.1/requirements.html
                if line.startswith('-e'):
                    # devel requirement
                    splitted = line.split('#egg=')
                    rdev[splitted[1].lower()] = line

                elif line.startswith('-r'):
                    # recursive file command
                    splitted = re.split('-r\\s+', line)
                    subrdev, subrnormal, substuff = parse_pip_file(splitted[1])
                    for k, v in subrdev.iteritems():
                        if k not in rdev:
                            rdev[k] = v
                    rnormal.extend(subrnormal)
                elif line.startswith('-'):
                    # another special command we don't recognize
                    stuff.append(line)
                else:
                    # ordinary requirement, similarly to them used in setup.py
                    rnormal.append(line)
    except IOError:
        print(
            'Warning: could not parse requirements file "{0}"!',
            file=sys.stderr
        )

    return rdev, rnormal, stuff


def iter_requirements(level, extras, pip_file, setup_fp):
    """Iterate over requirements."""
    result = dict()
    requires = []
    stuff = []
    if level == 'dev':
        result, requires, stuff = parse_pip_file(pip_file)

    with mock.patch.object(setuptools, 'setup') as mock_setup:
        sys.path.append(os.path.dirname(setup_fp.name))
        g = {'__file__': setup_fp.name}
        exec(setup_fp.read(), g)
        sys.path.pop()
        assert g['setup']  # silence warning about unused imports

    # called arguments are in `mock_setup.call_args`
    mock_args, mock_kwargs = mock_setup.call_args
    install_requires = mock_kwargs.get('install_requires', [])
    install_requires.extend(requires)

    requires_extras = mock_kwargs.get('extras_require', {})
    for e, reqs in requires_extras.items():
        # Handle conditions on extras. See pkginfo_to_metadata function
        # in Wheel for details.
        condition = ''
        if ':' in e:
            e, condition = e.split(':', 1)
        if not e or e in extras:
            if condition:
                reqs = ['{0}; {1}'.format(r, condition) for r in reqs]
            install_requires.extend(reqs)

    for pkg in pkg_resources.parse_requirements(install_requires):
        # skip things we already know
        # FIXME be smarter about merging things

        # Evaluate environment markers skip if not applicable
        if hasattr(pkg, 'marker') and pkg.marker is not None:
            if not pkg.marker.evaluate():
                continue
            else:
                # Remove markers from the output
                pkg.marker = None

        if pkg.key in result:
            continue

        specs = dict(pkg.specs)
        if (('>=' in specs) and ('>' in specs)) \
                or (('<=' in specs) and ('<' in specs)):
            print(
                'ERROR: Do not specify such weird constraints! '
                '("{0}")'.format(pkg),
                file=sys.stderr
            )
            sys.exit(1)

        if '==' in specs:
            result[pkg.key] = '{0}=={1}'.format(pkg.project_name, specs['=='])

        elif '>=' in specs:
            if level == 'min':
                result[pkg.key] = '{0}=={1}'.format(
                    pkg.project_name, specs['>=']
                )
            else:
                result[pkg.key] = pkg

        elif '>' in specs:
            if level == 'min':
                minver_error(pkg.project_name)
            else:
                result[pkg.key] = pkg

        else:
            if level == 'min':
                minver_error(pkg.project_name)
            else:
                result[pkg.key] = pkg.project_name

    for s in stuff:
        yield s

    for k in sorted(result.keys()):
        yield str(result[k])
