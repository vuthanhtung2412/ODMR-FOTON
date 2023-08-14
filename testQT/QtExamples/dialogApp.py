import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)  #__init__(parent) provokes QDialog init
        # super() are used to call a method from a parent class in a class that inherits from it
        # explicit form normally used in Python 2. super() is used in Python 3
        self.setWindowTitle("My Form")
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)
        
    def greetings(self):
        print(f"Hello {self.edit.text()}")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())