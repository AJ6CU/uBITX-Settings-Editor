"""
Starts the uBITX Settings Editor from its installed package.

build_wheel.py copies this in as the package's __main__.py. The program's
modules import each other by plain name, as they do when run from their own
folder, so that folder goes on sys.path first; then the main program runs
as if started with `python uBITX_Settings_Editor.py`.
"""
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    try:
        import tkinter
        tkinter.Tcl()
    except Exception as err:
        # pip cannot install Tk: it comes with Python, or as a separate package.
        sys.exit("The uBITX Settings Editor needs Python's Tk, which this Python does not have "
                 f"({err}).\n"
                 "  macOS with Homebrew:  brew install python-tk@3.x  (your Python's version)\n"
                 "  Debian/Ubuntu/Pi:     sudo apt install python3-tk\n"
                 "  python.org Python includes it.")
    if sys.platform == "win32":
        # Its own taskbar identity, so Windows shows the program's icon there
        # and not pythonw's (as uBITX CEC Desktop does).
        try:
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("AJ6CU.uBITXSettingsEditor")
        except Exception:
            pass
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    runpy.run_path(os.path.join(HERE, "uBITX_Settings_Editor.py"), run_name="__main__")


if __name__ == "__main__":
    main()
