
from scannerwidget import ScannerWidget

class Scanner (ScannerWidget):
    def log_msg(self, txBox, msg:str):
        txBox.config(state="normal")
        txBox.insert("end", msg + "\n")
        txBox.config(state="disabled")
        txBox.see("end")