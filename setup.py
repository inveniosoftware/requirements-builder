# -*- coding: utf-8 -*-
#
# This file is part of Requirements-Builder
# Copyright (C) 2015, 2016, 2017 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.
#
"""Build requirements files from setup.py requirements."""

import os

from setuptools import setup

# Get the version string.  Cannot be done with import!
g = {}
with open(os.path.join('requirements_builder', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as history_file:
    history = history_file.read().replace('.. :changes:', '')

install_requires = [
    'click>=5.0.0',
    'mock>=1.3.0',
]

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.0.0',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=2.0.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx<1.5.0,>=1.4.2',
        'docutils<0.13,>=0.12',
    ],
    'tests': tests_require,
}

extras_require['all'] = extras_require['tests'] + extras_require['docs']

setup_requires = ['pytest-runner>=2.6.2', ]

setup(
    name='requirements-builder',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    author="Invenio Collaboration",
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/requirements-builder',
    entry_points={
        'console_scripts':
            ["requirements-builder = requirements_builder.cli:cli"]
    },
    packages=['requirements_builder', ],
    include_package_data=True,
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    license='BSD',
    zip_safe=False,
    keywords='requirements-builder',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
