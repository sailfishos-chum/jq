Summary: lightweight and flexible command-line JSON processor
Name: jq
Version: 1.6
Release: 2%{?dist}
License: MIT
Group: System/Utilities
URL: https://stedolan.github.io/jq/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Patch0:     jq-1.6-r3-never-bundle-oniguruma.patch
Patch1:     jq-1.6-runpath.patch
Patch2:     jq-1.6-segfault-fix.patch
Patch3:     jq-1.6-warnings.patch
BuildRequires: gcc flex bison libtool autoconf
BuildRequires: pkgconfig(oniguruma)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
jq is a lightweight and flexible command-line JSON processor.

%package devel
Summary: JQ development headers
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package provides headers for development


%prep
%setup -q -n %{name}-%{version}/jq

# jq-1.6-r3-never-bundle-oniguruma.patch
%patch0 -p1
# jq-1.6-runpath.patch
%patch1 -p1
# jq-1.6-segfault-fix.patch
%patch2 -p1
# jq-1.6-warnings.patch
%patch3 -p1

%build
CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"

autoreconf -fi

%configure --disable-static \
    --enable-silent-rules \
    --disable-maintainer-mode \
    --enable-devel \
    --disable-valgrind \
    --disable-docs

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%%{__make} install DESTDIR=%%{buildroot}
%make_install

rm -f %{buildroot}%{_docdir}/%{name}/README
rm -f %{buildroot}%{_docdir}/%{name}/COPYING
rm -f %{buildroot}%{_docdir}/%{name}/AUTHORS
rm -rf %{buildroot}%{_mandir}

%post -n jq -p /sbin/ldconfig

%postun -n jq -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%license COPYING
%{_docdir}/%{name}/README.md
%{_bindir}/jq
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/lib*.so
#%%{_libdir}/*.la
#%%{_mandir}/man1/*
#%%{_datadir}/doc/jq

%changelog
* Mon Nov 22 2021 nephros <sailfish@nephros.org> - 1.6-2
- disable static build - remove libs

* Mon Nov 22 2021 nephros <sailfish@nephros.org> - 1.6-1
- version bump
- do not use packaged oniguruma library

* Thu May 18 2017 rinigus <rinigus.git@gmail.com> - 1.5-1
- initial packaging release for SFOS
