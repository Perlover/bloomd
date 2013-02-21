%global _git_author armon
%global _git_commit 6dfd4b5ce672a0e92d66181a507e6f452ca1f5ab

Name:           bloomd
Version:        0.5.0
Release:        1.vortex%{?dist}
Summary:        high-performance C server which is used to expose bloom filters and operations over them to networked clients
Vendor:         Vortex RPM

Group:          System Environment/Daemons
License:        BSD
URL:            https://github.com/%{_git_author}/%{name}
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  scons

%description
Bloomd is a high-performance C server which is used to expose bloom filters and
operations over them to networked clients. It uses a simple ASCI protocol which
is human readable, and similar to memcached.



%prep
%setup -q -n bloomd-%{_git_commit}


%build
scons


%install
rm -rf $RPM_BUILD_ROOT
cp %{SOURCE1} $RPM_BUILD_ROOT
install -D -m 0755 -s %{name} $RPM_BUILD_ROOT/%{_sbindir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sharedstatedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE CHANGELOG.mdown README.rst TODO.mdown
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sharedstatedir}/%{name}
%{_sbindir}/%{name}


%changelog
* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-1.vortex
- Initial packaging.

