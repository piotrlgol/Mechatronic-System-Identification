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
        Dialog.resize(629, 161)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 100, 591, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.windowInput = QtWidgets.QLineEdit(Dialog)
        self.windowInput.setGeometry(QtCore.QRect(10, 50, 113, 22))
        self.windowInput.setObjectName("windowInput")
        self.persekInput = QtWidgets.QLineEdit(Dialog)
        self.persekInput.setGeometry(QtCore.QRect(160, 50, 113, 22))
        self.persekInput.setObjectName("persekInput")
        self.overlapInput = QtWidgets.QLineEdit(Dialog)
        self.overlapInput.setGeometry(QtCore.QRect(320, 50, 113, 22))
        self.overlapInput.setObjectName("overlapInput")
        self.nfftInput = QtWidgets.QLineEdit(Dialog)
        self.nfftInput.setGeometry(QtCore.QRect(470, 50, 113, 22))
        self.nfftInput.setObjectName("nfftInput")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(350, 20, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(500, 20, 55, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.windowInput.setText(_translate("Dialog", "hann"))
        self.persekInput.setText(_translate("Dialog", "50"))
        self.overlapInput.setText(_translate("Dialog", "0"))
        self.nfftInput.setText(_translate("Dialog", "1024"))
        self.label.setText(_translate("Dialog", "Window"))
        self.label_2.setText(_translate("Dialog", "nperseq"))
        self.label_3.setText(_translate("Dialog", "overlap"))
        self.label_4.setText(_translate("Dialog", "nfft"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

