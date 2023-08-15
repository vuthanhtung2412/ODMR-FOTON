import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_pulseStreamer import (Ui_MainWindow, DSequence)
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QSpinBox, QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectSignalsAndSlots()
        # connect button signals to slots
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.playButton.clicked.connect(self.play)
        
    # Slots
    def play(self):
        print("play called")
        
        # Compose sequence data
        signals = []
        scales = []
        dur = []
        
        d = {"ns": 1e-9,
            "micro": 1e-6,
            "ms": 1e-3, 
            "s": 1}
        
        for i in range(1,self.ui.DHL.count()-1):
            tmp = []
            o = self.ui.DHL.itemAt(i)
            if isinstance(o, DSequence):    
                for b in o.binButtons:
                    tmp.append(b.isChecked())
                signals.append(tmp)
                
                scales.append(d[str(o.comboBox.currentText())])
                dur.append(str(o.duration.value()))
        
        for s in signals:
            print(s)
        print(scales)
        print(dur)
        
        # Load seq data to pulse streamer
        pass
    
    def cancel(self):
        print("cancel called")
        
        # Cancel execution 
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())