# Qubes Dom0 Shell RPC Service

[![Hippocratic License HL3-FULL](https://img.shields.io/static/v1?label=Hippocratic%20License&message=HL3-FULL&labelColor=5e2751&color=bc8c3d)](https://firstdonoharm.dev/version/3/0/full.html)

> [!WARNING]  
> This RPC service gives client VMs _full_ system control!

This has two components; a package for dom0 (`qubes-app-dom0-shell`) and a package for client VMs (`qubes-app-dom0-shell-client`).

The dom0 package has a simple RPC service definition that uses socat to allocate a virtual pty. The default policy allows no connections by default; for a server instance, you'll want to add your trusted admin VM to the whitelist in the RPC policy file.

The client package has just one simple script: `qubes-dom0-shell` that invokes socat and the RPC service to drop a shell.

### Why to Use:

- If dom0 isn't always available (i.e. if you're using `sys-gui`)
- If you want to get proper remote access to a Qubes system
- If you like taking risks

### How to Install

1. Clone or download this repo into any qube (for example a disposable VM)

1. The `Makefile` in the root directory detects the current qube's name and runs the appropriate installer

   - If you're anal, you can manually run the appropriate `make install` tasks. For dom0, run `make install` in `./src/dom0`. In the desired domU, run the `make install` task found in `./src/domU`

1. Configure your RPC policies. By default, the dom0 installation task installs a policy that doesn't allow any VMs to get a shell. There are a few example rules in the policy file which you can make use of, or write your own:

   ```diff
   # qubes.Dom0Shell  *  @anyvm       @default  ask  default_target=dom0
   # qubes.Dom0Shell  *  sys-gui      @default  allow target=dom0 notify=yes
   # qubes.Dom0Shell  *  sys-gui-gpu  @default  allow target=dom0 notify=yes

   + qubes.Dom0Shell  *  my-super-privileged-qube  @default  ask default_target=dom0

   qubes.Dom0Shell  *  @anyvm  @anyvm    deny notify=yes
   ```

   - Bear in mind that if you choose to set this up for a [GUI domain](https://www.qubes-os.org/doc/gui-domain/), the GUI domain won't have its own `guivm` configured. This means that `ask` won't work, and it will automatically reject.

### Other Solutions

- [Safe Remote dom0 terminals](https://www.qubes-os.org/doc/safe-remote-ttys/)
