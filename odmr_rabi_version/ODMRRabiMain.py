import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_odmrEtRabi import Ui_MainWindow

# Pulser dependencies
from pulsestreamer import PulseStreamer
from pulsestreamer import findPulseStreamers
from pulsestreamer import TriggerStart, TriggerRearm
from pulsestreamer import Sequence, OutputState

# R&S dependencies
from RsSmbv import *

# other dependencies
from odmr_rabi_elements.DSequence import DSequence

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
        
        # State information
        self.power = 0
        self.freq = 0
        self.freqList = []
        self.variedDurList = []
        self.signals = []
        self.dur= []
        self.scales = []
        self.varied = []
        self.timeScaleDict = {"ns": 1,
            "micro": 1e3,
            "ms": 1e6, 
            "s": 1e9}
        self.freqScaleDict = {"Hz" : 1,
            "KHz" : 1e3,
            "MHz": 1e6,
            "GHz" : 1e9, 
        }
        
        # machine 
        self.pulser = None 
        self.generator = None 
        
    def searchPulseStreamer(self):
        print("search Pulstreamer")
        devices = findPulseStreamers()
        ip = ""
        if devices !=[]:
            print("Detected Pulse Streamer 8/2: ")
            print(devices)
            print("------------------------------------------------------\n")
            #Connect to the first discovered Pulse Streamer
            ip = devices[0][0]
            self.ui.PSaddress.setText(ip)
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
    
    def searchRSGenerator(self):
        print("Search RS generator")
        instr_list = RsSmbv.list_resources("?*")
        print(instr_list)
        if instr_list:
            self.ui.RSaddress.setText(instr_list[0])
        pass
        
    def load(self):
        print("Load")
        
        # clear information of previous experiments
        self.power = 0
        self.freq = 0
        self.freqList.clear()
        self.variedDurList.clear()
        self.signals.clear()
        self.dur.clear()
        self.scales.clear()
        self.varied.clear()
        self.seq = Sequence()
        
        # ODMR experiment
        if self.ui.DTabWidget.currentIndex():
            print("ODMR experiment")
            self.odmrLoad()       
        # Rabi experiment
        else : 
            print("Rabi experiment")
            self.rabiLoad()
    
    def odmrLoad(self):
        exp = self.ui.odmrScrollArea.DHLayout
           
        # Load freq list
        startDur = self.ui.odmrStartFreqVal.value() * self.freqScaleDict[self.ui.odmrStartFreqScale.currentText()]
        endDur = self.ui.odmrEndFreqVal.value() * self.freqScaleDict[self.ui.odmrEndFreqScale.currentText()]
        if endDur < startDur:
            raise Exception("start duration must be smaller than end duration")
        
        nbStep = self.ui.odmrStepVal.value()
        self.freqList = [startDur + (endDur - startDur)/nbStep * i for i in range(nbStep+1)]
        
        # load power
        self.power = self.ui.odmrPowerVal.value()
        
        # load scale and duration
        for i in range(1,exp.count()-1): 
            o = exp.itemAt(i)
            if isinstance(o, DSequence):    
                self.scales.append(str(o.scaleComboBox.currentText()))
                self.dur.append(int(o.duration.value()))
        
        # load signals
        for i in range(8):
            tmp = []
            for j in range(1,exp.count()-1):
                o = exp.itemAt(j)
                if isinstance(o, DSequence):
                    tmp.append(int(o.buttons[i].isChecked()))
            self.signals.append(tmp)
        
        # Load sequence into Pulse Streamer
        self.seq = Sequence()
        for c in range(8):
            s = []
            for i in range(len(self.dur)):
                s.append((self.dur[i]*self.timeScaleDict[self.scales[i]], self.signals[c][i]))
            self.seq.setDigital(c,s)
        
        self.seq.plot()
        
        # Load frequency list into generator 
        
        # Load Power 
    
    def rabiLoad(self):
        exp = self.ui.rabiScrollArea.DHLayout

        # Load time range 
        startFreq = self.ui.rabiStartTimeVal.value() * self.timeScaleDict[self.ui.rabiStartTimeScale.currentText()]
        endFreq = self.ui.rabiEndTimeVal.value() * self.timeScaleDict[self.ui.rabiEndTimeScale.currentText()]
        if endFreq < startFreq:
            raise Exception("start frequency must be smaller than end frequency")
        
        nbStep = self.ui.odmrStepVal.value()
        self.variedDurList = [startFreq + (endFreq - startFreq)/nbStep * i for i in range(nbStep+1)]
        
        # Load freq, Power
        self.freq = self.ui.RabiFreqVal.value() * self.freqScaleDict[self.ui.RabiFreqScale.currentText()]
        self.power = self.ui.odmrPowerVal.value() 
        
        # Load signals 
        for i in range(8):
            tmp = []
            for j in range(1,exp.count()-1):
                o = exp.itemAt(j)
                if isinstance(o, DSequence):
                    tmp.append(int(o.buttons[i].isChecked()))
            self.signals.append(tmp)
        
        for i in range(1,exp.count()-1): 
            o = exp.itemAt(i)
            if isinstance(o, DSequence):
                self.varied.append(o.variCheckBox.isChecked())    
                self.scales.append(str(o.scaleComboBox.currentText()))
                self.dur.append(int(o.duration.value())) 
        
        # Load pulse sequence into Pulse Streamer
        self.seq = Sequence()
        for c in range(8):
            s = []
            for t in self.variedDurList: 
                for i in range(len(self.varied)):
                    if self.varied[i]:
                        s.append((t,self.signals[c][i]))
                    else:
                        s.append((self.dur[i]*self.timeScaleDict[self.scales[i]], self.signals[c][i]))
            self.seq.setDigital(c,s)
                
        self.seq.plot()
        
        # Load power and frequency
        
        
    def play(self):
        print("Play")
        
        # Trigger Generators 
        
        # trigger pulser
        start = TriggerStart.IMMEDIATE
        rearm = TriggerRearm.MANUAL
        n_runs = self.ui.repeatBox.value()
        final = OutputState.ZERO()
        
        if self.pulser:
            self.pulser.reset()
            self.pulser.constant(OutputState.ZERO())
            self.pulser.setTrigger(start=start, rearm=rearm)
            self.pulser.stream(self.seq, n_runs, final)
            
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
        print("----------Log Info----------")
        if self.ui.DTabWidget.currentIndex():
            print("this is a ODMR experiment")
            print("Frequency List : %s" %(self.freqList))
            print("Power : %s" %(self.power))
            print("Signals : %s" %(self.signals))
            print("Time Scales : %s" %(self.scales))
            print("Duration : %s" %(self.dur))
        else:
            print("this is Rabi experiment")
            print("Varying Duration List : %s" %(self.variedDurList))
            print("Frequency : %s" %(self.freq))
            print("Power : %s" %(self.power))
            print("Signals : %s" %(self.signals))
            print("Time Scales : %s" %(self.scales))
            print("Duration : %s" %(self.dur))
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())