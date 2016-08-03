Qubes Dom0 Shell RPC Service
====
WARNING: This RPC service gives client VMs *full* system control!
----
This has two components; a package for Dom0 and a package for client VMs.

The Dom0 package has a simple RPC service definition that uses socat to allocate a virtual pty. The default policy allows no connections by default; for a server instance, you'll want to add your trusted admin VM to the whitelist in the RPC policy file.

The client package has just one simple script: `qubes-dom0-shell` that invokes socat and the RPC service to drop a shell.
