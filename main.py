import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from GraphDisplay import Ui_MainWindow

from SignalProcesing import Math, Function
from NewSignal import NewFunctWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.m = PlotCanvas(self, width=5, height=5)
        self.ui.m.move(0,30)
        self.show()

        self.function = Function(0,0,1)

        self.ui.newFunc.triggered.connect(self.new_function)
        self.ui.TimeButton.clicked.connect(self.ui.m.plot_time)
        self.ui.FreqButton.clicked.connect(self.ui.m.plot_freq)

    def new_function(self):
        new_window = NewFunctWindow()
        if new_window.exec_():
            self.function = new_window.function

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=3, height=3, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.parent = parent
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
    def plot_time(self):
        self.fig.clear()
        # plt.plot(self.parent.function.time, self.parent.function.amplitude) 
        # ax = self.fig.add_axes([0,0,1,1])
        self.axes.plot(self.parent.function.time, self.parent.function.amplitude, color='blue', lw=2)
        self.draw()

    def plot_freq(self):
        self.fig.clear()
        # ax = self.fig.add_axes([0,0,1,1])
        signal_frequency = np.fft.fft(self.parent.function.amplitude)
        frequency = np.fft.fftfreq(self.parent.function.time.size, 1/self.parent.function.Fs)
        self.axes.plot(frequency, signal_frequency, color='blue', lw=2)
        self.draw()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())


