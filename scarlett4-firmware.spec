Name:           scarlett4-firmware
Version:        2403
Release:        1%{?dist}
Summary:        Firmware files for Focusrite Scarlett 4th Gen large interfaces

# Firmware is redistributable but with restrictions
License:        LicenseRef-Focusrite-Firmware
URL:            https://github.com/geoffreybennett/scarlett4-firmware
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# Required by fcp-support package
Enhances:       fcp-support

%description
This package contains firmware files for Focusrite Scarlett 4th Generation
large USB audio interfaces:

- Scarlett 4th Gen 16i16
- Scarlett 4th Gen 18i16
- Scarlett 4th Gen 18i20

These firmware files are tested with Linux and used by the FCP Support package
for firmware updates on these devices.


%prep
%autosetup


%build
# Nothing to build - firmware files only


%install
%make_install FWDIR=%{_prefix}/lib/firmware/scarlett4


%files
%license LICENSE.Focusrite
%doc README.md
%{_prefix}/lib/firmware/scarlett4/


%changelog
* Sat Jan 17 2026 Federico Manzella <ferdiu.manzella@gmail.com> - 2403-1
- First package for version 2403
