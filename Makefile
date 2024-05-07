ifeq ($(wildcard /code),)
PYTHON=PYTHONPATH=$$PYTHONPATH:../.. python3
else
PYTHON=python3
endif

MANAGE_PY=$(PYTHON) manage.py

.PHONY:
migrate:
	$(MANAGE_PY) migrate

.PHONY:
makeadmin:
	$(MANAGE_PY) createsuperuser --noinput || true

.PHONY:
runserver:
	$(MANAGE_PY) runserver 0.0.0.0:8000
