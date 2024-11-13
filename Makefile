qube_name := $(shell qubesdb-read /name)

.DEFAULT_GOAL := install

install:
	if [ "$(qube_name)" == "dom0" ]; then $(MAKE) -C src/dom0 install; \
	else $(MAKE) -C src/domU install; fi
