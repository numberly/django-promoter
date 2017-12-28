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

The main purpose of this project is to be able to manage rights when you 
have to use a read-only backend.
The `./manage.py createsuperuser` isn't available because you can't create
new users.
Using Django Promoter, once the user is inserted in the Django database,
you can promote him to a superuser without having to modify the auth database.

License
-------

The MIT License (MIT)

Copyright © 2017 Numberly


.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
.. |PyPI version| image:: https://badge.fury.io/py/promoter.svg
   :target: https://badge.fury.io/py/promoter
