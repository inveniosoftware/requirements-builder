..
    This file is part of Requirements-Builder
    Copyright (C) 2015, 2016, 2020 CERN.
    Copyright (C) 2018 Swiss Data Science Center (SDSC)
    A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
    Eidgenössische Technische Hochschule Zürich (ETHZ).

    Requirements-Builder is free software; you can redistribute it and/or
    modify it under the terms of the Revised BSD License; see LICENSE
    file for more details.

.. :changes:

Changes
=======

Version 0.4.0 (released 2020-05-25)
-----------------------------------

New features
~~~~~~~~~~~~

- Adds support for parsing setup.cfg.


Version 0.3.0 (released 2018-05-17)
-----------------------------------

New features
~~~~~~~~~~~~

- Includes package extras in the generated result.

Bug fixes
---------

- Fixes ``~=`` selector output by including the minimum version
  additionally to the X.* specifier.

Version 0.2.6 (released 2017-07-13)
-----------------------------------

Bug fixes
~~~~~~~~~

- Fixes fatal error if setup() is called under 'if __name__ == "__main__":'


Version 0.2.5 (released 2017-04-11)
-----------------------------------

Bug fixes
~~~~~~~~~

- Fixes support of recursive requirements files.

Version 0.2.4 (released 2017-03-10)
-----------------------------------

Bug fixes
~~~~~~~~~

- Fixes issue with upper version requirements being stripped from the output.

Version 0.2.3 (released 2017-03-09)
-----------------------------------

Bug fixes
~~~~~~~~~

- Fixes the issue with conditions on extra_require not being taken into
  account.

Version 0.2.2 (released 2017-02-01)
-----------------------------------

Bug fixes
~~~~~~~~~

- Fixes issue with properly building requirements for packages with version
  markers.

Improvements
~~~~~~~~~~~~

- Adds YAPF auto-formatting configuration.

Version 0.2.1 (released 2017-01-23)
-----------------------------------

Bug fixes
~~~~~~~~~

- Accepts non-`-e` packages from devel file.
- Sphinx 1.5+ drops support for Python 2.6 and 3.3.
- Adds Python 3.6 support.
- Makes `--extras` option accepting comma separated values as
  described in help.  (#14)


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
