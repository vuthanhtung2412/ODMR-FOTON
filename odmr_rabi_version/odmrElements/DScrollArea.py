from PySide6.QtCore import (QCoreApplication, QRect, QSize, Qt)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from odmrElements.DSequence import DSequence

class DScrollArea(QScrollArea):
    def __init__(self, parent = None) -> None:
        super(DScrollArea, self).__init__(parent)
        
        # Size Policies
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
        
        # Content
        self.setObjectName(u"odmrScrollArea")
        self.setSizePolicy(sizePolicy3)
        self.setAutoFillBackground(False)
        self.setWidgetResizable(True)
        self.odmrHLContainer = QWidget()
        self.odmrHLContainer.setObjectName(u"odmrHLContainer")
        self.odmrHLContainer.setGeometry(QRect(0, 0, 650, 259))
        self.odmrHLContainer.setAutoFillBackground(True)
        self.odmrHorizontalLayout = QHBoxLayout(self.odmrHLContainer)
        self.odmrHorizontalLayout.setObjectName(u"odmrHorizontalLayout")
        self.titleCol = QVBoxLayout()
        self.titleCol.setSpacing(0)
        self.titleCol.setObjectName(u"titleCol")
        
        self.label_11 = QLabel(self.odmrHLContainer)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMinimumSize(QSize(0, 0))

        self.titleCol.addWidget(self.label_11)
        
        self.titles = [QLineEdit(self.odmrHLContainer) for _ in range(8)]
        for i in range(len(self.titles)):
            self.titles[i].setObjectName(u"lineC%s" %(i))
            self.titles[i].setText("Channel %s" %(i))
            self.titles[i].setSizePolicy(sizePolicy4)
            self.titles[i].setContextMenuPolicy(Qt.DefaultContextMenu)

            self.titleCol.addWidget(self.titles[i])

        self.label_43 = QLabel(self.odmrHLContainer)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setSizePolicy(sizePolicy4)
        self.label_43.setMinimumSize(QSize(0, 0))

        self.titleCol.addWidget(self.label_43)


        self.odmrHorizontalLayout.addLayout(self.titleCol)
        
        # TODO : replace by DSequence obj
        self.DSequence = DSequence()
        
        self.sequence_3 = QVBoxLayout()
        self.sequence_3.setSpacing(0)
        self.sequence_3.setObjectName(u"sequence_3")
        
        # Duration
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

        # buttons
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

        self.setWidget(self.odmrHLContainer)
        
        self.retranslateUi

    def retranslateUi(self):
        """
        Description : Fill in text of elements with proper translation
        """
    
    def addSequence(self):
        pass