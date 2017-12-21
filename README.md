# Django Promoter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/django-promoter.svg)](https://badge.fury.io/py/django-promoter)

> Give me the damn rights already.

## Features

- Promote an existing user
- Demote an existing user


## Installation

- 1. Install using `pip install django-promoter`
- 2. Add `'django_promoter'` to your `'INSTALLED_APPS'` settings
- 3. You can now access the `promote` and `demote` commands from your `./manage.py`


## Usage

#### Promote a user

```bash
$ ./manage.py promote username
```

### Demote a user

```bash
$ ./manage.py promote username
```

## Why would I use this ?

There are some specific some use-cases, such as the one I encountered,
which was about having some users on an LDAP server, and I had some
issues granting superuser rights to myself.

I didn't find such a tool, so I made this simple commands.

In addition, I'm totally a CLI guy, I plan on not having to log
into the admin panel, because it's not really my thing.
