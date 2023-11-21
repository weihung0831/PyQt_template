from PyQt6.QtWidgets import *


class View(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MVC Example")
        self.setGeometry(100, 100, 200, 100)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.layout = QVBoxLayout(centralWidget)

        self.lineEdit = QLineEdit()
        self.layout.addWidget(self.lineEdit)

        self.button = QPushButton("Set Text")
        self.layout.addWidget(self.button)

        self.label = QLabel()
        self.layout.addWidget(self.label)

        self.click_button()

    def click_button(self):
        self.lineEdit.setText("Hello World")
        self.button.clicked.connect(self.controller.buttonClicked)

    def getText(self):
        return self.lineEdit.text()

    def setText(self, text):
        self.label.setText(text)
