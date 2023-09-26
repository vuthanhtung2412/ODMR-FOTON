from PySide6.QtCore import (QCoreApplication, QRect, Qt, QSize)
from PySide6.QtWidgets import (QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class AArea(QScrollArea):
    def __init__(self, parent = None) -> None:
        super(AArea, self).__init__(parent)
        
        # Size Policies
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(3)
        
        # Content
        self.setObjectName(u"AArea")
        self.setSizePolicy(sizePolicy10)
        self.setWidgetResizable(True)
        self.ACol = QWidget()
        self.ACol.setObjectName(u"ACol")
        self.ACol.setEnabled(True)
        self.ACol.setGeometry(QRect(0, 0, 841, 157))
        self.horizontalLayout_2 = QHBoxLayout(self.ACol)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_16 = QLabel(self.ACol)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setMinimumSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.label_16)

        self.label_21 = QLabel(self.ACol)
        self.label_21.setObjectName(u"label_21")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(1)
        self.label_21.setSizePolicy(sizePolicy11)

        self.verticalLayout_7.addWidget(self.label_21)

        self.label_22 = QLabel(self.ACol)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setSizePolicy(sizePolicy11)

        self.verticalLayout_7.addWidget(self.label_22)

        self.lineEdit_6 = QLineEdit(self.ACol)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setSizePolicy(sizePolicy4)
        self.lineEdit_6.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_7.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.ACol)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setSizePolicy(sizePolicy4)
        self.lineEdit_7.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_7.addWidget(self.lineEdit_7)

        self.label_19 = QLabel(self.ACol)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setSizePolicy(sizePolicy4)
        self.label_19.setMinimumSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.label_19)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.ACol)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(3)
        self.frame_3.setSizePolicy(sizePolicy12)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setSizePolicy(sizePolicy11)

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.spinBox_11 = QSpinBox(self.frame_3)
        self.spinBox_11.setObjectName(u"spinBox_11")
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(1)
        self.spinBox_11.setSizePolicy(sizePolicy13)

        self.gridLayout_2.addWidget(self.spinBox_11, 0, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.frame_3)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(1)
        self.comboBox_6.setSizePolicy(sizePolicy14)
        self.comboBox_6.setMinimumSize(QSize(0, 1))
        self.comboBox_6.setMaximumSize(QSize(55, 16777215))

        self.gridLayout_2.addWidget(self.comboBox_6, 0, 2, 1, 1)

        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setSizePolicy(sizePolicy11)

        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)

        self.spinBox_12 = QSpinBox(self.frame_3)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setSizePolicy(sizePolicy13)

        self.gridLayout_2.addWidget(self.spinBox_12, 1, 1, 1, 1)

        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setSizePolicy(sizePolicy11)

        self.gridLayout_2.addWidget(self.label_24, 2, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.frame_3)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setSizePolicy(sizePolicy14)

        self.gridLayout_2.addWidget(self.comboBox_7, 2, 1, 1, 2)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.pushButton_10 = QPushButton(self.ACol)
        self.pushButton_10.setObjectName(u"pushButton_10")
        
        self.pushButton_10.setSizePolicy(sizePolicy6)
        self.pushButton_10.setMinimumSize(QSize(0, 0))
        self.pushButton_10.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_10.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.ACol)
        self.pushButton_11.setObjectName(u"pushButton_11")
        
        self.pushButton_11.setSizePolicy(sizePolicy6)
        self.pushButton_11.setMinimumSize(QSize(0, 0))
        self.pushButton_11.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_11.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.ACol)
        self.pushButton_12.setObjectName(u"pushButton_12")
        
        self.pushButton_12.setSizePolicy(sizePolicy6)
        self.pushButton_12.setMinimumSize(QSize(0, 0))
        self.pushButton_12.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_12.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setCheckable(False)

        self.verticalLayout_4.addWidget(self.pushButton_12)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.setWidget(self.ACol)
        
        self.retranslateUi()
        
    def retranslateUi(self):
        """
        Description : Fill in text of elements with proper translation
        """
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"Channel 0", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"period :", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"ns", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"micro", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"ms", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"s", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"reps :", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"type :", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"DC", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Sin", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Chirp", None))

        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    
    def addASequence(self):
        pass
