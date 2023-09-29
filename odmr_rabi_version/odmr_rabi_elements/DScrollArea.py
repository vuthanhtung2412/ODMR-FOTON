from PySide6.QtCore import (QCoreApplication, QRect, QSize, Qt)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from odmr_rabi_elements.DSequence import DSequence

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
        self.DHLayout = QHBoxLayout(self.odmrHLContainer)
        self.DHLayout.setObjectName(u"DHLayout")
        self.titleCol = QVBoxLayout()
        self.titleCol.setSpacing(0)
        self.titleCol.setObjectName(u"titleCol")
        
        self.topCell = QLabel(self.odmrHLContainer)
        self.topCell.setText("-----")
        self.topCell.setObjectName(u"topCell")
        self.topCell.setSizePolicy(sizePolicy4)
        self.topCell.setMinimumSize(QSize(0, 0))

        self.titleCol.addWidget(self.topCell)
        
        self.titles = [QLineEdit(self.odmrHLContainer) for _ in range(8)]
        for i in range(len(self.titles)):
            self.titles[i].setObjectName(u"lineC%s" %(i))
            self.titles[i].setText("Channel %s" %(i))
            self.titles[i].setSizePolicy(sizePolicy4)
            self.titles[i].setContextMenuPolicy(Qt.DefaultContextMenu)

            self.titleCol.addWidget(self.titles[i])

        self.bottomCell = QLabel(self.odmrHLContainer)
        self.bottomCell.setObjectName(u"bottomCell")
        self.bottomCell.setText("-----")
        self.bottomCell.setSizePolicy(sizePolicy4)
        self.bottomCell.setMinimumSize(QSize(0, 0))

        self.titleCol.addWidget(self.bottomCell)

        self.DHLayout.addLayout(self.titleCol)
        
        # TODO : replace by DSequence obj
        self.DSequence = DSequence()
        
        self.DHLayout.addLayout(self.DSequence)

        self.DHLayoutSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.DHLayout.addItem(self.DHLayoutSpacer)

        self.setWidget(self.odmrHLContainer)
    
    def addSequence(self):
        print("%s : sequence added" %(self.objectName()))
        newSeq = DSequence()
        self.DHLayout.insertLayout(self.DHLayout.count()-1,newSeq)
        pass