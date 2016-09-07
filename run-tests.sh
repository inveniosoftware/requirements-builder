# This file is part of Requirements-Builder
# Copyright (C) 2015, 2016 CERN.
#
# Requirements-Builder is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

pydocstyle requirements_builder && \
#isort -rc -c -vb -df -sp .isort.cfg **/*.py && \
check-manifest && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test && \
sphinx-build -qnNW -b doctest docs docs/_build/doctest
