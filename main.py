import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_pulseStreamer import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QSpinBox, QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # connect button signals to slots
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.playButton.clicked.connect(self.play)
        
    # Slots
    def play(self):
        pass
    
    def cancel(self):
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())