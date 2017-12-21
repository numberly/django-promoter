Django Promoter
===============

|License: MIT| |PyPI version|

    Give me the damn rights.

Current Features
--------

-  Promote an existing user
-  Demote an existing user

Installation
------------

-  

   1. Install using ``pip install django-promoter``

-  

   2. Add ``'django_promoter'`` to your ``'INSTALLED_APPS'`` settings

-  

   3. You can now access the ``promote`` and ``demote`` commands from
      your ``./manage.py``

Usage
-----

Promote a user
^^^^^^^^^^^^^^

.. code:: bash

    $ ./manage.py promote username

Demote a user
~~~~~~~~~~~~~

.. code:: bash

    $ ./manage.py demote username

Why would I use this ?
----------------------

There are some specific some use-cases, such as the one you can encounter,
while having a RO backend. (Such as LDAP)


.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
.. |PyPI version| image:: https://badge.fury.io/py/promoter.svg
   :target: https://badge.fury.io/py/promoter
