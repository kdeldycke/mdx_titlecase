Markdown title-casing extension
===============================

`Python's Markdown <https://pythonhosted.org/Markdown/>`_ extension to apply
proper English title-casing.

This project use `titlecase <https://pypi.python.org/pypi/titlecase>`_ module
under the hood. Transformation is applied on content enclosed in ``<h1>`` to
``<h6>`` HTML tags. `Meta-Data extension
<https://pythonhosted.org/Markdown/extensions/meta_data.html>`_ is supported so
that document title can be transformed too.

Stable release: |release| |license| |dependencies| |popularity|

Development: |build| |coverage| |quality|

.. |release| image:: https://img.shields.io/pypi/v/mdx_titlecase.svg?style=flat
    :target: https://pypi.python.org/pypi/mdx_titlecase
    :alt: Last release
.. |license| image:: https://img.shields.io/pypi/l/mdx_titlecase.svg?style=flat
    :target: https://www.gnu.org/licenses/gpl-2.0.html
    :alt: Software license
.. |popularity| image:: https://img.shields.io/pypi/dm/mdx_titlecase.svg?style=flat
    :target: https://pypi.python.org/pypi/mdx_titlecase#downloads
    :alt: Popularity
.. |dependencies| image:: https://img.shields.io/requires/github/kdeldycke/mdx_titlecase/master.svg?style=flat
    :target: https://requires.io/github/kdeldycke/mdx_titlecase/requirements/?branch=master
    :alt: Requirements freshness
.. |build| image:: https://img.shields.io/travis/kdeldycke/mdx_titlecase/develop.svg?style=flat
    :target: https://travis-ci.org/kdeldycke/mdx_titlecase
    :alt: Unit-tests status
.. |coverage| image:: https://codecov.io/github/kdeldycke/mdx_titlecase/coverage.svg?branch=develop
    :target: https://codecov.io/github/kdeldycke/mdx_titlecase?branch=develop
    :alt: Coverage Status
.. |quality| image:: https://img.shields.io/scrutinizer/g/kdeldycke/mdx_titlecase.svg?style=flat
    :target: https://scrutinizer-ci.com/g/kdeldycke/mdx_titlecase/?branch=develop
    :alt: Code Quality


Install
-------

This package is `available on PyPi
<https://pypi.python.org/pypi/mdx_titlecase>`_, so you can install the
latest stable release and its dependencies with a simple `pip` call:

.. code-block:: bash

    $ pip install mdx_titlecase

See also `pip installation instructions
<https://pip.pypa.io/en/stable/installing/>`_.


Configuration
-------------

+--------------+-----------------+--------------------------------------------+
| Parameter    | Default value   | Description                                |
+==============+=================+============================================+
| ``metadata`` | ``['title', ]`` | List of metadata keys to which apply       |
|              |                 | titlecasing.                               |
+--------------+-----------------+--------------------------------------------+


Development
-----------

Check out latest development branch:

.. code-block:: bash

    $ git clone git@github.com:kdeldycke/mdx_titlecase.git
    $ cd ./mdx_titlecase
    $ python ./setup.py develop

Run unit-tests:

.. code-block:: bash

    $ python ./setup.py nosetests

Run `PEP8 <https://pep8.readthedocs.org>`_ and `Pylint
<http://docs.pylint.org>`_ code style checks:

.. code-block:: bash

    $ pip install pep8 pylint
    $ pep8 mdx_titlecase
    $ pylint --rcfile=setup.cfg mdx_titlecase


Stability policy
----------------

Here is a bunch of rules we're trying to follow regarding stability:

* Patch releases (``0.x.n`` → ``0.x.(n+1)`` upgrades) are bug-fix only. These
  releases must not break anything and keeps backward-compatibility with
  ``0.x.*`` and ``0.(x-1).*`` series.

* Minor releases (``0.n.*`` → ``0.(n+1).0`` upgrades) includes any non-bugfix
  changes. These releases must be backward-compatible with any ``0.n.*``
  version but are allowed to drop compatibility with the ``0.(n-1).*`` series
  and below.

* Major releases (``n.*.*`` → ``(n+1).0.0`` upgrades) are not planned yet:
  we're still in beta and the final feature set of the ``1.0.0`` release is not
  decided yet.


Release process
---------------

Start from the ``develop`` branch:

.. code-block:: bash

    $ git clone git@github.com:kdeldycke/mdx_titlecase.git
    $ git checkout develop

Revision should already be set to the next version, so we just need to set the
released date in the changelog:

.. code-block:: bash

    $ vi ./CHANGES.rst

Create a release commit, tag it and merge it back to ``master`` branch:

.. code-block:: bash

    $ git add ./mdx_titlecase/__init__.py ./CHANGES.rst
    $ git commit -m "Release vX.Y.Z"
    $ git tag "vX.Y.Z"
    $ git push
    $ git push --tags
    $ git checkout master
    $ git pull
    $ git merge "vX.Y.Z"
    $ git push

Push packaging to the `test cheeseshop
<https://wiki.python.org/moin/TestPyPI>`_:

.. code-block:: bash

    $ pip install wheel
    $ python ./setup.py register -r testpypi
    $ python ./setup.py clean
    $ rm -rf ./build ./dist
    $ python ./setup.py sdist bdist_egg bdist_wheel upload -r testpypi

Publish packaging to `PyPi <https://pypi.python.org>`_:

.. code-block:: bash

    $ python ./setup.py register -r pypi
    $ python ./setup.py clean
    $ rm -rf ./build ./dist
    $ python ./setup.py sdist bdist_egg bdist_wheel upload -r pypi

Bump revision back to its development state:

.. code-block:: bash

    $ pip install bumpversion
    $ git checkout develop
    $ bumpversion --verbose patch
    $ git add ./mdx_titlecase/__init__.py ./CHANGES.rst
    $ git commit -m "Post release version bump."
    $ git push

Now if the next revision is no longer bug-fix only:

.. code-block:: bash

    $ bumpversion --verbose minor
    $ git add ./mdx_titlecase/__init__.py ./CHANGES.rst
    $ git commit -m "Next release no longer bug-fix only. Bump revision."
    $ git push


License
-------

This software is licensed under the `GNU General Public License v2 or later
(GPLv2+)
<https://github.com/kdeldycke/mdx_titlecase/blob/master/LICENSE>`_.
