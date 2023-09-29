import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_pulseStreamer import (Ui_MainWindow, DSequence)
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QSpinBox, QLineEdit)

from pulsestreamer import PulseStreamer
from pulsestreamer import findPulseStreamers
from pulsestreamer import TriggerStart, TriggerRearm
from pulsestreamer import Sequence, OutputState

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectSignalsAndSlots()
        self.pulser = None
        # connect button signals to slots
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.playButton.clicked.connect(self.play)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.logButton.clicked.connect(self.log)
        
    def search(self):
        print("search for pulse streamer device")
        devices = findPulseStreamers()
        if devices !=[]:
            print("Detected Pulse Streamer 8/2: ")
            print(devices)
            print("------------------------------------------------------\n")
            #Connect to the first discovered Pulse Streamer
            ip = devices[0][0]
            self.ui.IPLabel.setText(ip)
            print(ip)
        else:
            # if discovery failed try to connect by the default hostname
            # IP address of the pulse streamer (default hostname is 'pulsestreamer')
            print("No Pulse Streamer found")
            ip = 'pulsestreamer'
        
        #connect to the pulse streamer
        self.pulser = PulseStreamer(ip)

        # Print serial number and FPGA-ID
        if self.pulser:
            print('Serial: ' + self.pulser.getSerial())
            print('FPGA ID: ' + self.pulser.getFPGAID())
        pass
        
    # Slots
    def play(self):
        print("play called")
        
        # Compose sequence data
        seqCount = self.ui.DHL.count()
        signals = []
        scales = []
        dur = []
        
        d = {"ns": 1,
            "micro": 1e3,
            "ms": 1e6, 
            "s": 1e9}
        
        for i in range(1,seqCount-1):
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
        
        # set up and plot sequences data
        seq = Sequence()
        for c in range(8):
            s = []
            for i in range(seqCount-2):
                s.append((dur[i]*scales[i],signals[i][c]))
            seq.setDigital(c,s)
        
        seq.plot()
        
        # trigger pulser
        start = TriggerStart.IMMEDIATE
        rearm = TriggerRearm.MANUAL
        n_runs = self.ui.repeatBox.value()
        final = OutputState.ZERO()
        
        if self.pulser:
            self.pulser.reset()
            self.pulser.constant(OutputState.ZERO())
            self.pulser.setTrigger(start=start, rearm=rearm)
            self.pulser.stream(seq, n_runs, final)
            
        pass
    
    def cancel(self):
        print("cancel called")
        
        # Cancel execution 
        pass
    
    ### function for debug purposes
    def log(self):
        print("print state")
        print("IP address of pulser: " + str(self.pulser))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())