Name:           scarlett2-firmware
Version:        2128b
Release:        1%{?dist}
Summary:        Firmware files for Focusrite Scarlett 2nd/3rd/4th Gen and Clarett USB interfaces

# Firmware is redistributable but with restrictions
License:        LicenseRef-Focusrite-Firmware
URL:            https://github.com/geoffreybennett/scarlett2-firmware
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make

# Required by alsa-scarlett-gui for firmware updates
Enhances:       alsa-scarlett-gui

%description
This package contains firmware files for Focusrite USB audio interfaces:

- Scarlett 2nd Gen: 6i6, 18i8, 18i20
- Scarlett 3rd Gen: Solo, 2i2, 4i4, 8i6, 18i8, 18i20
- Scarlett 4th Gen: Solo, 2i2, 4i4
- Clarett USB: 2Pre, 4Pre, 8Pre
- Clarett+: 2Pre, 4Pre, 8Pre
- Vocaster: One, Two

These firmware files are used by alsa-scarlett-gui to update device firmware
on Linux systems.


%prep
%autosetup


%build
# Nothing to build - firmware files only


%install
%make_install FWDIR=%{_prefix}/lib/firmware/scarlett2


%files
%license LICENSE.Focusrite
%doc README.md
%{_prefix}/lib/firmware/scarlett2/


%changelog
* Sat Jan 17 2026 Federico Manzella <ferdiu.manzella@gmail.com> - 2128b-1
- First package for version 2128b
