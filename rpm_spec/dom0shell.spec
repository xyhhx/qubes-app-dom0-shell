%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%define version %(cat version)
%if 0%{?qubes_builder}
%define _builddir %(pwd)
%endif
    
Name:		qubes-app-dom0-shell
Version:	%{version}
Release:	1%{?dist}
Summary:	Qubes Dom0 Shell RPC Provider

Group:		System Environment/Daemons
License:	GPLv2
URL:		https://www.qubes-os.org/

Requires:   socat
BuildRequires:  systemd

%description
A simple Qubes RPC endpoint which implements an RPC endpoint serving a Dom0 shell.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build
make %{?_smp_mflags} all

%install
make install DESTDIR=%{buildroot}

%files
%doc README.md
%defattr(-,root,root,-)
%attr(0664,root,root) /etc/qubes-rpc/qubes.Dom0Shell
%attr(0664,root,qubes) %config{noreplace} /etc/qubes-rpc/policy/qubes.Dom0Shell

%package client
Summary:    Simple client for Qubes Dom0 Shell RPC service
Requires:   socat
BuildRequires:  systemd

%description client
A simple client script to invoke socat and the Qubes Dom0 Shell RPC endpoint service and drop a Dom0 shell.

%files client
%doc README.md
%defattr(-,root,qubes,-)
%attr(0775,root,qubes) /usr/local/bin/qubes-dom0-shell

%changelog

