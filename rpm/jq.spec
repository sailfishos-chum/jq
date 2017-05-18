Summary: lightweight and flexible command-line JSON processor
Name: jq
Version: 1.5
Release: 1%{?dist}
License: MIT
Group: System/Utilities
URL: https://stedolan.github.io/jq/

Source: https://github.com/stedolan/jq/releases/download/jq-1.5/jq-1.5.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc

%description
jq is a lightweight and flexible command-line JSON processor.

%package devel
Summary: ZeroMQ development headers
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package provides headers for development

%prep
%setup

%build
%{__make} clean || true

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure --disable-static

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post

%files
%files
%defattr(-, root, root, 0755)
%{_bindir}/jq
%{_libdir}/libjq.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_libdir}/libjq.la
%{_mandir}/man1/*
%{_datadir}/doc/jq

%changelog
* Thu May 18 2017 rinigus <rinigus.git@gmail.com> - 1.5-1
- initial packaging release for SFOS
