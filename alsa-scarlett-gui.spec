Name:           alsa-scarlett-gui
Version:        0.5.1
Release:        1%{?dist}
Summary:        Gtk4 GUI for ALSA controls on Focusrite Scarlett/Clarett/Vocaster interfaces

License:        GPLv3+ LGPLv3+
URL:            https://github.com/geoffreybennett/alsa-scarlett-gui
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  desktop-file-utils

Requires:       gtk4
Requires:       hicolor-icon-theme
Requires:       alsa-lib
Requires:       openssl-libs

# Kernel driver requirements (informational)
Recommends:     (kernel >= 5.4 if kernel)
# Firmware packages (optional but recommended)
Suggests:       scarlett2-firmware
Suggests:       scarlett4-firmware

%description
alsa-scarlett-gui is a Gtk4 GUI for the ALSA controls presented by the Linux
kernel Focusrite USB drivers (Scarlett 1st/2nd/3rd/4th Gen, Clarett USB,
Clarett+, and Vocaster).

The Focusrite USB audio interfaces are class compliant, working out of the box
on Linux. However, the larger models have proprietary functionality requiring
specific kernel drivers. This application provides a user-friendly interface
for controlling mixer settings, routing, phantom power, Air mode, and other
advanced features.

Supported devices include:
- Scarlett 1st Gen: 6i6, 8i6, 18i6, 18i8, 18i20
- Scarlett 2nd Gen: 6i6, 18i8, 18i20
- Scarlett 3rd Gen: Solo, 2i2, 4i4, 8i6, 18i8, 18i20
- Scarlett 4th Gen: Solo, 2i2, 4i4, 16i16, 18i16, 18i20
- Clarett USB: 2Pre, 4Pre, 8Pre
- Clarett+: 2Pre, 4Pre, 8Pre
- Vocaster: One, Two


%prep
%autosetup -p1


%build
# Build in src directory as per upstream instructions
cd src
%set_build_flags
%make_build VERSION=%{version} PREFIX=%{_prefix}


%install
cd src
%make_install \
    PREFIX=%{_prefix}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/vu.b4.alsa-scarlett-gui.desktop


%files
%license LICENSES/GPL-3.0-or-later.txt
%license LICENSES/LGPL-3.0-or-later.txt
%doc README.md FAQ.md
%doc docs/INSTALL.md docs/USAGE.md
%doc docs/iface-*.md
%{_bindir}/alsa-scarlett-gui
%{_datadir}/applications/vu.b4.alsa-scarlett-gui.desktop
%{_datadir}/icons/hicolor/*/apps/vu.b4.alsa-scarlett-gui.*


%changelog
* Sat Jan 17 2026 Federico Manzella <ferdiu.manzella@gmail.com> - 0.5.1-1
- First package for version 0.5.1
