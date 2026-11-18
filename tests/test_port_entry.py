"""
The port list: USB adapters first, and a port typed in by hand is used.

    python3 tests/test_port_entry.py

Found 2026-11-19 (PA1CJT, Ubuntu 26.04): /dev/ttyUSB0 existed and could be
opened, yet was not offered in the list, so there was no way to choose it.
Runs without Tk: the widget is replaced by stand-ins.
"""
import os, sys, types

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "uBITX_Settings_Editor")
sys.path.insert(0, SRC)

# Stand-ins for what com_portManager imports.
class Var:
    def __init__(self, v=""): self.v = v
    def get(self): return self.v
    def set(self, v): self.v = v

class Combo:
    def __init__(self): self.values = None
    def configure(self, **kw):
        if "values" in kw: self.values = list(kw["values"])

class Widget:
    def __init__(self, parent):
        self.availableComPorts = Var("Select Serial Port")
        self.comPortsOptionMenu = Combo()
        self.comPortListRefresh = types.SimpleNamespace(configure=lambda **k: None)

PORTS = []
serial = types.ModuleType("serial"); serial.PARITY_NONE = "N"
serial.tools = types.ModuleType("serial.tools")
serial.tools.list_ports = types.ModuleType("serial.tools.list_ports")
def _port(d):
    if isinstance(d, tuple):                      # (device, description, hwid)
        return types.SimpleNamespace(device=d[0], description=d[1], hwid=d[2])
    return types.SimpleNamespace(device=d, description="USB Serial", hwid="USB VID:PID=1A86:7523")
serial.tools.list_ports.comports = lambda: [_port(d) for d in PORTS]
stub = lambda name, **attrs: sys.modules.setdefault(name, types.SimpleNamespace(**attrs))
sys.modules.update({"serial": serial, "serial.tools": serial.tools,
                    "serial.tools.list_ports": serial.tools.list_ports})
stub("tkinter", messagebox=None); stub("tkinter.messagebox")
stub("PIL", Image=types.SimpleNamespace(open=lambda p: None),
     ImageTk=types.SimpleNamespace(PhotoImage=lambda i: None))
stub("PIL.Image"); stub("PIL.ImageTk")
sys.modules["comportmanagerwidget"] = types.SimpleNamespace(ComPortmanagerWidget=Widget)
sys.modules["globalvars"] = types.SimpleNamespace(RELOADICON="", BAUD=38400, __all__=["RELOADICON", "BAUD"])

import com_portManager as cpm

out = []
def case(name, ok):
    out.append(("PASS  " if ok else "FAIL  ") + name)

def manager():
    cpm.com_portManager.last_com_port_selected = "INVALID"
    states = []
    m = cpm.com_portManager(None, states.append)
    return m, states

PORTS[:] = ["/dev/ttyS4", "/dev/ttyUSB0", "/dev/ttyS0"]
m, states = manager()
case("every port pyserial finds is offered, USB adapters first",
     m.comPortsOptionMenu.values == ["/dev/ttyUSB0", "/dev/ttyS0", "/dev/ttyS4"])
case("nothing chosen yet: the buttons are off", states[-1] == "disabled")

# Kees's Ubuntu 26.04: 32 ttyS slots, only ttyS4 real, ttyUSB0 last.
PORTS[:] = ([("/dev/ttyS%d" % i, "n/a", "n/a") for i in range(32) if i != 4]
            + [("/dev/ttyS4", "ttyS4", "PNP0501"), "/dev/ttyUSB0"])
m, states = manager()
case("Ubuntu 26.04's empty ttyS slots are left out; ttyUSB0 is first",
     m.comPortsOptionMenu.values == ["/dev/ttyUSB0", "/dev/ttyS4"])

PORTS[:] = ["/dev/ttyS4"]                         # pyserial misses ttyUSB0
m, states = manager()
m.availableComPorts.set("/dev/ttyUSB0"); m.comPortTyped()
case("a port typed in is chosen and turns the buttons on",
     states[-1] == "normal" and m.getSelectedComPort() == "/dev/ttyUSB0")
m.updateComPorts()
case("... and survives a refresh that still does not list it",
     m.getSelectedComPort() == "/dev/ttyUSB0" and states[-1] == "normal")

m.availableComPorts.set("COM7 "); m.comPortTyped()
case("a Windows COM name counts, spaces trimmed", m.getSelectedComPort() == "COM7" and states[-1] == "normal")
m.availableComPorts.set("hello"); m.comPortTyped()
case("anything else turns the buttons off", states[-1] == "disabled")

print("\n".join(out))
print(f"\n{sum(l.startswith('PASS') for l in out)}/{len(out)} passed")
sys.exit(0 if all(l.startswith("PASS") for l in out) else 1)
