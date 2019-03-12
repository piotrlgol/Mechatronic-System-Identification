import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QDialog
from stftBox import Ui_Dialog

class stftFunctWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.window = self.ui.windowInput.text()
        self.persek = int(self.ui.persekInput.text())
        self.overlap = int(self.ui.overlapInput.text())
        self.nfft = int(self.ui.nfftInput.text())

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept(self):
        self.window = self.ui.windowInput.text()
        self.persek = int(self.ui.persekInput.text())
        self.overlap = int(self.ui.overlapInput.text())
        self.nfft = int(self.ui.nfftInput.text())
        super().accept()