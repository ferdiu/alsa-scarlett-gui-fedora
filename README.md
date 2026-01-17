# alsa-scarlett-gui RPM Spec File

Fedora-compliant RPM spec file for building [alsa-scarlett-gui](https://github.com/geoffreybennett/alsa-scarlett-gui) - a Gtk4 GUI for controlling Focusrite Scarlett, Clarett, and Vocaster USB audio interfaces on Linux.

## Building Locally

```bash
# Install build dependencies
sudo dnf builddep alsa-scarlett-gui.spec

# Download source
spectool -g -R alsa-scarlett-gui.spec

# Build the RPM
rpmbuild -ba alsa-scarlett-gui.spec
```

## Requirements

- Fedora 39+ or compatible RHEL-based distribution
- Kernel 5.4+ with Focusrite USB drivers enabled
- Supported Focusrite USB audio interface

## License

The spec file follows the same license as the upstream project: GPL-3.0-or-later