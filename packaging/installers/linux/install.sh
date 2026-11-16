#!/usr/bin/env bash
# Installs uBITX Settings Editor for this user, from the wheel next to this script.
#
#   bash install.sh          (or double-click it and choose "Run in Terminal")
#
# Puts the program in ~/.local/share/ubitx-settings-editor (its own Python
# environment -- nothing is installed into the system's Python), the command
# ~/.local/bin/ubitx-settings-editor, and an entry in the desktop's application
# menu. Run it again to upgrade or repair. Needs no root, except to add Python's
# Tk and venv packages or the serial-port group if they are missing, and then
# only after asking.
set -u

APP="uBITX Settings Editor"
HERE="$(cd "$(dirname "$0")" && pwd)"
HOME_DIR="$HOME/.local/share/ubitx-settings-editor"
VENV="$HOME_DIR/venv"
BIN="$HOME/.local/bin"
MENU="$HOME/.local/share/applications/ubitx-settings-editor.desktop"

say()  { printf '\n%s\n' "$*"; }
fail() { printf '\nNOT INSTALLED: %s\n' "$*" >&2; exit 1; }

# -- the wheel --------------------------------------------------------------
shopt -s nullglob
wheels=("$HERE"/ubitx_settings_editor-*.whl)
[ ${#wheels[@]} -eq 1 ] || fail "expected one ubitx_settings_editor-*.whl next to this script, found ${#wheels[@]}."
WHEEL="${wheels[0]}"
say "Installing $APP from $(basename "$WHEEL")"

# -- a Python that can run it ----------------------------------------------
# 3.10 or newer, with Tk (Python's window toolkit, which pip cannot install)
# and venv. Debian, Ubuntu and Raspberry Pi OS package both separately.
python_ok() {
    "$1" - <<'PY' 2>/dev/null
import sys, tkinter, ensurepip, venv
sys.exit(0 if sys.version_info >= (3, 10) else 1)
PY
}
PY=""
for cand in python3 python3.14 python3.13 python3.12 python3.11 python3.10; do
    p="$(command -v "$cand" 2>/dev/null)" || continue
    if python_ok "$p"; then PY="$p"; break; fi
done
if [ -z "$PY" ]; then
    if command -v apt-get >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1; then
        say "Python needs its Tk and venv packages (python3-tk, python3-venv)."
        read -r -p "Install them now with sudo apt? [Y/n] " ans || ans=n   # no keyboard: no
        case "${ans:-y}" in
            [Yy]*) sudo apt-get install -y python3-tk python3-venv || fail "apt could not install them." ;;
            *) fail "run: sudo apt install python3-tk python3-venv   then run this again." ;;
        esac
        python_ok "$(command -v python3)" && PY="$(command -v python3)"
    fi
fi
[ -n "$PY" ] || fail "no Python 3.10+ with Tk and venv found.
Install them with your package manager (Debian/Ubuntu/Pi: sudo apt install python3 python3-tk python3-venv), then run this again."
say "Using $PY ($("$PY" -c 'import sys; print(sys.version.split()[0])'))"

# -- its own environment ---------------------------------------------------
# Remade if the Python it was made from has gone (an OS upgrade).
if [ -x "$VENV/bin/python" ] && ! "$VENV/bin/python" -c "import sys" 2>/dev/null; then
    rm -rf "$VENV"
fi
if [ ! -x "$VENV/bin/python" ]; then
    mkdir -p "$HOME_DIR"
    "$PY" -m venv "$VENV" || fail "could not create $VENV"
fi
"$VENV/bin/python" -m pip install --quiet --upgrade pip || say "(pip itself could not be upgraded; carrying on)"
say "Installing the program and what it needs from PyPI -- a minute or two the first time"
"$VENV/bin/python" -m pip install --quiet --upgrade "$WHEEL" || fail "pip could not install it (see the message above; is the internet reachable?)"
# The same version again (a rebuilt wheel) is not picked up by --upgrade.
"$VENV/bin/python" -m pip install --quiet --force-reinstall --no-deps "$WHEEL" || fail "pip could not reinstall the wheel"

# -- how to start it ---------------------------------------------------------
mkdir -p "$BIN" "$(dirname "$MENU")"
PKG="$("$VENV/bin/python" -c 'import os, ubitx_settings_editor_app; print(os.path.dirname(ubitx_settings_editor_app.__file__))')"
ln -sf "$VENV/bin/ubitx-settings-editor" "$BIN/ubitx-settings-editor"
cat > "$MENU" <<DESKTOP
[Desktop Entry]
Type=Application
Name=$APP
Comment=Back up, edit and restore a uBITX's KD8CEC settings
Exec="$VENV/bin/ubitx-settings-editor"
Icon=$PKG/icon_256.png
Terminal=false
Categories=Network;HamRadio;
DESKTOP
command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$(dirname "$MENU")" >/dev/null 2>&1

# -- the radio's serial port -----------------------------------------------
# USB serial adapters are /dev/ttyUSB* or /dev/ttyACM*, group dialout.
NOTE=""
ME="$(id -un)"
if getent group dialout >/dev/null 2>&1 && ! id -nG "$ME" | tr ' ' '\n' | grep -qx dialout; then
    say "To open the radio's USB serial port, $ME must be in the 'dialout' group."
    read -r -p "Add $ME to dialout now with sudo? [Y/n] " ans || ans=n   # no keyboard: no
    LATER="Later: sudo usermod -aG dialout $ME   then log out and back in."
    case "${ans:-y}" in
        [Yy]*) if sudo usermod -aG dialout "$ME"; then
                   NOTE="Log out and back in (or reboot) once, so the new 'dialout' group takes effect."
               else
                   NOTE="Could not add $ME to dialout. $LATER"
               fi ;;
        *) NOTE="$LATER" ;;
    esac
fi

say "DONE. $APP is installed.
  Start it from the application menu (Internet / Ham Radio), or type: ubitx-settings-editor
  Program:  $HOME_DIR
  Your backup and settings files stay wherever you saved them."
case ":$PATH:" in *":$BIN:"*) ;; *) say "(~/.local/bin is not on your PATH yet; it usually is after logging in again.)";; esac
[ -n "$NOTE" ] && say "$NOTE"
exit 0
