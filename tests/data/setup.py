# SPDX-FileCopyrightText: 2015, 2016, 2017, 2018 CERN.
# SPDX-License-Identifier: BSD-3-Clause
#
"""Build requirements files from setup.py requirements."""

import os

import testpkh
from setuptools import setup

dirname = os.path.dirname(__file__)

requirements = [
    'click>=5.0.0',
    'mock>=1.3.0',
    'CairoSVG<2.0.0,>=1.0.20',
    'functools32>=3.2.3-2; python_version=="2.7"',
    'invenio-records~=1.0.0',
    'invenio[base,auth,metadata]>=3.0.0',
]

extras_require = {
    'docs': ['Sphinx>=1.4.2'],
    'tests': ['pytest>=2.7'],
    'flask': ['Flask>=0.11'],
    ':python_version=="2.7"': ['ipaddr>=2.1.11']
}

setup(
    name='testpkh',
    version=testpkh.__version__,
    install_requires=requirements,
    extras_require=extras_require,
)
