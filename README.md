# Focusrite Scarlett RPM Spec Files

Fedora-compliant RPM spec files for:

- **alsa-scarlett-gui** - Gtk4 GUI for controlling Focusrite USB audio interfaces
- **scarlett2-firmware** - Firmware for Scarlett 2nd/3rd/4th Gen (small), Clarett, and Vocaster
- **scarlett4-firmware** - Firmware for Scarlett 4th Gen large interfaces (16i16, 18i16, 18i20)

## Building Locally

### alsa-scarlett-gui
```bash
# Install build dependencies
sudo dnf builddep alsa-scarlett-gui.spec

# Download source
spectool -g -R alsa-scarlett-gui.spec

# Build the RPM
rpmbuild -ba alsa-scarlett-gui.spec
```

### Firmware Packages
```bash
# For scarlett2-firmware
spectool -g -R scarlett2-firmware.spec
rpmbuild -ba scarlett2-firmware.spec

# For scarlett4-firmware
spectool -g -R scarlett4-firmware.spec
rpmbuild -ba scarlett4-firmware.spec
```

## Package Relationships

- `alsa-scarlett-gui` suggests both firmware packages for full functionality
- Firmware packages enhance `alsa-scarlett-gui` for device updates
- All packages can be installed independently

## Requirements

- Fedora 39+ or compatible RHEL-based distribution
- Kernel 5.4+ with Focusrite USB drivers enabled
- Supported Focusrite USB audio interface

## License

- alsa-scarlett-gui: GPL-3.0-or-later
- Firmware packages: Focusrite proprietary (redistributable with restrictions)