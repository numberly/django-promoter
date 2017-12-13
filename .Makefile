VENV			= .venv
PYTHON_VERSION		= python3.5
PIP			= $(VENV)/bin/pip
PYTHON			= $(VENV)/bin/python
MANAGE			= $(PYTHON) ./manage.py
REQUIREMENTS		= requirements.txt
PORT			= 8000
HOST			= 127.0.0.1
ADMIN_USER		= admin
USERNAME		=

.PHONY: all clean collectstatic configure demoteuser \
	help install promoteuser serve syncdb test

all: help ## Display help

clean: ## Remove .venv and compiled files
	rm -fr $(VENV)
	find -name '*.py[co]' -delete

collectstatic: ## Collect static files in a location
	$(MANAGE) collectstatic

$(PYTHON):
	virtualenv --python $(PYTHON_VERSION) $(VENV)

configure: $(PYTHON) ## Set up the virtualenv

freeze: $(PYTHON) ## Freeze the dependencies
	$(PIP) freeze > $(REQUIREMENTS)

install: $(PYTHON) ## Install the dependencies
	$(PIP) install -r $(REQUIREMENTS)
	@echo "You should now promote a superuser from"
	@echo "the LDAP backend."
	@echo "'make promoteuser USERNAME=username'"

promoteuser: ## Promote a user to admin status
	$(MANAGE) promote $(USERNAME)

demoteuser: ## Demote a user to admin status
	$(MANAGE) demote $(USERNAME)

serve: ## Run the server on $PORT: Default=8000
	$(MANAGE) runserver $(HOST):$(PORT)

syncdb: ## Apply migrations
	$(MANAGE) makemigrations
	$(MANAGE) migrate

test: ## Run the unit tests
	$(MANAGE) test

help: ## List Makefile rules
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z_\-]*: *.*## *" \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; \
		{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
