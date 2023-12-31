# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pulseStreamer1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget,QGridLayout)

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow : QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(823, 742)
        
        # Set central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Search for device horizontal layout
        self.searchBar = QHBoxLayout()
        self.searchBar.setObjectName(u"searchBar")
        # search Button
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setText("Search")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchBar.addWidget(self.searchButton)
        # IP label
        self.IPLabel = QLabel(self.centralwidget)
        self.IPLabel.setObjectName(u"IP_label")
        self.IPLabel.setText("NO DEVICE DETECTED")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.IPLabel.setSizePolicy(sizePolicy)
        self.searchBar.addWidget(self.IPLabel)
        
        self.verticalLayout.addLayout(self.searchBar)
        
        # play pause horizontal layout
        self.PlayPause = QHBoxLayout()
        self.PlayPause.setObjectName(u"PlayPause")
        
        self.repeatBox = QSpinBox(self.centralwidget)
        self.repeatBox.setObjectName(u"repeatBox")
        self.PlayPause.addWidget(self.repeatBox)

        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        self.PlayPause.addWidget(self.playButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.PlayPause.addWidget(self.cancelButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PlayPause.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.PlayPause)
        
        # Title for digital signals
        self.DTitle = QHBoxLayout()
        self.DTitle.setObjectName(u"DTitle")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.DTitle.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.DTitle.addItem(self.horizontalSpacer_2)

        self.dAdd = QPushButton(self.centralwidget)
        self.dAdd.setObjectName(u"dAdd")

        self.DTitle.addWidget(self.dAdd)
        
        self.verticalLayout.addLayout(self.DTitle)

        # Scroll area for digital sequence
        self.DArea = QScrollArea(self.centralwidget)
        self.DArea.setObjectName(u"DArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        self.DArea.setSizePolicy(sizePolicy)
        self.DArea.setAutoFillBackground(False)
        self.DArea.setWidgetResizable(True)
        # Horizontal layout for digtal sequence
        self.DCol = QWidget()
        self.DCol.setObjectName(u"DCol")
        self.DCol.setGeometry(QRect(0, 0, 803, 448))
        self.DCol.setAutoFillBackground(True)
        self.DHL = QHBoxLayout(self.DCol)
        self.DHL.setSpacing(5)
        self.DHL.setObjectName(u"DHL")
        self.DHL.setContentsMargins(5, 5, 5, 5)
        self.DId = QVBoxLayout()
        
        # digital sequence first column 
        self.DId.setSpacing(0)
        self.DId.setObjectName(u"DId")
        self.DId.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        
        # add labels
        self.label_4 = QLabel(self.DCol)
        self.label_4.setObjectName(u"Dheader")
        self.label_4.setText("---")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(0, 0))

        self.DId.addWidget(self.label_4)
        
        # labels for 8 digital channels
        for i in range(8):
            tmp = QLabel(self.DCol)
            tmp.setObjectName(u"Dlabel_%s" % (i))
            tmp.setText(u"Channel %s" % (i))
            tmp.setSizePolicy(sizePolicy1)
            self.DId.addWidget(tmp)

        self.label_3 = QLabel(self.DCol)
        self.label_3.setObjectName(u"footer")
        self.label_3.setText("---")
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 0))

        self.DId.addWidget(self.label_3)

        self.DHL.addLayout(self.DId)
        
        # Spacer for digital area
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.DHL.addItem(self.horizontalSpacer_4)

        self.DArea.setWidget(self.DCol)

        self.verticalLayout.addWidget(self.DArea)
        
        # Title for analog sequence
        self.ATitle = QHBoxLayout()
        self.ATitle.setObjectName(u"ATitle")
        self.aLabel = QLabel(self.centralwidget)
        self.aLabel.setObjectName(u"aLabel")

        self.ATitle.addWidget(self.aLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ATitle.addItem(self.horizontalSpacer_3)

        self.aAdd = QPushButton(self.centralwidget)
        self.aAdd.setObjectName(u"aAdd")

        self.ATitle.addWidget(self.aAdd)

        self.verticalLayout.addLayout(self.ATitle)

        # Scroll area for analog sequence
        self.AArea = QScrollArea(self.centralwidget)
        self.AArea.setObjectName(u"AArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        self.AArea.setSizePolicy(sizePolicy4)
        self.AArea.setWidgetResizable(True)
        self.ACol = QWidget()
        self.ACol.setObjectName(u"ACol")
        self.ACol.setEnabled(True)
        self.ACol.setGeometry(QRect(0, 0, 803, 127))
        self.AHL = QHBoxLayout(self.ACol)
        self.AHL.setSpacing(5)
        self.AHL.setObjectName(u"AHL")
        self.AHL.setContentsMargins(5, 5, 5, 5)
        
        # First col of analog sequence
        self.AId = QVBoxLayout()
        self.AId.setSpacing(0)
        self.AId.setObjectName(u"AId")
        self.AId.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.AId.setContentsMargins(0, -1, 0, 0)
        
        for i in range(3):
            tmp = QLabel(self.DCol)
            tmp.setObjectName(u"Aheader_%s" % (i))
            tmp.setText("---")
            tmp.setSizePolicy(sizePolicy1)
            self.AId.addWidget(tmp)

        for i in range(2):
            tmp = QLabel(self.ACol)
            tmp.setObjectName(u"Alabel_%s" % (i))
            tmp.setText(u"Channel %s" % (i))
            tmp.setSizePolicy(sizePolicy1)
            self.AId.addWidget(tmp)

        self.label_16 = QLabel(self.ACol)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMinimumSize(QSize(0, 0))

        self.AId.addWidget(self.label_16)

        self.AHL.addLayout(self.AId)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.AHL.addItem(self.horizontalSpacer_5)

        self.AArea.setWidget(self.ACol)

        self.verticalLayout.addWidget(self.AArea)

        # Action / Menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 823, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        ### Button for debug ###
        self.logButton = QPushButton("Log")
        self.verticalLayout.addWidget(self.logButton)
        
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow : QMainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pulser Streamer Controller", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Digital Channels", None))
        self.dAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.aLabel.setText(QCoreApplication.translate("MainWindow", u"Analog Channels", None))
        self.aAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi
    
    ### Connect Signals and Slots ###
    def connectSignalsAndSlots(self):
        self.dAdd.clicked.connect(self.addDSequence)
        self.aAdd.clicked.connect(self.addASequence)
    
    def addDSequence(self):
        print("addDSequence called")
        newSeq = DSequence()
        self.DHL.insertLayout(self.DHL.count()-1,newSeq)
        pass
    
    def addASequence(self):
        print("addASequence called")
        newSeq = ASequence()
        self.AHL.insertLayout(self.AHL.count()-1,newSeq)
        pass

class BinButton(QPushButton):
    def __init__(self,parent=None):
        super(BinButton, self).__init__(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        self.setSizePolicy(sizePolicy)
        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.setCheckable(True)
        self.setText("0")
        
        self.clicked.connect(self.updateText)
        
        
    def updateText(self, b):
        if b:
            self.setText("1")
        else:
            self.setText("0")

class DSequence(QVBoxLayout):
    def __init__(self):
        super(DSequence, self).__init__()
        self.binButtons = [BinButton() for _ in range(8)]
        
        self.setSpacing(0)
        
        # timer
        self.frame = QFrame()
        
        # create sizePolicy
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        
        # size policy for the frame
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        
        # Horizontal layout
        self.DHL = QHBoxLayout(self.frame)
        self.DHL.setSpacing(0)
        self.DHL.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.DHL.setContentsMargins(0, 0, 0, 0)
        
        # duration spinbox
        self.duration = QSpinBox(self.frame)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        self.duration.setSizePolicy(sizePolicy2)

        self.DHL.addWidget(self.duration)
        
        # Scale combo box
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("ns")
        self.comboBox.addItem("micro")
        self.comboBox.addItem("ms")
        self.comboBox.addItem("s")
        self.comboBox.setMaximumSize(QSize(55, 16777215))

        self.DHL.addWidget(self.comboBox)

        self.addWidget(self.frame)
        
        # add buttons
        for b in self.binButtons:
            self.addWidget(b)
        
        self.deleteButton = QPushButton()
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        self.deleteButton.setSizePolicy(sizePolicy3)
        self.deleteButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))

        self.addWidget(self.deleteButton)
        
        # connect to delete slot
        self.deleteButton.clicked.connect(self.deleteSequence)
    
    def deleteSequence(self):
        print("Dsequence deleted")
        for i in reversed(range(self.count())): 
            self.itemAt(i).widget().deleteLater()
        
        self.deleteLater()
    
class ASequence(QVBoxLayout):
    def __init__(self):
        super(ASequence, self).__init__()
        self.binButtons = [BinButton() for _ in range(2)]

        self.setSpacing(0)
        # Header frame for analog channel
        self.frame = QFrame()
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        self.frame.setSizePolicy(sizePolicy)
        
        # Add grid layout to the frame
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)   
        
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        
        # Title and combo box to set up duration of a period
        self.period = QLabel(self.frame)
        self.period.setObjectName(u"period")
        self.period.setText(u"period :")
        self.period.setSizePolicy(sizePolicy1)
        self.gridLayout.addWidget(self.period, 0, 0, 1, 1)
        
        self.periodVal = QSpinBox(self.frame)
        self.periodVal.setObjectName(u"periodVal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        self.periodVal.setSizePolicy(sizePolicy2)
        self.gridLayout.addWidget(self.periodVal, 0, 1, 1, 1)   

        self.scale = QComboBox(self.frame)
        self.scale.addItem("ns")
        self.scale.addItem("micro")
        self.scale.addItem("ms")
        self.scale.addItem("s")
        self.scale.setObjectName(u"scale")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        self.scale.setSizePolicy(sizePolicy3)
        self.gridLayout.addWidget(self.scale, 0, 2, 1, 1)     
        
        # Label and spinbox for reps
        self.rep = QLabel(self.frame)
        self.rep.setObjectName(u"rep")
        self.rep.setText(u"reps :")
        self.rep.setSizePolicy(sizePolicy1)
        self.gridLayout.addWidget(self.rep, 1, 0, 1, 1)
        
        self.repVal = QSpinBox(self.frame)
        self.repVal.setObjectName(u"repVal")
        self.repVal.setSizePolicy(sizePolicy2)
        self.gridLayout.addWidget(self.repVal, 1, 1, 1, 1)
        
        # label and combo box for type of signal
        self.type = QLabel(self.frame)
        self.type.setObjectName(u"type")
        self.type.setText(u"type :")
        self.type.setSizePolicy(sizePolicy1)
        self.gridLayout.addWidget(self.type, 2, 0, 1, 1)
        
        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.addItem("DC")
        self.comboBox_3.addItem("Sin")
        self.comboBox_3.addItem("Chirp")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setSizePolicy(sizePolicy3)
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 2)
        
        self.addWidget(self.frame)
        
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        
        # add buttons
        for b in self.binButtons:
            self.addWidget(b)
            
        # delete button
        self.deleteButton = QPushButton()
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        self.deleteButton.setSizePolicy(sizePolicy4)
        self.deleteButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.addWidget(self.deleteButton)
        
        # connect to delete slot
        self.deleteButton.clicked.connect(self.deleteSequence)
        
    def deleteSequence(self):
        print("Dsequence deleted")
        for i in reversed(range(self.count())): 
            self.itemAt(i).widget().deleteLater()
        
        self.deleteLater()        
