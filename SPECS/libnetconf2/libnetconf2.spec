Summary:        NETCONF library in C intended for building NETCONF clients and servers.
Name:           libnetconf2
Version:        2.1.7
Release:        1%{?dist}
License:        BSD-3-Clause
Group:          Development/Tools
URL:            https://github.com/CESNET/libnetconf2
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        https://github.com/CESNET/libnetconf2/archive/refs/tags/%{name}-%{version}.tar.gz
%define sha1 %{name}=bac66d22bc7928f5fbd77850775f79f73e4b18b8

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libssh-devel
BuildRequires:  openssl-devel
BuildRequires:  libyang-devel
BuildRequires:  pcre2-devel

Requires:  cmocka
Requires:  valgrind

%description
libnetconf2 is a NETCONF library in C intended for building NETCONF clients and
servers. NETCONF is the NETwork CONFiguration protocol introduced by IETF.

%package devel
Summary: Development libraries for libnetconf2

%description devel
Headers of libnetconf library.

%prep
%autosetup -p1

%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DCMAKE_BUILD_TYPE:String="Release" \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DENABLE_TESTS=ON \
    ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%check
make test %{?_smp_mflags}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE
%{_libdir}/%{name}.so.*
%exclude %dir %{_libdir}/debug

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*.h
%{_includedir}/%{name}/*.h
%dir %{_includedir}/%{name}

%changelog
*   Thu Mar 24 2022 Brennan Lamoreaux <blamoreaux@vmware.com> 2.1.7-1
-   Initial addition. Modified for photon.
*   Tue Oct 12 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.7-1
-   upstream package