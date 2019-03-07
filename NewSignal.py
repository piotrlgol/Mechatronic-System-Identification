import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QDialog
from NewSignalBox import Ui_Dialog
from SignalProcesing import Function

class NewFunctWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.function = Function(0,0,1)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept(self):
        time_start = float(self.ui.TimeStart.text())
        time_end = float(self.ui.TimeEnd.text())
        Fs = int(self.ui.Fs.text())
        t = np.linspace(time_start,time_end,Fs)
        equation_txt = self.ui.Equation.text()
        a = eval(equation_txt)
        self.function = Function(t,a,Fs)
        super().accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NewFunctWindow()
    w.show()
    sys.exit(app.exec_())