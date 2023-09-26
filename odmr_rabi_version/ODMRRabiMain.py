import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_odmrEtRabi import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        # set up UI
        self.ui.setupUi(self)
        
        # Connect UI element to function trigger
        self.ui.addDChannelBut.clicked.connect(self.addDSequence)
        self.ui.searchPSButton.clicked.connect(self.searchPulseStreamer)
        self.ui.searchRSButton.clicked.connect(self.searchRSGenerator)
        self.ui.playButton.clicked.connect(self.play)
        self.ui.loadButton.clicked.connect(self.load)
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.addASequenceButton.clicked.connect(self.addASequence)
        self.ui.logStateButton.clicked.connect(self.log)
        
    def searchPulseStreamer(self):
        print("search Pulstreamer")
        pass
    
    def searchRSGenerator(self):
        print("Search RS generator")
        pass
        
    def load(self):
        print("Load")
        pass
        
    def play(self):
        print("Play")
        pass
    
    def cancel(self):
        print("Cancel")
        pass
        
    def addDSequence(self):
        if self.ui.DTabWidget.currentIndex():
            self.ui.odmrScrollArea.addSequence()
        else: 
            self.ui.rabiScrollArea.addSequence()
    
    def addASequence(self):
        self.ui.AArea.addASequence()
        pass

    def log(self):
        print("Log Info")
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())