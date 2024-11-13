POLICY_DIR  ?= /etc/qubes/policy.d
POLICY_FILE ?= 50-dom0-shell.policy
RPC_DIR     ?= /etc/qubes-rpc

.DEFAULT_GOAL := install

install:
	install -d $(DESTDIR)$(RPC_DIR)
	install -d $(DESTDIR)$(POLICY_DIR)
	install -m 0755 qubes.Dom0Shell $(DESTDIR)$(RPC_DIR)/qubes.Dom0Shell
	install -m 0644 50-dom0-shell.policy $(DESTDIR)$(POLICY_DIR)/$(POLICY_FILE)
