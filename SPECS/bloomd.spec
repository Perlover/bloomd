Name:           bloomd
Version:        0.5.0
Release:        1.vortex%{?dist}
Summary:        high-performance C server which is used to expose bloom filters and operations over them to networked clients

Group:          System Environment/Daemons
License:        BSD
URL:            https://github.com/armon/bloomd
Source0:        bloomd-0.5.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  scons
Requires:       

%description
Bloomd is a high-performance C server which is used to expose bloom filters and
operations over them to networked clients. It uses a simple ASCI protocol which
is human readable, and similar to memcached.



%prep
%setup -q -n bloomd-6dfd4b5ce672a0e92d66181a507e6f452ca1f5ab


%build
scons
ls -la
#%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog
* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-1.vortex
- Initial packaging.

