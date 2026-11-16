#!/usr/bin/env python3
"""
Makes the three download bundles from the wheel build_wheel.py made:

    python3 packaging/build_bundles.py

    dist/uBITX-Settings-Editor-<version>-Windows.zip
    dist/uBITX-Settings-Editor-<version>-macOS.zip
    dist/uBITX-Settings-Editor-<version>-Linux.tar.gz

Each holds one folder: the wheel, that platform's installer and uninstaller
(from packaging/installers/), and a READ ME. The installers find the wheel by
its name pattern, so no version is written into them -- a new release is
build_wheel.py, then this.

Run build_wheel.py first; this stops if dist/ has no wheel for the version in
globalvars.APPVERSION.
"""
import io
import os
import re
import sys
import tarfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIST = os.path.join(ROOT, "dist")
INSTALLERS = os.path.join(HERE, "installers")

README = {
    "Windows": """\
uBITX Settings Editor {version} for Windows
==========================================

1. Install Python from https://www.python.org/downloads/windows/ if you do not
   have it (3.10 or newer). In its installer keep "tcl/tk and IDLE" ticked.
2. Right-click the downloaded zip > Extract All... (double-clicking the
   installer inside the zip without extracting it does not work). The
   extracted folder is not needed after installing.
3. In the extracted folder, double-click "Install uBITX Settings Editor.py".
   Python runs it, in a window that shows its progress. If Windows asks which program should open it,
   choose Python. It does not need "Run as administrator".
4. Start the program from the Start menu or the Desktop shortcut.

The installer is a Python file rather than a .bat because Windows 11's Smart
App Control blocks unsigned .bat files.

To upgrade: run the installer from a newer version's folder.
To remove: "Uninstall uBITX Settings Editor.py". Your backup and settings files
are not touched.
If the program does not start: "Start with messages.py" in
%LOCALAPPDATA%\\uBITX Settings Editor shows what went wrong.
""",
    "macOS": """\
uBITX Settings Editor {version} for macOS
========================================

1. Install Python from https://www.python.org/downloads/macos/ if you do not
   have it (3.10 or newer; python.org's installer includes Tk).
2. Double-click "Install uBITX Settings Editor.command".
   The first time, macOS refuses ("Not Opened -- Apple could not verify..."),
   because the script is not signed. Click Done, then:
     System Settings > Privacy & Security, scroll down to Security, click
     "Open Anyway" next to "Install uBITX Settings Editor.command", confirm,
     and double-click the installer again.
   (Or: open Terminal, type  zsh  and a space, drag the .command file into the
   window, and press Return.)
3. Start the program from Applications (in your home folder), Launchpad or
   Spotlight: "uBITX Settings Editor". It opens without any warning: the
   installer makes it on your Mac.

To upgrade: run the installer from a newer version's folder.
To remove: "Uninstall uBITX Settings Editor.command". Your backup and settings
files are not touched.
The program's messages: ~/Library/Logs/uBITX Settings Editor.log
""",
    "Linux": """\
uBITX Settings Editor {version} for Linux (and Raspberry Pi OS)
==============================================================

1. Unpack this folder:   tar xzf uBITX-Settings-Editor-{version}-Linux.tar.gz
2. Run the installer:    bash uBITX-Settings-Editor-{version}/install.sh
   It checks for Python's Tk and venv packages and the 'dialout' group for
   the radio's serial port, and offers to add what is missing (with sudo).
3. Start the program from the application menu (Internet / Ham Radio), or
   type:  ubitx-settings-editor

To upgrade: run install.sh from a newer version's folder.
To remove: bash uninstall.sh. Your backup and settings files are not touched.
""",
}

FILES = {
    "Windows": ["Install uBITX Settings Editor.py", "Uninstall uBITX Settings Editor.py"],
    "macOS": ["Install uBITX Settings Editor.command",
              "Uninstall uBITX Settings Editor.command"],
    "Linux": ["install.sh", "uninstall.sh"],
}
SOURCE = {"Windows": "windows", "macOS": "macos", "Linux": "linux"}


def version():
    with open(os.path.join(ROOT, "uBITX_Settings_Editor", "globalvars.py"), encoding="utf-8") as f:
        m = re.search(r'^APPVERSION\s*=\s*["\']([^"\']+)', f.read(), re.M)
    if not m:
        sys.exit("no APPVERSION in uBITX_Settings_Editor/globalvars.py")
    return m.group(1)


def entries(platform, ver, wheel):
    """(name in the archive, bytes, executable) for one platform's folder."""
    top = f"uBITX-Settings-Editor-{ver}"
    out = [(f"{top}/{os.path.basename(wheel)}", open(wheel, "rb").read(), False)]
    for name in FILES[platform]:
        with open(os.path.join(INSTALLERS, SOURCE[platform], name), "rb") as f:
            data = f.read()
        if platform == "Windows" and name.endswith(".bat"):
            data = data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
        out.append((f"{top}/{name}", data, name.endswith((".sh", ".command"))))
    text = README[platform].format(version=ver)
    if platform == "Windows":
        text = text.replace("\n", "\r\n")
    out.append((f"{top}/READ ME.txt", text.encode(), False))
    return out


def write_zip(path, items):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data, exe in items:
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3                      # unix, so the mode is used
            info.external_attr = (0o100755 if exe else 0o100644) << 16
            z.writestr(info, data)


def write_tgz(path, items):
    with tarfile.open(path, "w:gz") as t:
        for name, data, exe in items:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.mode = 0o755 if exe else 0o644
            info.mtime = 0
            t.addfile(info, io.BytesIO(data))


def main():
    ver = version()
    wheel = os.path.join(DIST, f"ubitx_settings_editor-{ver}-py3-none-any.whl")
    if not os.path.exists(wheel):
        sys.exit(f"no {os.path.relpath(wheel, ROOT)} -- run packaging/build_wheel.py first")
    for platform in ("Windows", "macOS", "Linux"):
        items = entries(platform, ver, wheel)
        if platform == "Linux":
            out = os.path.join(DIST, f"uBITX-Settings-Editor-{ver}-Linux.tar.gz")
            write_tgz(out, items)
        else:
            out = os.path.join(DIST, f"uBITX-Settings-Editor-{ver}-{platform}.zip")
            write_zip(out, items)
        print(f"  {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
