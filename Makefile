.PHONY: test upload clean bootstrap

SHELL=/bin/bash

_build_bin:
	@for a in $$(find ./src/bin -type d); do \
	if [ -d $$a ]; then \
	echo "processing folder $$a"; \
	if [ -f $$a/Makefile ]; then \
	$(MAKE) -C $$a; \
	fi; \
	fi; \
	done;
	@echo "Done!"


test: _activate


build: _build_bin	


_create_commands:
	for n in $(find ./src/bin -name "*.py"); do cp $n ./bin/rollout-$(basename $n | sed s'/\.py//'g); done
	chmod +x ./bin/rollout-*

upload: 
	make clean

	
register:
	python setup.py register

clean:
	rm -rf venv
	rm -rf build/*
	rm -rf bin/rollout-*
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	
bootstrap: _virtualenv
ifneq ($(wildcard setup.py),)
	venv/bin/pip install -e .
endif
ifneq ($(wildcard requirements.txt),) 
	venv/bin/pip install -r requirements.txt
endif

_virtualenv_init: 
	python3 -m venv venv

_virtualenv: _virtualenv_init
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
