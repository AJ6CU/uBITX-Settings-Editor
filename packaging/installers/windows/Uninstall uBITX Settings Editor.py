"""
Removes uBITX Settings Editor installed by "Install uBITX Settings Editor.py".

Double-click it. Your backup and settings files are not touched. Close the
program first.
"""
import os
import shutil
import sys

APP = "uBITX Settings Editor"
HOME = os.path.join(os.environ.get("LOCALAPPDATA") or os.path.expanduser("~"), APP)


def folder(name, fallback):
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
        return os.path.expandvars(winreg.QueryValueEx(key, name)[0])
    except (ImportError, OSError):
        return fallback


programs = folder("Programs", os.path.join(os.environ.get("APPDATA", ""), "Microsoft",
                                          "Windows", "Start Menu", "Programs"))
desktop = folder("Desktop", os.path.join(os.path.expanduser("~"), "Desktop"))
problem = None
if os.path.isdir(HOME):
    try:
        shutil.rmtree(HOME)
    except OSError as err:
        problem = f"could not remove {HOME} ({err}) -- is the program still running?"
for path in (os.path.join(programs, f"{APP}.lnk"), os.path.join(desktop, f"{APP}.lnk"),
             os.path.join(desktop, f"{APP}.pyw")):
    try:
        os.remove(path)
    except OSError:
        pass

print()
if problem:
    print("NOT FULLY REMOVED: " + problem)
else:
    print(f"{APP} removed. Your backup and settings files are not touched.")
print()
try:
    input("Press Enter to close this window.")
except EOFError:
    pass
sys.exit(1 if problem else 0)
