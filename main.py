import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from GraphDisplay import Ui_MainWindow

from SignalProcesing import Math, Function
from NewSignal import NewFunctWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.function = None

        self.ui.TimeButton.text = "time"

        self.ui.newFunc.triggered.connect(self.new_function)
        self.ui.TimeButton.clicked.connect(self.call_Math)
        self.ui.FreqButton.clicked.connect(self.call_Math)

    def new_function(self):
        new_window = NewFunctWindow()
        if new_window.exec_():
            self.function = new_window.function

    def plot(self, x, y):
        self.ui.Display.canvas.ax.plot(x, y)
        self.ui.Display.canvas.draw()

    def call_Math(self, operation):
        print("in main: ", operation)
        if self.function is None:
            return
        if operation == "time":
            x, y = Math.time_domain(self.function)
            self.plot(x,y)
        elif operation == "freq":
            x, y = Math.frequency_domain(self.function)
            self.plot(x,y)
        elif operation == "stft":
            pass
        elif operation == "cwt":
            pass


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())


