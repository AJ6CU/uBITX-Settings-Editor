#!/usr/bin/env python3
"""
Builds the uBITX Settings Editor as a wheel, for the installers in
packaging/installers/ (and for anyone who prefers pip):

    python3 packaging/build_wheel.py

    dist/ubitx_settings_editor-<version>-py3-none-any.whl

The version is APPVERSION in uBITX_Settings_Editor/globalvars.py.

The program's files are copied, unchanged, into a package named
`ubitx_settings_editor_app`, with packaging/launcher.py as its __main__.py, so
it starts as

    ubitx-settings-editor            (the command pip makes)
    python -m ubitx_settings_editor_app

The program's modules import each other by plain name (`import globalvars`),
as they do when run from their own folder; the launcher puts the package's
folder on sys.path so that keeps working. Its data files (help, about, the
EEPROM map, the template, the images) are found beside the code through
globalvars.resource_path.

Needs `pip` and `build`'s backend, setuptools -- both come with a normal
Python's venv: python3 -m pip install --upgrade pip setuptools wheel
"""
import glob
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "uBITX_Settings_Editor")
BUILD = os.path.join(ROOT, "build", "wheel")
PKG = "ubitx_settings_editor_app"
DIST = os.path.join(ROOT, "dist")

# The program's own data, as the PyInstaller .spec files list it, plus the
# window icon and the icons the installers give the app.
DATA = [
    "help.xml", "about.xml", "eeprommemorymap.xml", "usermodfiletemplate.xml",
    "images/*.png", "settingseditor.gif", "settingseditor.ico", "settingseditor.icns",
]

REQUIRES = ["pyserial", "lxml", "bitarray", "pygubu", "Pillow"]

PYPROJECT = """\
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "ubitx-settings-editor"
version = "{version}"
description = "Back up, edit and restore the settings a uBITX running KD8CEC firmware keeps in EEPROM"
readme = "README.md"
requires-python = ">=3.10"
license = {{text = "GPL-3.0-or-later"}}
authors = [{{name = "Mark Hatch, AJ6CU"}}]
dependencies = {requires}

[project.urls]
Homepage = "https://github.com/AJ6CU/uBITX-Settings-Editor"

[project.scripts]
ubitx-settings-editor = "{pkg}.__main__:main"

[project.gui-scripts]
ubitx-settings-editor-gui = "{pkg}.__main__:main"

[tool.setuptools]
packages = ["{pkg}"]

[tool.setuptools.package-data]
{pkg} = {data}
"""


def version():
    with open(os.path.join(SRC, "globalvars.py"), encoding="utf-8") as f:
        m = re.search(r'^APPVERSION\s*=\s*["\']([^"\']+)', f.read(), re.M)
    if not m:
        sys.exit("no APPVERSION in uBITX_Settings_Editor/globalvars.py")
    return m.group(1)


def png_icon(dest):
    """A 256 px PNG of the window icon, for the Linux menu entry (which wants
    PNG or SVG). Pillow is one of the program's own requirements."""
    try:
        from PIL import Image
    except ImportError:
        print("  (Pillow not installed here: no icon_256.png; Linux uses the GIF)")
        return
    with Image.open(os.path.join(SRC, "settingseditor.gif")) as im:
        im.convert("RGBA").resize((256, 256), Image.LANCZOS).save(dest)


def main():
    ver = version()
    shutil.rmtree(BUILD, ignore_errors=True)
    pkg = os.path.join(BUILD, PKG)
    os.makedirs(pkg)

    # The code: every module beside the main program; the old experiments
    # and generated PyInstaller files are not part of it.
    for path in glob.glob(os.path.join(SRC, "*.py")):
        shutil.copy2(path, pkg)
    data = []
    for pattern in DATA:
        found = glob.glob(os.path.join(SRC, pattern))
        if not found:
            sys.exit(f"missing {pattern} in uBITX_Settings_Editor/")
        for path in found:
            # Kept in its folder (images/...), where resource_path looks.
            dest = os.path.join(pkg, os.path.relpath(path, SRC))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(path, dest)
        data.append(pattern)
    png_icon(os.path.join(pkg, "icon_256.png"))
    if os.path.exists(os.path.join(pkg, "icon_256.png")):
        data.append("icon_256.png")
    shutil.copy2(os.path.join(HERE, "launcher.py"), os.path.join(pkg, "__main__.py"))
    open(os.path.join(pkg, "__init__.py"), "w").close()

    shutil.copy2(os.path.join(ROOT, "README.md"), BUILD)
    with open(os.path.join(BUILD, "pyproject.toml"), "w", encoding="utf-8") as f:
        f.write(PYPROJECT.format(version=ver, pkg=PKG, requires=REQUIRES, data=data))

    os.makedirs(DIST, exist_ok=True)
    done = subprocess.run([sys.executable, "-m", "pip", "wheel", "--no-deps",
                           "--no-build-isolation", "-w", DIST, BUILD])
    if done.returncode != 0:
        sys.exit("the wheel was not built (see above). Is setuptools installed? "
                 "python3 -m pip install --upgrade setuptools wheel")
    print(f"\n  dist/ubitx_settings_editor-{ver}-py3-none-any.whl")


if __name__ == "__main__":
    main()
