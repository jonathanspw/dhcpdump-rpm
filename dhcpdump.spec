Name:           dhcpdump
Version:        1.8
Release:        1%{?dist}
Summary:        Parse DHCP packets

License:        BSD
URL:            http://www.mavetju.org/unix/general.php
Source0:        http://www.mavetju.org/download/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl-podlators

%description
A utility to analyze sniffed DHCP packets.

%prep
%autosetup


%build
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
install -D -p -m 755 -t %{buildroot}%{_bindir} %{name}
install -D -p -m 644 -t %{buildroot}%{_mandir}/man8/ %{name}.8

%files
%license LICENSE
%doc CHANGES CONTACT
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Wed Jul 13 2022 Jonathan Wright <jonathan@almalinux.org> - 1.8-1
- Initial version of the package
