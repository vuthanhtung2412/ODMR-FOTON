from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QPushButton, QSizePolicy)

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