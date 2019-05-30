# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stftBox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 298)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 250, 591, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.persekInput = QtWidgets.QLineEdit(Dialog)
        self.persekInput.setGeometry(QtCore.QRect(160, 50, 113, 22))
        self.persekInput.setObjectName("persekInput")
        self.overlapInput = QtWidgets.QLineEdit(Dialog)
        self.overlapInput.setGeometry(QtCore.QRect(320, 50, 113, 22))
        self.overlapInput.setObjectName("overlapInput")
        self.nfftInput = QtWidgets.QLineEdit(Dialog)
        self.nfftInput.setGeometry(QtCore.QRect(470, 50, 113, 22))
        self.nfftInput.setObjectName("nfftInput")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(350, 20, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(500, 20, 55, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 120, 221))
        self.groupBox.setObjectName("groupBox")
        self.radBoxcar = QtWidgets.QRadioButton(self.groupBox)
        self.radBoxcar.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.radBoxcar.setChecked(False)
        self.radBoxcar.setObjectName("radBoxcar")
        self.radTriang = QtWidgets.QRadioButton(self.groupBox)
        self.radTriang.setGeometry(QtCore.QRect(10, 60, 95, 20))
        self.radTriang.setObjectName("radTriang")
        self.radBlackam = QtWidgets.QRadioButton(self.groupBox)
        self.radBlackam.setGeometry(QtCore.QRect(10, 90, 95, 20))
        self.radBlackam.setObjectName("radBlackam")
        self.radHamming = QtWidgets.QRadioButton(self.groupBox)
        self.radHamming.setGeometry(QtCore.QRect(10, 120, 95, 20))
        self.radHamming.setObjectName("radHamming")
        self.radHann = QtWidgets.QRadioButton(self.groupBox)
        self.radHann.setGeometry(QtCore.QRect(10, 150, 95, 20))
        self.radHann.setChecked(True)
        self.radHann.setObjectName("radHann")
        self.radBartlett = QtWidgets.QRadioButton(self.groupBox)
        self.radBartlett.setGeometry(QtCore.QRect(10, 180, 95, 20))
        self.radBartlett.setObjectName("radBartlett")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.persekInput.setText(_translate("Dialog", "50"))
        self.overlapInput.setText(_translate("Dialog", "0"))
        self.nfftInput.setText(_translate("Dialog", "1024"))
        self.label_2.setText(_translate("Dialog", "nperseq"))
        self.label_3.setText(_translate("Dialog", "overlap"))
        self.label_4.setText(_translate("Dialog", "nfft"))
        self.groupBox.setTitle(_translate("Dialog", "Window"))
        self.radBoxcar.setText(_translate("Dialog", "boxcar"))
        self.radTriang.setText(_translate("Dialog", "triang"))
        self.radBlackam.setText(_translate("Dialog", "blackman"))
        self.radHamming.setText(_translate("Dialog", "hamming"))
        self.radHann.setText(_translate("Dialog", "hann"))
        self.radBartlett.setText(_translate("Dialog", "bartlett"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

