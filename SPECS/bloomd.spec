%global _git_author armon
%global _git_commit 16a99fdfb80d2ee645166889e7bea124c72b8cd0

%global _bloomd_user  bloomd
%global _bloomd_group bloomd
%global _bloomd_home  /var/lib/bloomd

Name:           bloomd
Version:        0.7.5
Release:        1.perlover%{?dist}
Summary:        high-performance C server which is used to expose bloom filters and operations over them to networked clients
Vendor:         Perlover RPM

Group:          System Environment/Daemons
License:        BSD
URL:            https://github.com/%{_git_author}/%{name}
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  scons

%description
Bloomd is a high-performance C server which is used to expose bloom filters and
operations over them to networked clients. It uses a simple ASCI protocol which
is human readable, and similar to memcached.



%prep
%setup -q -n bloomd-%{version}


%build
scons


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sharedstatedir}/%{name}
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}.conf
install -D -m 0755 -s %{name} $RPM_BUILD_ROOT/%{_sbindir}/%{name}
install -D -m 0755 %{SOURCE2} $RPM_BUILD_ROOT/%{_initddir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%pre
getent group %{_bloomd_group} >/dev/null || groupadd -r %{_bloomd_group}
getent passwd %{_bloomd_user} >/dev/null || \
    useradd -r -g %{_bloomd_user} -d %{_bloomd_home} -s /sbin/nologin \
    -c "bloomd user" %{_bloomd_user}
exit 0


%post
/sbin/chkconfig --add %{name}


%preun
if [ $1 -eq 0 ] ; then
        /sbin/service %{name} stop >/dev/null 2>&1
        /sbin/chkconfig --del %{name}
fi


%postun
if [ "$1" -ge "1" ] ; then
        /sbin/service %{name} restart >/dev/null 2>&1
fi


%files
%defattr(-,root,root,-)
%doc LICENSE CHANGELOG.mdown README.md TODO.mdown
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0775,%{_bloomd_user},%{_bloomd_group}) %{_sharedstatedir}/%{name}
%{_sbindir}/%{name}
%{_initddir}/%{name}


%changelog
* Mon Mar 26 2018 Perlover <perlover@perlover.com> - 0.7.5-1.perlover
- Update for v0.7.5

* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-7.vortex
- Fix init-script.

* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-6.vortex
- Fix init-script.

* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-5.vortex
- Add bloomd homedir.

* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-4.vortex
- Add bloomd user and group.

* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-3.vortex
- Add post/pre actions.

* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-2.vortex
- Add init-script.

* Fri Feb 22 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.5.0-1.vortex
- Initial packaging.

