# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ODMRetRabi.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from odmrElements.binButton import BinButton
from odmrElements.AArea import AArea
from odmrElements.DScrollArea import DScrollArea

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(878, 621)
        
        # Size Policies
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(2)
        sizePolicy8.setVerticalStretch(0)
        
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        
        # Contents
        
        # Main layout
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainVerticalLayout = QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        
        # Search Pulser Streamer
        self.searchPSBox = QHBoxLayout()
        self.searchPSBox.setObjectName(u"searchPSBox")
        self.searchPSButton = QPushButton(self.centralwidget)
        self.searchPSButton.setObjectName(u"searchPSButton")
        self.searchPSButton.setSizePolicy(sizePolicy)

        self.searchPSBox.addWidget(self.searchPSButton)

        self.PSaddress = QLabel(self.centralwidget)
        self.PSaddress.setObjectName(u"PSaddress")
        self.PSaddress.setSizePolicy(sizePolicy1)

        self.searchPSBox.addWidget(self.PSaddress)

        self.mainVerticalLayout.addLayout(self.searchPSBox)
        
        # Search R&S generator
        self.searchRSBox = QHBoxLayout()
        self.searchRSBox.setObjectName(u"searchRSBox")
        self.searchRSButton = QPushButton(self.centralwidget)
        self.searchRSButton.setObjectName(u"searchRSButton")
        self.searchRSButton.setSizePolicy(sizePolicy)

        self.searchRSBox.addWidget(self.searchRSButton)

        self.RSaddress = QLabel(self.centralwidget)
        self.RSaddress.setObjectName(u"RSaddress")
        self.RSaddress.setSizePolicy(sizePolicy1)

        self.searchRSBox.addWidget(self.RSaddress)

        self.mainVerticalLayout.addLayout(self.searchRSBox)
        
        # Play Pause bar 
        self.PlayPause = QHBoxLayout()
        self.PlayPause.setObjectName(u"PlayPause")
        self.reps = QLabel(self.centralwidget)
        self.reps.setObjectName(u"reps")

        self.PlayPause.addWidget(self.reps)

        self.repeatBox = QSpinBox(self.centralwidget)
        self.repeatBox.setObjectName(u"repeatBox")
        self.repeatBox.setMinimum(1)
        self.repeatBox.setMaximum(1000)

        self.PlayPause.addWidget(self.repeatBox)

        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")
        self.PlayPause.addWidget(self.loadButton)
        
        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        self.PlayPause.addWidget(self.playButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.PlayPause.addWidget(self.cancelButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PlayPause.addItem(self.horizontalSpacer_3)

        self.mainVerticalLayout.addLayout(self.PlayPause)
        
        # Add digital channel
        self.addDChannelHL = QHBoxLayout()
        self.addDChannelHL.setObjectName(u"addDChannelHL")
        self.DTitle = QLabel(self.centralwidget)
        self.DTitle.setObjectName(u"DTitle")

        self.addDChannelHL.addWidget(self.DTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.addDChannelHL.addItem(self.horizontalSpacer)

        self.addDChannelBut = QPushButton(self.centralwidget)
        self.addDChannelBut.setObjectName(u"addDChannelBut")

        self.addDChannelHL.addWidget(self.addDChannelBut)

        self.mainVerticalLayout.addLayout(self.addDChannelHL)

        # Digital area
        self.DTabWidget = QTabWidget(self.centralwidget)
        self.DTabWidget.setObjectName(u"DTabWidget")
        self.DTabWidget.setSizePolicy(sizePolicy2)
        
        # Rabi Tab
        self.rabiTab = QWidget()
        self.rabiTab.setObjectName(u"rabiTab")
        self.rabiGrid = QGridLayout(self.rabiTab)
        self.rabiGrid.setObjectName(u"rabiGrid")
        
        # TODO : make this scroll area to class
        self.rabiScrollArea = DScrollArea(self.rabiTab)
        self.rabiScrollArea.setObjectName("rabiScrollArea")
        self.rabiGrid.addWidget(self.rabiScrollArea, 0, 0, 2, 1)
        
        # box to set light source parameter for rabi exp
        self.rabiSourceParamBox = QGroupBox(self.rabiTab)
        self.rabiSourceParamBox.setObjectName(u"rabiSourceParamBox")
        self.DVLayoutSourceParam = QVBoxLayout(self.rabiSourceParamBox)
        self.DVLayoutSourceParam.setObjectName(u"DVLayoutSourceParam")
        
        # Frequency
        self.HLRabiFreq = QHBoxLayout()
        self.HLRabiFreq.setSpacing(0)
        self.HLRabiFreq.setObjectName(u"HLRabiFreq")
        self.RabiFreqLabel = QLabel(self.rabiSourceParamBox)
        self.RabiFreqLabel.setObjectName(u"RabiFreqLabel")
        self.RabiFreqLabel.setSizePolicy(sizePolicy7)

        self.HLRabiFreq.addWidget(self.RabiFreqLabel)

        self.RabiFreqVal = QSpinBox(self.rabiSourceParamBox)
        self.RabiFreqVal.setObjectName(u"RabiFreqVal")
        self.RabiFreqVal.setSizePolicy(sizePolicy5)
        self.RabiFreqVal.setMinimum(1)
        self.RabiFreqVal.setMaximum(1000)

        self.HLRabiFreq.addWidget(self.RabiFreqVal)

        self.RabiFreqScale = QComboBox(self.rabiSourceParamBox)
        self.RabiFreqScale.addItem("")
        self.RabiFreqScale.addItem("")
        self.RabiFreqScale.addItem("")
        self.RabiFreqScale.addItem("")
        self.RabiFreqScale.setObjectName(u"RabiFreqScale")
        self.RabiFreqScale.setSizePolicy(sizePolicy5)

        self.HLRabiFreq.addWidget(self.RabiFreqScale)


        self.DVLayoutSourceParam.addLayout(self.HLRabiFreq)

        # Power
        self.HLRabiPower = QHBoxLayout()
        self.HLRabiPower.setSpacing(0)
        self.HLRabiPower.setObjectName(u"HLRabiPower")
        self.rabiPowerLabel = QLabel(self.rabiSourceParamBox)
        self.rabiPowerLabel.setObjectName(u"rabiPowerLabel")
        self.rabiPowerLabel.setSizePolicy(sizePolicy7)
        self.rabiPowerLabel.setMinimumSize(QSize(1, 0))

        self.HLRabiPower.addWidget(self.rabiPowerLabel)

        self.rabiPowerVal = QSpinBox(self.rabiSourceParamBox)
        self.rabiPowerVal.setObjectName(u"rabiPowerVal")
        self.rabiPowerVal.setSizePolicy(sizePolicy5)
        self.rabiPowerVal.setMinimumSize(QSize(0, 0))
        self.rabiPowerVal.setMinimum(1)
        self.rabiPowerVal.setMaximum(1000)

        self.HLRabiPower.addWidget(self.rabiPowerVal)

        self.rabiPowerScale = QComboBox(self.rabiSourceParamBox)
        self.rabiPowerScale.addItem("")
        self.rabiPowerScale.setObjectName(u"rabiPowerScale")
        self.rabiPowerScale.setSizePolicy(sizePolicy5)

        self.HLRabiPower.addWidget(self.rabiPowerScale)


        self.DVLayoutSourceParam.addLayout(self.HLRabiPower)


        self.rabiGrid.addWidget(self.rabiSourceParamBox, 1, 1, 1, 1)

        # Box to set Rabi variable time 
        self.rabiTimeVarBox = QGroupBox(self.rabiTab)
        self.rabiTimeVarBox.setObjectName(u"rabiTimeVarBox")
        self.rabiVarTimeVL = QVBoxLayout(self.rabiTimeVarBox)
        self.rabiVarTimeVL.setObjectName(u"rabiVarTimeVL")
        
        # Horizontal layout to set number of step
        self.rabiNbStepsHL = QHBoxLayout()
        self.rabiNbStepsHL.setSpacing(0)
        self.rabiNbStepsHL.setObjectName(u"rabiNbStepsHL")
        self.rabiStepLabel = QLabel(self.rabiTimeVarBox)
        self.rabiStepLabel.setObjectName(u"rabiStepLabel")
        self.rabiStepLabel.setSizePolicy(sizePolicy8)

        self.rabiNbStepsHL.addWidget(self.rabiStepLabel)

        self.rabiStepVal = QSpinBox(self.rabiTimeVarBox)
        self.rabiStepVal.setObjectName(u"rabiStepVal")
        self.rabiStepVal.setSizePolicy(sizePolicy5)
        self.rabiStepVal.setMinimum(1)
        self.rabiStepVal.setMaximum(1000)

        self.rabiNbStepsHL.addWidget(self.rabiStepVal)


        self.rabiVarTimeVL.addLayout(self.rabiNbStepsHL)

        # Horizontal layout to set starting point
        self.rabiStartTimeHL = QHBoxLayout()
        self.rabiStartTimeHL.setObjectName(u"rabiStartTimeHL")
        self.rabiStartTimeLabel = QLabel(self.rabiTimeVarBox)
        self.rabiStartTimeLabel.setObjectName(u"rabiStartTimeLabel")
        self.rabiStartTimeLabel.setSizePolicy(sizePolicy7)

        self.rabiStartTimeHL.addWidget(self.rabiStartTimeLabel)

        self.rabiStartTimeVal = QSpinBox(self.rabiTimeVarBox)
        self.rabiStartTimeVal.setObjectName(u"rabiStartTimeVal")
        self.rabiStartTimeVal.setSizePolicy(sizePolicy5)
        self.rabiStartTimeVal.setMinimum(1)
        self.rabiStartTimeVal.setMaximum(1000)

        self.rabiStartTimeHL.addWidget(self.rabiStartTimeVal)

        self.rabiStartTimeScale = QComboBox(self.rabiTimeVarBox)
        self.rabiStartTimeScale.addItem("")
        self.rabiStartTimeScale.addItem("")
        self.rabiStartTimeScale.addItem("")
        self.rabiStartTimeScale.addItem("")
        self.rabiStartTimeScale.setObjectName(u"rabiStartTimeScale")
        self.rabiStartTimeScale.setSizePolicy(sizePolicy5)
        self.rabiStartTimeScale.setMaximumSize(QSize(55, 16777215))

        self.rabiStartTimeHL.addWidget(self.rabiStartTimeScale)


        self.rabiVarTimeVL.addLayout(self.rabiStartTimeHL)

        # Horizontal layout to set end time
        self.rabiEndTimeHL = QHBoxLayout()
        self.rabiEndTimeHL.setObjectName(u"rabiEndTimeHL")
        self.rabiEndTimeLabel = QLabel(self.rabiTimeVarBox)
        self.rabiEndTimeLabel.setObjectName(u"rabiEndTimeLabel")
        self.rabiEndTimeLabel.setSizePolicy(sizePolicy7)

        self.rabiEndTimeHL.addWidget(self.rabiEndTimeLabel)

        self.rabiEndTimeVal = QSpinBox(self.rabiTimeVarBox)
        self.rabiEndTimeVal.setObjectName(u"rabiEndTimeVal")
        self.rabiEndTimeVal.setSizePolicy(sizePolicy9)
        self.rabiEndTimeVal.setMinimum(1)
        self.rabiEndTimeVal.setMaximum(1000)

        self.rabiEndTimeHL.addWidget(self.rabiEndTimeVal)

        self.rabiEndTimeScale = QComboBox(self.rabiTimeVarBox)
        self.rabiEndTimeScale.addItem("")
        self.rabiEndTimeScale.addItem("")
        self.rabiEndTimeScale.addItem("")
        self.rabiEndTimeScale.addItem("")
        self.rabiEndTimeScale.setObjectName(u"rabiEndTimeScale")
        self.rabiEndTimeScale.setSizePolicy(sizePolicy5)
        self.rabiEndTimeScale.setMaximumSize(QSize(55, 16777215))

        self.rabiEndTimeHL.addWidget(self.rabiEndTimeScale)


        self.rabiVarTimeVL.addLayout(self.rabiEndTimeHL)


        self.rabiGrid.addWidget(self.rabiTimeVarBox, 0, 1, 1, 1)

        self.DTabWidget.addTab(self.rabiTab, "")
        
        # ODMR tab
        self.odmrTab = QWidget()
        self.odmrTab.setObjectName(u"odmrTab")
        self.odmrTabHL = QHBoxLayout(self.odmrTab)
        self.odmrTabHL.setObjectName(u"odmrTabHL")
        # TODO : replace by a scroll area obj
        self.odmrScrollArea = DScrollArea(self.odmrTab)
        self.odmrScrollArea.setObjectName("odmrScrollAreas")
        self.odmrTabHL.addWidget(self.odmrScrollArea)
        
        # odmr variable light source 
        self.odmrSourceBox = QGroupBox(self.odmrTab)
        self.odmrSourceBox.setObjectName(u"odmrSourceBox")
        self.odmrSourceVLayout = QVBoxLayout(self.odmrSourceBox)
        self.odmrSourceVLayout.setObjectName(u"odmrSourceVLayout")
        
        # number of steps 
        self.odmrStepHLayout = QHBoxLayout()
        self.odmrStepHLayout.setSpacing(0)
        self.odmrStepHLayout.setObjectName(u"odmrStepHLayout")
        self.odmrStepLabel = QLabel(self.odmrSourceBox)
        self.odmrStepLabel.setObjectName(u"odmrStepLabel")
        self.odmrStepLabel.setSizePolicy(sizePolicy8)

        self.odmrStepHLayout.addWidget(self.odmrStepLabel)

        self.odmrStepVal = QSpinBox(self.odmrSourceBox)
        self.odmrStepVal.setObjectName(u"odmrStepVal")
        self.odmrStepVal.setSizePolicy(sizePolicy9)
        self.odmrStepVal.setMinimum(1)
        self.odmrStepVal.setMaximum(1000)

        self.odmrStepHLayout.addWidget(self.odmrStepVal)

        self.odmrSourceVLayout.addLayout(self.odmrStepHLayout)

        # odmr start freq
        self.odmrStartFreqHLayout = QHBoxLayout()
        self.odmrStartFreqHLayout.setSpacing(0)
        self.odmrStartFreqHLayout.setObjectName(u"odmrStartFreqHLayout")
        self.odmrStartFreqLabel = QLabel(self.odmrSourceBox)
        self.odmrStartFreqLabel.setObjectName(u"odmrStartFreqLabel")
        self.odmrStartFreqLabel.setSizePolicy(sizePolicy7)

        self.odmrStartFreqHLayout.addWidget(self.odmrStartFreqLabel)

        self.odmrStartFreqVal = QSpinBox(self.odmrSourceBox)
        self.odmrStartFreqVal.setObjectName(u"odmrStartFreqVal")
        self.odmrStartFreqVal.setSizePolicy(sizePolicy5)
        self.odmrStartFreqVal.setMinimum(1)
        self.odmrStartFreqVal.setMaximum(1000)

        self.odmrStartFreqHLayout.addWidget(self.odmrStartFreqVal)

        self.odmrStartFreqScale = QComboBox(self.odmrSourceBox)
        self.odmrStartFreqScale.addItem("")
        self.odmrStartFreqScale.addItem("")
        self.odmrStartFreqScale.addItem("")
        self.odmrStartFreqScale.addItem("")
        self.odmrStartFreqScale.setObjectName(u"odmrStartFreqScale")
        self.odmrStartFreqScale.setSizePolicy(sizePolicy5)

        self.odmrStartFreqHLayout.addWidget(self.odmrStartFreqScale)

        self.odmrSourceVLayout.addLayout(self.odmrStartFreqHLayout)

        # odmr end freq
        self.odmrEndFreqHLayout = QHBoxLayout()
        self.odmrEndFreqHLayout.setSpacing(0)
        self.odmrEndFreqHLayout.setObjectName(u"odmrEndFreqHLayout")
        self.odmrEndFreqLabel = QLabel(self.odmrSourceBox)
        self.odmrEndFreqLabel.setObjectName(u"odmrEndFreqLabel")
        self.odmrEndFreqLabel.setSizePolicy(sizePolicy7)

        self.odmrEndFreqHLayout.addWidget(self.odmrEndFreqLabel)

        self.odmrEndFreqVal = QSpinBox(self.odmrSourceBox)
        self.odmrEndFreqVal.setObjectName(u"odmrEndFreqVal")
        self.odmrEndFreqVal.setSizePolicy(sizePolicy5)
        self.odmrEndFreqVal.setMinimum(1)
        self.odmrEndFreqVal.setMaximum(1000)

        self.odmrEndFreqHLayout.addWidget(self.odmrEndFreqVal)

        self.odmrEndFreqScale = QComboBox(self.odmrSourceBox)
        self.odmrEndFreqScale.addItem("")
        self.odmrEndFreqScale.addItem("")
        self.odmrEndFreqScale.addItem("")
        self.odmrEndFreqScale.addItem("")
        self.odmrEndFreqScale.setObjectName(u"odmrEndFreqScale")
        self.odmrEndFreqScale.setSizePolicy(sizePolicy5)

        self.odmrEndFreqHLayout.addWidget(self.odmrEndFreqScale)

        self.odmrSourceVLayout.addLayout(self.odmrEndFreqHLayout)

        # odmr power
        self.odmrPowerHLayout = QHBoxLayout()
        self.odmrPowerHLayout.setSpacing(0)
        self.odmrPowerHLayout.setObjectName(u"odmrPowerHLayout")
        self.odmrPowerLabel = QLabel(self.odmrSourceBox)
        self.odmrPowerLabel.setObjectName(u"odmrPowerLabel")
        self.odmrPowerLabel.setSizePolicy(sizePolicy7)

        self.odmrPowerHLayout.addWidget(self.odmrPowerLabel)

        self.odmrPowerVal = QSpinBox(self.odmrSourceBox)
        self.odmrPowerVal.setObjectName(u"odmrPowerVal")
        self.odmrPowerVal.setSizePolicy(sizePolicy5)
        self.odmrPowerVal.setMinimum(1)
        self.odmrPowerVal.setMaximum(1000)

        self.odmrPowerHLayout.addWidget(self.odmrPowerVal)

        self.odmrPowerScale = QComboBox(self.odmrSourceBox)
        self.odmrPowerScale.addItem("")
        self.odmrPowerScale.setObjectName(u"odmrPowerScale")
        self.odmrPowerScale.setSizePolicy(sizePolicy5)
        self.odmrPowerScale.setMaximumSize(QSize(16777215, 16777215))

        self.odmrPowerHLayout.addWidget(self.odmrPowerScale)


        self.odmrSourceVLayout.addLayout(self.odmrPowerHLayout)

        self.odmrTabHL.addWidget(self.odmrSourceBox)

        self.DTabWidget.addTab(self.odmrTab, "")

        self.mainVerticalLayout.addWidget(self.DTabWidget)

        # Title for analog channel
        self.analogTitleHLayout = QHBoxLayout()
        self.analogTitleHLayout.setObjectName(u"analogTitleHLayout")
        self.analogTitleLabel = QLabel(self.centralwidget)
        self.analogTitleLabel.setObjectName(u"analogTitleLabel")

        self.analogTitleHLayout.addWidget(self.analogTitleLabel)

        self.analogTitleSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.analogTitleHLayout.addItem(self.analogTitleSpacer)

        self.addASequenceButton = QPushButton(self.centralwidget)
        self.addASequenceButton.setObjectName(u"addASequenceButton")

        self.analogTitleHLayout.addWidget(self.addASequenceButton)

        self.mainVerticalLayout.addLayout(self.analogTitleHLayout)

        # Area for analog signal
        self.AArea = AArea(self.centralwidget)
        self.mainVerticalLayout.addWidget(self.AArea)
        
        # Log state 
        self.logStateButton = QPushButton(self.centralwidget)
        self.logStateButton.setObjectName(u"logStateButton")
        self.logStateButton.setSizePolicy(sizePolicy3)
        self.mainVerticalLayout.addWidget(self.logStateButton)

        # Final set up 
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 878, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.DTabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchPSButton.setText(QCoreApplication.translate("MainWindow", u"Search Pulstreamer", None))
        self.PSaddress.setText(QCoreApplication.translate("MainWindow", u"pulse streamer IP address", None))
        self.searchRSButton.setText(QCoreApplication.translate("MainWindow", u"Search generator", None))
        self.RSaddress.setText(QCoreApplication.translate("MainWindow", u"generator address", None))
        self.reps.setText(QCoreApplication.translate("MainWindow", u"Reps :", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.DTitle.setText(QCoreApplication.translate("MainWindow", u"Digital channels (*checkbox for variable step)", None))
        self.addDChannelBut.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.rabiSourceParamBox.setTitle(QCoreApplication.translate("MainWindow", u"Light source param :", None))
        self.RabiFreqLabel.setText(QCoreApplication.translate("MainWindow", u"Frequency:", None))
        self.RabiFreqScale.setItemText(0, QCoreApplication.translate("MainWindow", u"Hz", None))
        self.RabiFreqScale.setItemText(1, QCoreApplication.translate("MainWindow", u"KHz", None))
        self.RabiFreqScale.setItemText(2, QCoreApplication.translate("MainWindow", u"MHz", None))
        self.RabiFreqScale.setItemText(3, QCoreApplication.translate("MainWindow", u"GHz", None))

        self.rabiPowerLabel.setText(QCoreApplication.translate("MainWindow", u"Power:", None))
        self.rabiPowerScale.setItemText(0, QCoreApplication.translate("MainWindow", u"dBm", None))

        self.rabiTimeVarBox.setTitle(QCoreApplication.translate("MainWindow", u"Time variable :", None))
        self.rabiStepLabel.setText(QCoreApplication.translate("MainWindow", u"Number of steps:", None))
        self.rabiStartTimeLabel.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.rabiStartTimeScale.setItemText(0, QCoreApplication.translate("MainWindow", u"ns", None))
        self.rabiStartTimeScale.setItemText(1, QCoreApplication.translate("MainWindow", u"micro", None))
        self.rabiStartTimeScale.setItemText(2, QCoreApplication.translate("MainWindow", u"ms", None))
        self.rabiStartTimeScale.setItemText(3, QCoreApplication.translate("MainWindow", u"s", None))

        self.rabiEndTimeLabel.setText(QCoreApplication.translate("MainWindow", u"to:", None))
        self.rabiEndTimeScale.setItemText(0, QCoreApplication.translate("MainWindow", u"ns", None))
        self.rabiEndTimeScale.setItemText(1, QCoreApplication.translate("MainWindow", u"micro", None))
        self.rabiEndTimeScale.setItemText(2, QCoreApplication.translate("MainWindow", u"ms", None))
        self.rabiEndTimeScale.setItemText(3, QCoreApplication.translate("MainWindow", u"s", None))

        self.DTabWidget.setTabText(self.DTabWidget.indexOf(self.rabiTab), QCoreApplication.translate("MainWindow", u"Rabi", None))
        self.odmrSourceBox.setTitle(QCoreApplication.translate("MainWindow", u"variable source:", None))
        self.odmrStepLabel.setText(QCoreApplication.translate("MainWindow", u"Number of steps:", None))
        self.odmrStartFreqLabel.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.odmrStartFreqScale.setItemText(0, QCoreApplication.translate("MainWindow", u"Hz", None))
        self.odmrStartFreqScale.setItemText(1, QCoreApplication.translate("MainWindow", u"KHz", None))
        self.odmrStartFreqScale.setItemText(2, QCoreApplication.translate("MainWindow", u"MHz", None))
        self.odmrStartFreqScale.setItemText(3, QCoreApplication.translate("MainWindow", u"GHz", None))

        self.odmrEndFreqLabel.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.odmrEndFreqScale.setItemText(0, QCoreApplication.translate("MainWindow", u"Hz", None))
        self.odmrEndFreqScale.setItemText(1, QCoreApplication.translate("MainWindow", u"KHz", None))
        self.odmrEndFreqScale.setItemText(2, QCoreApplication.translate("MainWindow", u"MHz", None))
        self.odmrEndFreqScale.setItemText(3, QCoreApplication.translate("MainWindow", u"GHz", None))

        self.odmrPowerLabel.setText(QCoreApplication.translate("MainWindow", u"Power:", None))
        self.odmrPowerScale.setItemText(0, QCoreApplication.translate("MainWindow", u"dBm", None))

        self.DTabWidget.setTabText(self.DTabWidget.indexOf(self.odmrTab), QCoreApplication.translate("MainWindow", u"ODMR", None))
        self.analogTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Analog channels (*checkbox for variable steps)", None))
        self.addASequenceButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        
        self.logStateButton.setText(QCoreApplication.translate("MainWindow", u"Log State", None))

    # retranslateUi
            
class DArea(QScrollArea):
    pass

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
        self.rabiGrid = QGridLayout(self.frame)
        self.rabiGrid.setSpacing(0)
        self.rabiGrid.setObjectName(u"rabiGrid")
        self.rabiGrid.setContentsMargins(0, 0, 0, 0)   
        
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        
        # Title and combo box to set up duration of a period
        self.period = QLabel(self.frame)
        self.period.setObjectName(u"period")
        self.period.setText(u"period :")
        self.period.setSizePolicy(sizePolicy1)
        self.rabiGrid.addWidget(self.period, 0, 0, 1, 1)
        
        self.periodVal = QSpinBox(self.frame)
        self.periodVal.setObjectName(u"periodVal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        self.periodVal.setSizePolicy(sizePolicy2)
        self.rabiGrid.addWidget(self.periodVal, 0, 1, 1, 1)   

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
        self.rabiGrid.addWidget(self.scale, 0, 2, 1, 1)     
        
        # Label and spinbox for reps
        self.rep = QLabel(self.frame)
        self.rep.setObjectName(u"rep")
        self.rep.setText(u"reps :")
        self.rep.setSizePolicy(sizePolicy1)
        self.rabiGrid.addWidget(self.rep, 1, 0, 1, 1)
        
        self.repVal = QSpinBox(self.frame)
        self.repVal.setObjectName(u"repVal")
        self.repVal.setSizePolicy(sizePolicy2)
        self.rabiGrid.addWidget(self.repVal, 1, 1, 1, 1)
        
        # label and combo box for type of signal
        self.type = QLabel(self.frame)
        self.type.setObjectName(u"type")
        self.type.setText(u"type :")
        self.type.setSizePolicy(sizePolicy1)
        self.rabiGrid.addWidget(self.type, 2, 0, 1, 1)
        
        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.addItem("DC")
        self.comboBox_3.addItem("Sin")
        self.comboBox_3.addItem("Chirp")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setSizePolicy(sizePolicy3)
        self.rabiGrid.addWidget(self.comboBox_3, 2, 1, 1, 2)
        
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
