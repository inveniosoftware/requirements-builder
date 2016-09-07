..
    This file is part of Requirements-Builder
    Copyright (C) 2015, 2016 CERN.

    Requirements-Builder is free software; you can redistribute it and/or
    modify it under the terms of the Revised BSD License; see LICENSE
    file for more details.

.. :changes:

Changes
=======

Version 0.2.0 (released 2016-09-13)
-----------------------------------

New features
~~~~~~~~~~~~

- Adds an output option which is useful in the tox context where one
  cannot redirect the output to a file. See more at
  https://bitbucket.org/hpk42/tox/issues/73/pipe-output-of-command-into-file

Bug fixes
~~~~~~~~~

- Fixes problem when the setup.py command try to import the package
  its about to install in order to get the information like the
  version. E.g. Django does that.
- Fixes problem when the setup.py command plays with `__file__`  to
  read, exec, or whatever.


Version 0.1.0 (released 2015-10-05)
-----------------------------------

- Initial public release
