Qubes Dom0 Shell RPC Service
====
WARNING: This RPC service gives client VMs *full* system control!
----
This has two components; a package for Dom0 (`qubes-app-dom0-shell`) and a package for client VMs (`qubes-app-dom0-shell-client`).

The Dom0 package has a simple RPC service definition that uses socat to allocate a virtual pty. The default policy allows no connections by default; for a server instance, you'll want to add your trusted admin VM to the whitelist in the RPC policy file.

The client package has just one simple script: `qubes-dom0-shell` that invokes socat and the RPC service to drop a shell.

Why to Use:
----
- If you want to get proper remote access to a Qubes system
- If you like taking risks

How to Use:
----
1. Install the packages in Dom0 and the TemplateVM of your target VM.
2. Edit the Dom0 RPC policy file at `/etc/qubes-rpc/policy/qubes.Dom0Shell` to whitelist your target VM.
3. Run the client on your target VM:
```
user@targetvm$ qubes-dom0-shell
user@dom0$ 
```
