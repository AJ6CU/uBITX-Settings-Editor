#!/bin/zsh
# Installs uBITX Settings Editor for this user, from the wheel next to this script.
#
# Double-click it. If macOS says it cannot be opened (it is not signed): open
# Terminal, type  zsh  and a space, drag this file into the window, press Return.
#
# Puts the program in ~/Library/Application Support/uBITX Settings Editor (its own
# Python environment; nothing goes into Python itself) and the app
# "uBITX Settings Editor" in your Applications folder (~/Applications). Run it
# again to upgrade or repair. Needs no administrator password.
setopt nullglob
APP="uBITX Settings Editor"
HERE="${0:A:h}"
HOME_DIR="$HOME/Library/Application Support/$APP"
VENV="$HOME_DIR/venv"
BUNDLE="$HOME/Applications/$APP.app"

say()  { print; print -- "$*"; }
fail() { print; print -- "NOT INSTALLED: $*"; print; read -k1 "?Press a key to close."; exit 1; }

# -- the wheel --------------------------------------------------------------
wheels=("$HERE"/ubitx_settings_editor-*.whl)
(( ${#wheels} == 1 )) || fail "expected one ubitx_settings_editor-*.whl next to this script, found ${#wheels}."
WHEEL="${wheels[1]}"
say "Installing $APP from ${WHEEL:t}"

# -- a Python that can run it ----------------------------------------------
# 3.10 or newer with a working Tk. python.org's installer has Tk; Homebrew's
# Python needs "brew install python-tk@3.x" for it. Apple's own /usr/bin/python3
# (3.9) is too old. The newest that works is taken.
python_ok() { "$1" -c "import sys, tkinter, venv; tkinter.Tcl(); sys.exit(0 if sys.version_info >= (3, 10) else 1)" 2>/dev/null }
PY=""
for v in 3.14 3.13 3.12 3.11 3.10; do
    for p in "/Library/Frameworks/Python.framework/Versions/$v/bin/python$v" \
             "/opt/homebrew/bin/python$v" "/usr/local/bin/python$v"; do
        if [[ -x "$p" ]] && python_ok "$p"; then PY="$p"; break 2; fi
    done
done
if [[ -z "$PY" ]] && p="$(command -v python3)" && python_ok "$p"; then PY="$p"; fi
if [[ -z "$PY" ]]; then
    say "No Python 3.10 or newer with Tk was found.
Install Python from python.org (the page opens now) -- its installer includes Tk --
then run this again. (With Homebrew instead: brew install python@3.13 python-tk@3.13)"
    open "https://www.python.org/downloads/macos/"
    fail "Python with Tk needed."
fi
say "Using $PY ($("$PY" -c 'import sys; print(sys.version.split()[0])'))"

# -- its own environment ---------------------------------------------------
# Remade if the Python it was made from has gone (Python upgraded or removed).
if [[ -x "$VENV/bin/python" ]] && ! "$VENV/bin/python" -c "import sys" 2>/dev/null; then
    rm -rf "$VENV"
fi
if [[ ! -x "$VENV/bin/python" ]]; then
    mkdir -p "$HOME_DIR"
    "$PY" -m venv "$VENV" || fail "could not create $VENV"
fi
"$VENV/bin/python" -m pip install --quiet --upgrade pip || say "(pip itself could not be upgraded; carrying on)"
say "Installing the program and what it needs from PyPI -- a minute or two the first time"
"$VENV/bin/python" -m pip install --quiet --upgrade "$WHEEL" || fail "pip could not install it (see the message above; is the internet reachable?)"
# The same version again (a rebuilt wheel) is not picked up by --upgrade.
"$VENV/bin/python" -m pip install --quiet --force-reinstall --no-deps "$WHEEL" || fail "pip could not reinstall the wheel"

# -- how to start it: a small app in ~/Applications -------------------------
# Made here, on this Mac, so macOS does not treat it as downloaded. It starts
# the program and writes its messages to ~/Library/Logs/uBITX Settings Editor.log.
rm -rf "$BUNDLE"
# The architecture the environment's Python runs as here -- the one pip
# fetched the packages for (see the FIX at the start script below).
ARCH="$("$VENV/bin/python" -c 'import platform; print(platform.machine())')"
[[ "$ARCH" == "arm64" || "$ARCH" == "x86_64" ]] || ARCH="$(uname -m)"
mkdir -p "$BUNDLE/Contents/MacOS" "$BUNDLE/Contents/Resources"
# The program's own icon, from the installed package.
PKG="$("$VENV/bin/python" -c 'import os, ubitx_settings_editor_app; print(os.path.dirname(ubitx_settings_editor_app.__file__))')"
cp "$PKG/settingseditor.icns" "$BUNDLE/Contents/Resources/AppIcon.icns" 2>/dev/null
cat > "$BUNDLE/Contents/Info.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>CFBundleName</key><string>$APP</string>
  <key>CFBundleDisplayName</key><string>$APP</string>
  <key>CFBundleIdentifier</key><string>net.aj6cu.ubitx-settings-editor</string>
  <key>CFBundleExecutable</key><string>start</string>
  <key>CFBundleIconFile</key><string>AppIcon</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>NSHighResolutionCapable</key><true/>
  <key>LSArchitecturePriority</key><array><string>$ARCH</string></array>
</dict></plist>
PLIST
# FIX (2026-11-14): RUN PYTHON AS THE ARCHITECTURE IT WAS INSTALLED FOR.
# Mark's MacBook (Apple silicon): the app opened and closed at once, the log
# saying Pillow's library "is an incompatible architecture (have 'arm64',
# need 'x86_64')". python.org's Python is universal -- it runs as Apple
# silicon or as Intel (Rosetta), whichever its starter is -- and pip fetched
# the Apple-silicon packages while installing, but the app's start script
# was being run as Intel, so Python came up as Intel and could not load
# them. Now the start script asks for the architecture the packages were
# installed for, and the app says so to macOS (LSArchitecturePriority).
cat > "$BUNDLE/Contents/MacOS/start" <<START
#!/bin/zsh
exec /usr/bin/arch -$ARCH "$VENV/bin/python" -m ubitx_settings_editor_app >> "\$HOME/Library/Logs/$APP.log" 2>&1
START
chmod +x "$BUNDLE/Contents/MacOS/start"
touch "$BUNDLE"     # so Finder shows the new icon rather than a cached one

say "DONE. $APP is installed.
  Start it from Applications (in your home folder), Launchpad or Spotlight.
  Program:  $HOME_DIR
  Messages: ~/Library/Logs/$APP.log
  Your backup and settings files stay wherever you saved them."
print; read -k1 "?Press a key to close."
exit 0
