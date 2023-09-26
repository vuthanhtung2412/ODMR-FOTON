from PySide6.QtCore import (QCoreApplication, QSize, Qt)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLayout, QPushButton, QSizePolicy, 
    QSpinBox, QVBoxLayout)

from odmrElements.binButton import BinButton

class DSequence(QVBoxLayout):
    def __init__(self) -> None:
        super(DSequence, self).__init__()
        # Size Policies
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
        self.setSpacing(0)
        self.setObjectName(u"sequence_3")
        
        # Duration
        self.frame_4 = QFrame()
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

        self.addWidget(self.frame_4)

        # buttons
        self.buttons = [BinButton() for _ in range(8)]
        for b in self.buttons:
            self.addWidget(b)
        
        # delete button
        self.deleteButton = QPushButton()
        self.deleteButton.setSizePolicy(sizePolicy6)
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

