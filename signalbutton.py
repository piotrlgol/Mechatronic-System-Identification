from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal

class SignalButton(QPushButton):
    isclicked = pyqtSignal(str)

    def __init__(self, name):
        QPushButton.__init__(self, name)
        self.text = " "
        self.clicked.connect(self.on_clicked)

    def on_clicked(self, str):
        print("in button: ", self.text)
        self.isclicked.emit(self.text)