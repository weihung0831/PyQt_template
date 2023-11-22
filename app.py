import sys

from PyQt6 import QtWidgets
from qt_material import apply_stylesheet

from Controller.controller import Controller
from Model.model import Model
from View.view import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
apply_stylesheet(app, theme="dark_cyan.xml", css_file="./Resources/style.qss")
MainWindow = QtWidgets.QMainWindow()
controller = Controller(Model(), None)
view = Ui_MainWindow(controller)
view.setupUi(MainWindow)
controller.view = view
MainWindow.show()
sys.exit(app.exec())
