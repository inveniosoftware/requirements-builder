# SPDX-FileCopyrightText: 2017 CERN.
# SPDX-License-Identifier: BSD-3-Clause
#
"""Build requirements files from setup.py requirements."""

import testpkh
from setuptools import setup

requirements = [
    'click>=5.0.0',
]

extras_require = {
    'docs': ['Sphinx>=1.4.2'],
}

if __name__ == "__main__":
    setup(
        name='testpkh',
        version=testpkh.__version__,
        install_requires=requirements,
        extras_require=extras_require,
    )
