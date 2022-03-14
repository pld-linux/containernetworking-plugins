Summary:	CNI network plugins
Name:		containernetworking-plugins
Version:	1.1.1
Release:	1
License:	Apache v2.0
Group:		Applications/System
#Source0Download: https://github.com/containers/podman/releases
Source0:	https://github.com/containernetworking/plugins/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c37fed40151ddf0a00ef265c9dd91742
URL:		https://github.com/containernetworking/plugins/
BuildRequires:	bash
BuildRequires:	golang
BuildRequires:	rpmbuild(macros) >= 2.009
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
The CNI (Container Network Interface) project consists of a
specification and libraries for writing plugins to configure network
interfaces in Linux containers, along with a number of supported
plugins. CNI concerns itself only with network connectivity of
containers and removing allocated resources when the container is
deleted.

%prep
%setup -q -n plugins-%{version}

%build
GO="eval %__go" %{__bash} ./build_linux.sh

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/cni/net.d
install -d $RPM_BUILD_ROOT%{_libexecdir}/cni
cp -p bin/* $RPM_BUILD_ROOT%{_libexecdir}/cni

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md OWNERS.md README.md
%dir %{_sysconfdir}/cni
%dir %{_sysconfdir}/cni/net.d
%dir %{_libexecdir}/cni
%attr(755,root,root) %{_libexecdir}/cni/*
