..
    This file is part of Requirements-Builder
    Copyright (C) 2015 CERN.

    Requirements-Builder is free software; you can redistribute it and/or
    modify it under the terms of the Revised BSD License; see LICENSE
    file for more details.

======================
 Requirements-Builder
======================

.. image:: https://img.shields.io/travis/inveniosoftware/requirements-builder.svg
        :target: https://travis-ci.org/inveniosoftware/requirements-builder

.. image:: https://img.shields.io/coveralls/inveniosoftware/requirements-builder.svg
        :target: https://coveralls.io/r/inveniosoftware/requirements-builder

.. image:: https://img.shields.io/github/tag/inveniosoftware/requirements-builder.svg
        :target: https://github.com/inveniosoftware/requirements-builder/releases

.. image:: https://img.shields.io/pypi/dm/requirements-builder.svg
        :target: https://pypi.python.org/pypi/requirements-builder

.. image:: https://img.shields.io/github/license/inveniosoftware/requirements-builder.svg
        :target: https://github.com/inveniosoftware/requirements-builder/blob/master/LICENSE

About
=====

Build requirements from setup.py to test your package against minimum,
latest and development versions of your package dependencies. Particularly
useful when combined with your CI systems build matrix.

Installation
============

Requirements-Builder is on PyPI so all you need is::

    $ pip install requirements-builder

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv requirements-builder
    $ pip install requirements-builder

Testing
=======

Running the test suite is as simple as::

    $ ./run-tests.sh
