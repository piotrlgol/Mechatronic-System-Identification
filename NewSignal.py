import sys
import numpy as np
import h5py
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QDialog, QFileDialog
from NewSignalBox import Ui_Dialog
from SignalProcesing import Function

from scipy.io import loadmat

class NewFunctWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.function = Function(0,0,1)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.BrowseButton.clicked.connect(self.choose_file)

    def accept(self):
        try:
            mat = loadmat(self.ui.FilePathLine.text())
            t = mat["t"][0]
            a = mat["x"][0]
            Fs = (1/(t[1]-t[0]))
        except FileNotFoundError:      
            time_start = float(self.ui.TimeStart.text())
            time_end = float(self.ui.TimeEnd.text())
            Fs = int(self.ui.Fs.text())
            t = np.linspace(time_start,time_end-(1/Fs),Fs)
            equation_txt = self.ui.Equation.text()
            a = eval(equation_txt)
        finally:
            self.function = Function(t,a,Fs)
            super().accept()

    def choose_file(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file',
                                            'C:\\',
                                            "Function (*.mat)")
        self.ui.FilePathLine.setProperty("text", fname[0])

96
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NewFunctWindow()
    w.show()
    sys.exit(app.exec_())