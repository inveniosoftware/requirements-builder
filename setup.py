# -*- coding: utf-8 -*-
#
# This file is part of Requirements Builder
# Copyright (C) 2015 CERN.
#
# Requirements Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Build requirements files from setup.py requirements."""

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    """Integration of PyTest with setuptools."""

    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        """Initialize options."""
        TestCommand.initialize_options(self)
        try:
            from ConfigParser import ConfigParser
        except ImportError:
            from configparser import ConfigParser
        config = ConfigParser()
        config.read("pytest.ini")
        self.pytest_args = config.get("pytest", "addopts").split(" ")

    def finalize_options(self):
        """Finalize options."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run tests."""
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# Get the version string.  Cannot be done with import!
g = {}
with open(os.path.join('requirements_builder', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as history_file:
    history = history_file.read().replace('.. :changes:', '')

requirements = [
    'click>=5.0.0',
    'mock>=1.3.0',
]

test_requirements = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.0.0',
    'pep257>=0.6.0',
    'pytest-cache>=1.0',
    'pytest-cov>=2.0.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_requirements = {
    'docs': [
        'Sphinx>=1.3',
    ],
    'tests': test_requirements,
}
extras_requirements['all'] = \
    extras_requirements['tests'] + \
    extras_requirements['docs']

setup(
    name='requirements-builder',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    author="Invenio Collaboration",
    author_email='info@invenio-software.org',
    url='https://github.com/inveniosoftware/requirements-builder',
    entry_points={
        'console_scripts': [
            "requirements-builder = requirements_builder.cli:cli"
        ]
    },
    packages=[
        'requirements_builder',
    ],
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_requirements,
    license="BSD",
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
    ],
    tests_require=test_requirements,
    cmdclass={'test': PyTest},
)
