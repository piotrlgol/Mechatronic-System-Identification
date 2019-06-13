import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QDialog, QRadioButton
from windows.cwtBox import Ui_Dialog

class cwtFunctWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.scMin = int(self.ui.ScalesMin.text())
        self.scMax = int(self.ui.ScalesMax.text())
        self.wavelet = "cmor"
        
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept(self):
        for button in self.ui.groupBox.findChildren(QRadioButton):
            if button.isChecked():
                self.wavelet = button.text()
            self.scMin = int(self.ui.ScalesMin.text())
            self.scMax = int(self.ui.ScalesMax.text())
        super().accept()
