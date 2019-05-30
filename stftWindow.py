import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QDialog, QRadioButton
from windows.stftBox import Ui_Dialog

class stftFunctWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.window = "hann"
        self.persek = int(self.ui.persekInput.text())
        self.overlap = int(self.ui.overlapInput.text())
        self.nfft = int(self.ui.nfftInput.text())

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept(self):
        for button in self.ui.groupBox.findChildren(QRadioButton):
            if button.isChecked():
                self.window = button.text()
        self.persek = int(self.ui.persekInput.text())
        self.overlap = int(self.ui.overlapInput.text())
        self.nfft = int(self.ui.nfftInput.text())
        super().accept()