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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 769)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.searchButton)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PlayPause.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.PlayPause)

        self.DTitle = QHBoxLayout()
        self.DTitle.setObjectName(u"DTitle")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.DTitle.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.DTitle.addItem(self.horizontalSpacer_2)

        self.dAdd = QPushButton(self.centralwidget)
        self.dAdd.setObjectName(u"dAdd")

        self.DTitle.addWidget(self.dAdd)


        self.verticalLayout.addLayout(self.DTitle)

        self.DArea = QScrollArea(self.centralwidget)
        self.DArea.setObjectName(u"DArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        sizePolicy2.setHeightForWidth(self.DArea.sizePolicy().hasHeightForWidth())
        self.DArea.setSizePolicy(sizePolicy2)
        self.DArea.setAutoFillBackground(False)
        self.DArea.setWidgetResizable(True)
        self.DCol = QWidget()
        self.DCol.setObjectName(u"DCol")
        self.DCol.setGeometry(QRect(0, 0, 904, 400))
        self.DCol.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.DCol)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.DId = QVBoxLayout()
        self.DId.setSpacing(0)
        self.DId.setObjectName(u"DId")
        self.DId.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_4 = QLabel(self.DCol)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(0, 0))

        self.DId.addWidget(self.label_4)

        self.label_8 = QLabel(self.DCol)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)

        self.DId.addWidget(self.label_8)

        self.label_5 = QLabel(self.DCol)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.DId.addWidget(self.label_5)

        self.label_6 = QLabel(self.DCol)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)

        self.DId.addWidget(self.label_6)

        self.label_7 = QLabel(self.DCol)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.DId.addWidget(self.label_7)

        self.label_9 = QLabel(self.DCol)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)

        self.DId.addWidget(self.label_9)

        self.label_10 = QLabel(self.DCol)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.DId.addWidget(self.label_10)

        self.label_11 = QLabel(self.DCol)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)

        self.DId.addWidget(self.label_11)

        self.label_12 = QLabel(self.DCol)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)

        self.DId.addWidget(self.label_12)

        self.label_3 = QLabel(self.DCol)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(0, 0))

        self.DId.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.DId)

        self.sequence = QVBoxLayout()
        self.sequence.setSpacing(0)
        self.sequence.setObjectName(u"sequence")
        self.frame = QFrame(self.DCol)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.duration = QSpinBox(self.frame)
        self.duration.setObjectName(u"duration")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.duration.sizePolicy().hasHeightForWidth())
        self.duration.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.duration)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.sequence.addWidget(self.frame)

        self.pushButton_2 = QPushButton(self.DCol)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy5)
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setCheckable(True)

        self.sequence.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.DCol)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy5.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy5)
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setCheckable(True)

        self.sequence.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.DCol)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy5.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy5)
        self.pushButton_4.setMinimumSize(QSize(0, 0))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setCheckable(True)

        self.sequence.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.DCol)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy5.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy5)
        self.pushButton_5.setMinimumSize(QSize(0, 0))
        self.pushButton_5.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setCheckable(True)

        self.sequence.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.DCol)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy5.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy5)
        self.pushButton_6.setMinimumSize(QSize(0, 0))
        self.pushButton_6.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setCheckable(True)

        self.sequence.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.DCol)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy5.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy5)
        self.pushButton_7.setMinimumSize(QSize(0, 0))
        self.pushButton_7.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_7.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setCheckable(True)

        self.sequence.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.DCol)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy5.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy5)
        self.pushButton_9.setMinimumSize(QSize(0, 0))
        self.pushButton_9.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_9.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setCheckable(True)

        self.sequence.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.DCol)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy5.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy5)
        self.pushButton_8.setMinimumSize(QSize(0, 0))
        self.pushButton_8.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setCheckable(True)

        self.sequence.addWidget(self.pushButton_8)

        self.pushButton = QPushButton(self.DCol)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy5)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setCheckable(False)

        self.sequence.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.sequence)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.DArea.setWidget(self.DCol)

        self.verticalLayout.addWidget(self.DArea)

        self.ATitle = QHBoxLayout()
        self.ATitle.setObjectName(u"ATitle")
        self.aLabel = QLabel(self.centralwidget)
        self.aLabel.setObjectName(u"aLabel")

        self.ATitle.addWidget(self.aLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ATitle.addItem(self.horizontalSpacer_3)

        self.aAdd = QPushButton(self.centralwidget)
        self.aAdd.setObjectName(u"aAdd")

        self.ATitle.addWidget(self.aAdd)


        self.verticalLayout.addLayout(self.ATitle)

        self.AArea = QScrollArea(self.centralwidget)
        self.AArea.setObjectName(u"AArea")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(3)
        sizePolicy6.setHeightForWidth(self.AArea.sizePolicy().hasHeightForWidth())
        self.AArea.setSizePolicy(sizePolicy6)
        self.AArea.setWidgetResizable(True)
        self.ACol = QWidget()
        self.ACol.setObjectName(u"ACol")
        self.ACol.setEnabled(True)
        self.ACol.setGeometry(QRect(0, 0, 904, 170))
        self.horizontalLayout_2 = QHBoxLayout(self.ACol)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.AId = QVBoxLayout()
        self.AId.setSpacing(0)
        self.AId.setObjectName(u"AId")
        self.AId.setSizeConstraint(QLayout.SetMinimumSize)
        self.AId.setContentsMargins(0, -1, 0, 0)
        self.label_13 = QLabel(self.ACol)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMinimumSize(QSize(0, 0))

        self.AId.addWidget(self.label_13)

        self.label_21 = QLabel(self.ACol)
        self.label_21.setObjectName(u"label_21")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy7)

        self.AId.addWidget(self.label_21)

        self.label_22 = QLabel(self.ACol)
        self.label_22.setObjectName(u"label_22")
        sizePolicy7.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy7)

        self.AId.addWidget(self.label_22)

        self.label_14 = QLabel(self.ACol)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)

        self.AId.addWidget(self.label_14)

        self.label_15 = QLabel(self.ACol)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.AId.addWidget(self.label_15)

        self.label_16 = QLabel(self.ACol)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMinimumSize(QSize(0, 0))

        self.AId.addWidget(self.label_16)


        self.horizontalLayout_2.addLayout(self.AId)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.ACol)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(3)
        sizePolicy8.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy8)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy7.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.frame_3)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(1)
        sizePolicy9.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy9)

        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(1)
        sizePolicy10.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy10)
        self.comboBox_2.setMinimumSize(QSize(0, 1))
        self.comboBox_2.setMaximumSize(QSize(55, 16777215))

        self.gridLayout.addWidget(self.comboBox_2, 0, 2, 1, 1)

        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        sizePolicy7.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.frame_3)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy9.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy9)

        self.gridLayout.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        sizePolicy7.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy10.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy10)

        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.pushButton_10 = QPushButton(self.ACol)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy5.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy5)
        self.pushButton_10.setMinimumSize(QSize(0, 0))
        self.pushButton_10.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_10.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.ACol)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy5.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy5)
        self.pushButton_11.setMinimumSize(QSize(0, 0))
        self.pushButton_11.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_11.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.ACol)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy5.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy5)
        self.pushButton_12.setMinimumSize(QSize(0, 0))
        self.pushButton_12.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_12.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_12)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.AArea.setWidget(self.ACol)

        self.verticalLayout.addWidget(self.AArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 924, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search devices", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IP address", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Digital Channels", None))
        self.dAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Channel 0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Channel 5", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Channel 6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Channel 7", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ns", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"micro", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"ms", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"s", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.aLabel.setText(QCoreApplication.translate("MainWindow", u"Analog Channels", None))
        self.aAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Channel 0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"period :", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"ns", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"micro", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"ms", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"s", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"reps :", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"type :", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"DC", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Sin", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Chirp", None))

        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

