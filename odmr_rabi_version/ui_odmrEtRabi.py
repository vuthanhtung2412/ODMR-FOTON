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
        
        # Main layout
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainVerticalLayout = QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        
        # Search device
        self.deviceSearchHLayout = QHBoxLayout()
        self.deviceSearchHLayout.setObjectName(u"deviceSearchHLayout")
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.searchButton.setSizePolicy(sizePolicy)

        self.deviceSearchHLayout.addWidget(self.searchButton)

        self.IPaddress = QLabel(self.centralwidget)
        self.IPaddress.setObjectName(u"IPaddress")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        self.IPaddress.setSizePolicy(sizePolicy1)

        self.deviceSearchHLayout.addWidget(self.IPaddress)

        self.mainVerticalLayout.addLayout(self.deviceSearchHLayout)
        
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        self.DTabWidget.setSizePolicy(sizePolicy2)
        
        # Rabi Tab
        self.rabiTab = QWidget()
        self.rabiTab.setObjectName(u"rabiTab")
        self.rabiGrid = QGridLayout(self.rabiTab)
        self.rabiGrid.setObjectName(u"rabiGrid")
        
        # TODO : make this scroll area to class
        self.rabiScrollArea = QScrollArea(self.rabiTab)
        self.rabiScrollArea.setObjectName(u"rabiScrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        self.rabiScrollArea.setSizePolicy(sizePolicy3)
        self.rabiScrollArea.setAutoFillBackground(False)
        self.rabiScrollArea.setWidgetResizable(True)
        # Horizontal layout of scroll area
        self.rabiHLayoutContainer = QWidget()
        self.rabiHLayoutContainer.setObjectName(u"rabiHLayoutContainer")
        self.rabiHLayoutContainer.setGeometry(QRect(0, 0, 634, 259))
        self.rabiHLayoutContainer.setAutoFillBackground(True)
        self.DHLayout = QHBoxLayout(self.rabiHLayoutContainer)
        self.DHLayout.setObjectName(u"DHLayout")
        
        # DTitle column
        self.DTitleColumn = QVBoxLayout()
        self.DTitleColumn.setSpacing(0)
        self.DTitleColumn.setObjectName(u"DTitleColumn")
        # ---
        self.label_5 = QLabel(self.rabiHLayoutContainer)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(0, 0))

        self.DTitleColumn.addWidget(self.label_5)
        
        # Title of channels
        # TODO : refractor with for loop
        self.lineC0 = QLineEdit(self.rabiHLayoutContainer)
        self.lineC0.setObjectName(u"lineC0")
        self.lineC0.setSizePolicy(sizePolicy4)
        self.lineC0.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.DTitleColumn.addWidget(self.lineC0)

        self.lineC1 = QLineEdit(self.rabiHLayoutContainer)
        self.lineC1.setObjectName(u"lineC1")
        self.lineC1.setSizePolicy(sizePolicy4)
        self.lineC1.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.DTitleColumn.addWidget(self.lineC1)

        self.lineC2 = QLineEdit(self.rabiHLayoutContainer)
        self.lineC2.setObjectName(u"lineC2")
        self.lineC2.setSizePolicy(sizePolicy4)
        self.lineC2.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.DTitleColumn.addWidget(self.lineC2)

        self.lineC3 = QLineEdit(self.rabiHLayoutContainer)
        self.lineC3.setObjectName(u"lineC3")
        self.lineC3.setSizePolicy(sizePolicy4)
        self.lineC3.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.DTitleColumn.addWidget(self.lineC3)

        self.lineC4 = QLineEdit(self.rabiHLayoutContainer)
        self.lineC4.setObjectName(u"lineC4")
        self.lineC4.setSizePolicy(sizePolicy4)
        self.lineC4.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.DTitleColumn.addWidget(self.lineC4)

        self.lineC5 = QLineEdit(self.rabiHLayoutContainer)
        self.lineC5.setObjectName(u"lineC5")
        self.lineC5.setSizePolicy(sizePolicy4)
        self.lineC5.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.DTitleColumn.addWidget(self.lineC5)

        self.lineC6 = QLineEdit(self.rabiHLayoutContainer)
        self.lineC6.setObjectName(u"lineC6")
        self.lineC6.setSizePolicy(sizePolicy4)
        self.lineC6.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.DTitleColumn.addWidget(self.lineC6)

        self.lineC7 = QLineEdit(self.rabiHLayoutContainer)
        self.lineC7.setObjectName(u"lineC7")
        self.lineC7.setSizePolicy(sizePolicy4)
        self.lineC7.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.DTitleColumn.addWidget(self.lineC7)

        # ---
        self.label_42 = QLabel(self.rabiHLayoutContainer)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setSizePolicy(sizePolicy4)
        self.label_42.setMinimumSize(QSize(0, 0))

        self.DTitleColumn.addWidget(self.label_42)


        self.DHLayout.addLayout(self.DTitleColumn)

        # Digital sequence column
        # TODO : create DSequence obj
        self.DSequence = QVBoxLayout()
        self.DSequence.setSpacing(0)
        self.DSequence.setObjectName(u"DSequence")
        
        # Frame to set duration
        self.frame_2 = QFrame(self.rabiHLayoutContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_19.addWidget(self.checkBox_2)

        self.duration = QSpinBox(self.frame_2)
        self.duration.setObjectName(u"duration")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        self.duration.setSizePolicy(sizePolicy5)
        self.duration.setMinimum(1)
        self.duration.setMaximum(1000)

        self.horizontalLayout_19.addWidget(self.duration)

        # Scale of the duration 
        self.comboBox_9 = QComboBox(self.frame_2)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_19.addWidget(self.comboBox_9)

        self.DSequence.addWidget(self.frame_2)
        
        # List of button:
        # TODO : refractor loop while to add button
        self.pushButton_18 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        
        self.pushButton_18.setSizePolicy(sizePolicy6)
        self.pushButton_18.setMinimumSize(QSize(0, 0))
        self.pushButton_18.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_18.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_18.setAutoFillBackground(False)
        self.pushButton_18.setCheckable(True)

        self.DSequence.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_19.setObjectName(u"pushButton_19")
        
        self.pushButton_19.setSizePolicy(sizePolicy6)
        self.pushButton_19.setMinimumSize(QSize(0, 0))
        self.pushButton_19.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_19.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_19.setAutoFillBackground(False)
        self.pushButton_19.setCheckable(True)

        self.DSequence.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_20.setObjectName(u"pushButton_20")
        
        self.pushButton_20.setSizePolicy(sizePolicy6)
        self.pushButton_20.setMinimumSize(QSize(0, 0))
        self.pushButton_20.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_20.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_20.setAutoFillBackground(False)
        self.pushButton_20.setCheckable(True)

        self.DSequence.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_21.setObjectName(u"pushButton_21")
        
        self.pushButton_21.setSizePolicy(sizePolicy6)
        self.pushButton_21.setMinimumSize(QSize(0, 0))
        self.pushButton_21.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_21.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_21.setAutoFillBackground(False)
        self.pushButton_21.setCheckable(True)

        self.DSequence.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_22.setObjectName(u"pushButton_22")
        
        self.pushButton_22.setSizePolicy(sizePolicy6)
        self.pushButton_22.setMinimumSize(QSize(0, 0))
        self.pushButton_22.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_22.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_22.setAutoFillBackground(False)
        self.pushButton_22.setCheckable(True)

        self.DSequence.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_23.setObjectName(u"pushButton_23")
        
        self.pushButton_23.setSizePolicy(sizePolicy6)
        self.pushButton_23.setMinimumSize(QSize(0, 0))
        self.pushButton_23.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_23.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_23.setAutoFillBackground(False)
        self.pushButton_23.setCheckable(True)

        self.DSequence.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_24.setObjectName(u"pushButton_24")
        
        self.pushButton_24.setSizePolicy(sizePolicy6)
        self.pushButton_24.setMinimumSize(QSize(0, 0))
        self.pushButton_24.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_24.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_24.setAutoFillBackground(False)
        self.pushButton_24.setCheckable(True)

        self.DSequence.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_25.setObjectName(u"pushButton_25")
        
        self.pushButton_25.setSizePolicy(sizePolicy6)
        self.pushButton_25.setMinimumSize(QSize(0, 0))
        self.pushButton_25.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_25.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_25.setAutoFillBackground(False)
        self.pushButton_25.setCheckable(True)

        self.DSequence.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.rabiHLayoutContainer)
        self.pushButton_26.setObjectName(u"pushButton_26")
        
        self.pushButton_26.setSizePolicy(sizePolicy6)
        self.pushButton_26.setMinimumSize(QSize(0, 0))
        self.pushButton_26.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_26.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_26.setAutoFillBackground(False)
        self.pushButton_26.setCheckable(False)

        self.DSequence.addWidget(self.pushButton_26)

        self.DHLayout.addLayout(self.DSequence)
        self.DSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.DHLayout.addItem(self.DSpacer)

        self.rabiScrollArea.setWidget(self.rabiHLayoutContainer)

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
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
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
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(2)
        sizePolicy8.setVerticalStretch(0)
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
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
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
        self.DScrollArea = DScrollArea(self.odmrTab)
        self.odmrScrollArea = QScrollArea(self.odmrTab)
        self.odmrScrollArea.setObjectName(u"odmrScrollArea")
        self.odmrScrollArea.setSizePolicy(sizePolicy3)
        self.odmrScrollArea.setAutoFillBackground(False)
        self.odmrScrollArea.setWidgetResizable(True)
        self.odmrHLContainer = QWidget()
        self.odmrHLContainer.setObjectName(u"odmrHLContainer")
        self.odmrHLContainer.setGeometry(QRect(0, 0, 650, 259))
        self.odmrHLContainer.setAutoFillBackground(True)
        self.odmrHorizontalLayout = QHBoxLayout(self.odmrHLContainer)
        self.odmrHorizontalLayout.setObjectName(u"odmrHorizontalLayout")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.odmrHLContainer)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMinimumSize(QSize(0, 0))

        self.verticalLayout_9.addWidget(self.label_11)

        self.lineEdit_11 = QLineEdit(self.odmrHLContainer)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setSizePolicy(sizePolicy4)
        self.lineEdit_11.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_9.addWidget(self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.odmrHLContainer)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setSizePolicy(sizePolicy4)
        self.lineEdit_12.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_9.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.odmrHLContainer)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setSizePolicy(sizePolicy4)
        self.lineEdit_13.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_9.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.odmrHLContainer)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setSizePolicy(sizePolicy4)
        self.lineEdit_14.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_9.addWidget(self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.odmrHLContainer)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setSizePolicy(sizePolicy4)
        self.lineEdit_15.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_9.addWidget(self.lineEdit_15)

        self.lineEdit_16 = QLineEdit(self.odmrHLContainer)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setSizePolicy(sizePolicy4)
        self.lineEdit_16.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_9.addWidget(self.lineEdit_16)

        self.lineEdit_17 = QLineEdit(self.odmrHLContainer)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setSizePolicy(sizePolicy4)
        self.lineEdit_17.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_9.addWidget(self.lineEdit_17)

        self.lineEdit_18 = QLineEdit(self.odmrHLContainer)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setSizePolicy(sizePolicy4)
        self.lineEdit_18.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_9.addWidget(self.lineEdit_18)

        self.label_43 = QLabel(self.odmrHLContainer)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setSizePolicy(sizePolicy4)
        self.label_43.setMinimumSize(QSize(0, 0))

        self.verticalLayout_9.addWidget(self.label_43)


        self.odmrHorizontalLayout.addLayout(self.verticalLayout_9)
        
        # TODO : replace by DSequence obj
        self.sequence_3 = QVBoxLayout()
        self.sequence_3.setSpacing(0)
        self.sequence_3.setObjectName(u"sequence_3")
        self.frame_4 = QFrame(self.odmrHLContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_22.addWidget(self.checkBox)

        self.duration_2 = QSpinBox(self.frame_4)
        self.duration_2.setObjectName(u"duration_2")
        self.duration_2.setSizePolicy(sizePolicy5)
        self.duration_2.setMinimum(1)
        self.duration_2.setMaximum(1000)

        self.horizontalLayout_22.addWidget(self.duration_2)

        self.comboBox_12 = QComboBox(self.frame_4)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_22.addWidget(self.comboBox_12)


        self.sequence_3.addWidget(self.frame_4)

        self.pushButton_27 = QPushButton(self.odmrHLContainer)
        self.pushButton_27.setObjectName(u"pushButton_27")
        
        self.pushButton_27.setSizePolicy(sizePolicy6)
        self.pushButton_27.setMinimumSize(QSize(0, 0))
        self.pushButton_27.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_27.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_27.setAutoFillBackground(False)
        self.pushButton_27.setCheckable(True)

        self.sequence_3.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.odmrHLContainer)
        self.pushButton_28.setObjectName(u"pushButton_28")
        
        self.pushButton_28.setSizePolicy(sizePolicy6)
        self.pushButton_28.setMinimumSize(QSize(0, 0))
        self.pushButton_28.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_28.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_28.setAutoFillBackground(False)
        self.pushButton_28.setCheckable(True)

        self.sequence_3.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.odmrHLContainer)
        self.pushButton_29.setObjectName(u"pushButton_29")
        
        self.pushButton_29.setSizePolicy(sizePolicy6)
        self.pushButton_29.setMinimumSize(QSize(0, 0))
        self.pushButton_29.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_29.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_29.setAutoFillBackground(False)
        self.pushButton_29.setCheckable(True)

        self.sequence_3.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.odmrHLContainer)
        self.pushButton_30.setObjectName(u"pushButton_30")
        
        self.pushButton_30.setSizePolicy(sizePolicy6)
        self.pushButton_30.setMinimumSize(QSize(0, 0))
        self.pushButton_30.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_30.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_30.setAutoFillBackground(False)
        self.pushButton_30.setCheckable(True)

        self.sequence_3.addWidget(self.pushButton_30)

        self.pushButton_31 = QPushButton(self.odmrHLContainer)
        self.pushButton_31.setObjectName(u"pushButton_31")
        
        self.pushButton_31.setSizePolicy(sizePolicy6)
        self.pushButton_31.setMinimumSize(QSize(0, 0))
        self.pushButton_31.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_31.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_31.setAutoFillBackground(False)
        self.pushButton_31.setCheckable(True)

        self.sequence_3.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.odmrHLContainer)
        self.pushButton_32.setObjectName(u"pushButton_32")
        
        self.pushButton_32.setSizePolicy(sizePolicy6)
        self.pushButton_32.setMinimumSize(QSize(0, 0))
        self.pushButton_32.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_32.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_32.setAutoFillBackground(False)
        self.pushButton_32.setCheckable(True)

        self.sequence_3.addWidget(self.pushButton_32)

        self.pushButton_33 = QPushButton(self.odmrHLContainer)
        self.pushButton_33.setObjectName(u"pushButton_33")
        
        self.pushButton_33.setSizePolicy(sizePolicy6)
        self.pushButton_33.setMinimumSize(QSize(0, 0))
        self.pushButton_33.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_33.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_33.setAutoFillBackground(False)
        self.pushButton_33.setCheckable(True)

        self.sequence_3.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.odmrHLContainer)
        self.pushButton_34.setObjectName(u"pushButton_34")
        
        self.pushButton_34.setSizePolicy(sizePolicy6)
        self.pushButton_34.setMinimumSize(QSize(0, 0))
        self.pushButton_34.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_34.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_34.setAutoFillBackground(False)
        self.pushButton_34.setCheckable(True)

        self.sequence_3.addWidget(self.pushButton_34)

        self.pushButton_35 = QPushButton(self.odmrHLContainer)
        self.pushButton_35.setObjectName(u"pushButton_35")
        
        self.pushButton_35.setSizePolicy(sizePolicy6)
        self.pushButton_35.setMinimumSize(QSize(0, 0))
        self.pushButton_35.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_35.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_35.setAutoFillBackground(False)
        self.pushButton_35.setCheckable(False)

        self.sequence_3.addWidget(self.pushButton_35)


        self.odmrHorizontalLayout.addLayout(self.sequence_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.odmrHorizontalLayout.addItem(self.horizontalSpacer_7)

        self.odmrScrollArea.setWidget(self.odmrHLContainer)

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
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.mainVerticalLayout.addLayout(self.horizontalLayout_4)

        # Area for analog signal
        self.AArea = AArea(self.centralwidget)
        self.mainVerticalLayout.addWidget(self.AArea)

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
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search devices", None))
        self.IPaddress.setText(QCoreApplication.translate("MainWindow", u"IP address", None))
        self.reps.setText(QCoreApplication.translate("MainWindow", u"Reps :", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.DTitle.setText(QCoreApplication.translate("MainWindow", u"Digital channels (*checkbox for variable step)", None))
        self.addDChannelBut.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.lineC0.setText(QCoreApplication.translate("MainWindow", u"Channel 0", None))
        self.lineC1.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.lineC2.setText(QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.lineC3.setText(QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.lineC4.setText(QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.lineC5.setText(QCoreApplication.translate("MainWindow", u"Channel 5", None))
        self.lineC6.setText(QCoreApplication.translate("MainWindow", u"Channel 6", None))
        self.lineC7.setText(QCoreApplication.translate("MainWindow", u"Channel 7", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.checkBox_2.setText("")
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"ns", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"micro", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"ms", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"s", None))

        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
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
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"Channel 0", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"Channel 5", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"Channel 6", None))
        self.lineEdit_18.setText(QCoreApplication.translate("MainWindow", u"Channel 7", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.checkBox.setText("")
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"ns", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"micro", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"ms", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"s", None))

        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Analog channels (*checkbox for variable steps)", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+", None))

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
