=============================
 Requirements-Builder v0.2.0
=============================

Requirements-Builder v0.2.0 was released on September 13, 2016.

About
-----

Build requirements files from setup.py requirements.

New features
~~~~~~~~~~~~

- Adds an output option which is useful in the tox context where one
  cannot redirect the output to a file. See more at
  https://bitbucket.org/hpk42/tox/issues/73/pipe-output-of-command-into-file

Bug fixes
---------

- Fixes problem when the setup.py command try to import the package
  its about to install in order to get the information like the
  version. E.g. Django does that.
- Fixes problem when the setup.py command plays with `__file__`  to
  read, exec, or whatever.

Installation
------------

   $ pip install requirements-builder==0.2.0

Documentation
-------------

   http://requirements-builder.readthedocs.io/

Happy hacking and thanks for flying Requirements-Builder.

| Invenio Development Team
|   Email: info@inveniosoftware.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/requirements-builder
|   URL: http://inveniosoftware.org
