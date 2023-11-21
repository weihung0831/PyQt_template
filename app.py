import sys

from PyQt6.QtWidgets import *

from Controller.controller import Controller
from Model.model import Model
from View.view import View

app = QApplication(sys.argv)
model = Model()
controller = Controller(model, None)
view = View(controller)
controller.view = view
view.show()
sys.exit(app.exec())
