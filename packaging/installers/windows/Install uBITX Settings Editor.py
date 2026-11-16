"""
Installs uBITX Settings Editor for this user, from the wheel next to this file.

Double-click it (Python opens it). Needs Python 3.10 or newer from python.org,
and no administrator rights.

WHY PYTHON AND NOT A .BAT (Mark, on Windows 11, 2026-11-13): Smart App Control
blocks unsigned .bat and .ps1 files outright -- "Unblock" on the zip did not
help, only "Run as administrator" did -- and it stops PowerShell from making
shortcuts. A Python program run by Python (signed by the Python Software
Foundation) is not something it checks, and Python is needed anyway.

Puts the program in %LOCALAPPDATA%\\uBITX Settings Editor (its own Python
environment; nothing goes into Python itself) and a shortcut in the Start menu
and on the Desktop. Run it again to upgrade or repair. %LOCALAPPDATA% rather
than Documents: Documents is often synced by OneDrive, which copes badly with
thousands of small program files.
"""
import glob
import os
import shutil
import subprocess
import sys

APP = "uBITX Settings Editor"
HERE = os.path.dirname(os.path.abspath(__file__))
WINDOWS = os.name == "nt"
HOME = os.path.join(os.environ.get("LOCALAPPDATA") or os.path.expanduser("~"), APP)
VENV = os.path.join(HOME, "venv")
SCRIPTS = os.path.join(VENV, "Scripts" if WINDOWS else "bin")
VPY = os.path.join(SCRIPTS, "python.exe" if WINDOWS else "python")
VPYW = os.path.join(SCRIPTS, "pythonw.exe" if WINDOWS else "python")
# No console window for the programs this starts (pip and the like).
QUIET = {"creationflags": subprocess.CREATE_NO_WINDOW} if WINDOWS else {}


def say(text=""):
    print(text, flush=True)


def finish(code):
    say()
    try:
        input("Press Enter to close this window.")
    except EOFError:
        pass
    sys.exit(code)


def fail(text):
    say()
    say("NOT INSTALLED: " + text)
    finish(1)


def run(args, what):
    """Runs a step, its output shown; stops the install if it fails."""
    done = subprocess.run(args)
    if done.returncode != 0:
        fail(what)


def windows_folder(name, fallback):
    """A shell folder (Desktop may be on OneDrive), from the registry."""
    if WINDOWS:
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
            value, _ = winreg.QueryValueEx(key, name)
            return os.path.expandvars(value)
        except OSError:
            pass
    return fallback


def main():
    say(f"Installing {APP}")

    # -- the wheel -------------------------------------------------------------
    wheels = glob.glob(os.path.join(HERE, "ubitx_settings_editor-*.whl"))
    if not wheels:
        # Opened from inside the zip: Explorer shows a zip like a folder, but
        # double-clicking a file in it runs that one file from a temporary
        # folder, without the wheel beside it (Mark, on the X1).
        fail("the program file (ubitx_settings_editor-....whl) is not beside this installer.\n"
             "If you opened it from inside the downloaded zip: close this window,\n"
             "right-click the zip > Extract All..., open the extracted folder and\n"
             "double-click the installer there.")
    if len(wheels) > 1:
        fail(f"found {len(wheels)} ubitx_settings_editor-*.whl files beside this installer; keep one.")
    wheel = wheels[0]
    say(f"  from {os.path.basename(wheel)}")

    # -- the Python running this -----------------------------------------------
    if sys.version_info < (3, 10):
        fail(f"this is Python {sys.version.split()[0]}; 3.10 or newer is needed "
             f"(https://www.python.org/downloads/windows/).")
    try:
        import tkinter
        tkinter.Tcl()
    except Exception:
        fail("this Python has no Tk. Reinstall Python from python.org with "
             "'tcl/tk and IDLE' ticked, then run this again.")
    say(f"  using Python {sys.version.split()[0]} ({sys.executable})")

    # -- its own environment -----------------------------------------------------
    # Remade if the Python it was made from has gone (uninstalled or upgraded).
    if os.path.exists(VPY):
        ok = subprocess.run([VPY, "-c", "import sys"], capture_output=True, **QUIET).returncode == 0
        if not ok:
            shutil.rmtree(VENV, ignore_errors=True)
    if not os.path.exists(VPY):
        os.makedirs(HOME, exist_ok=True)
        say("  making its Python environment")
        run([sys.executable, "-m", "venv", VENV], f"could not create {VENV}")

    say("  installing the program and what it needs from PyPI -- a minute or two the first time")
    subprocess.run([VPY, "-m", "pip", "install", "--quiet", "--upgrade", "pip"])
    run([VPY, "-m", "pip", "install", "--quiet", "--upgrade", wheel],
        "pip could not install it (see above; is the internet reachable?)")
    # The same version again (a rebuilt wheel) is not picked up by --upgrade.
    run([VPY, "-m", "pip", "install", "--quiet", "--force-reinstall", "--no-deps", wheel],
        "pip could not reinstall the wheel")

    # -- how to start it ---------------------------------------------------------
    # The .bat the first version of this installer wrote: Smart App Control
    # blocks it, so it goes.
    try:
        os.remove(os.path.join(HOME, "Start with messages.bat"))
    except OSError:
        pass
    # For when something goes wrong: the app with its messages shown.
    with open(os.path.join(HOME, "Start with messages.py"), "w", encoding="utf-8") as f:
        f.write(f'"""Starts {APP} with its messages shown -- for when something goes wrong."""\n'
                "import subprocess\n"
                f"subprocess.run([{VPY!r}, '-m', 'ubitx_settings_editor_app'])\n"
                "input('Press Enter to close this window.')\n")

    if WINDOWS:
        make_shortcuts()

    say()
    say(f"DONE. {APP} is installed.")
    say("  Start it from the Start menu or the Desktop shortcut.")
    say(f"  Program:  {HOME}")
    say("  Your backup and settings files stay wherever you saved them.")
    say("  The radio's COM port: Device Manager > Ports (COM & LPT).")
    finish(0)


def make_shortcuts():
    """
    Start menu and Desktop shortcuts to pythonw (no console window).

    Written by pylnk3, a small pure-Python library for .lnk files, installed
    into the program's own environment: PowerShell's WScript.Shell, the usual
    way, is one of the things Smart App Control stops. Where a shortcut cannot
    be made, a launcher file goes on the Desktop instead -- double-clicking a
    .pyw starts the app the same way.
    """
    programs = os.path.join(windows_folder("Programs", os.path.join(
        os.environ.get("APPDATA", ""), "Microsoft", "Windows", "Start Menu", "Programs")))
    desktop = windows_folder("Desktop", os.path.join(os.path.expanduser("~"), "Desktop"))
    for place in (programs, desktop):
        os.makedirs(place, exist_ok=True)
    made = []
    if subprocess.run([VPY, "-m", "pip", "install", "--quiet", "pylnk3"]).returncode == 0:
        # The program's own icon, from the installed package.
        code = (
            "import os, sys, pylnk3, ubitx_settings_editor_app\n"
            "icon = os.path.join(os.path.dirname(ubitx_settings_editor_app.__file__), 'settingseditor.ico')\n"
            "for lnk in sys.argv[3:]:\n"
            "    pylnk3.for_file(sys.argv[1], lnk, arguments='-m ubitx_settings_editor_app',\n"
            "                    description='Back up, edit and restore the KD8CEC settings of a uBITX',\n"
            "                    work_dir=sys.argv[2],\n"
            "                    icon_file=icon if os.path.exists(icon) else None)\n")
        links = [os.path.join(programs, f"{APP}.lnk"), os.path.join(desktop, f"{APP}.lnk")]
        if subprocess.run([VPY, "-c", code, VPYW, os.path.expanduser("~")] + links,
                          **QUIET).returncode == 0:
            made = links
    if not made:
        launcher = os.path.join(desktop, f"{APP}.pyw")
        with open(launcher, "w", encoding="utf-8") as f:
            f.write(f'"""Starts {APP}."""\n'
                    "import subprocess\n"
                    f"subprocess.Popen([{VPYW!r}, '-m', 'ubitx_settings_editor_app'])\n")
        say(f"  (no shortcut could be made; a launcher is on the Desktop: {os.path.basename(launcher)})")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as err:  # said plainly, and the window stays open to read it
        fail(f"{type(err).__name__}: {err}")
