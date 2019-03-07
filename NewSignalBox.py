# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewSignalBox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.TimeStart = QtWidgets.QLineEdit(Dialog)
        self.TimeStart.setGeometry(QtCore.QRect(40, 50, 31, 31))
        self.TimeStart.setObjectName("TimeStart")
        self.Equation = QtWidgets.QLineEdit(Dialog)
        self.Equation.setGeometry(QtCore.QRect(20, 150, 361, 22))
        self.Equation.setObjectName("Equation")
        self.StartLabel = QtWidgets.QLabel(Dialog)
        self.StartLabel.setGeometry(QtCore.QRect(30, 20, 57, 16))
        self.StartLabel.setObjectName("StartLabel")
        self.EquationLabel = QtWidgets.QLabel(Dialog)
        self.EquationLabel.setGeometry(QtCore.QRect(140, 120, 101, 16))
        self.EquationLabel.setObjectName("EquationLabel")
        self.EndLabel = QtWidgets.QLabel(Dialog)
        self.EndLabel.setGeometry(QtCore.QRect(130, 20, 50, 16))
        self.EndLabel.setObjectName("EndLabel")
        self.TimeEnd = QtWidgets.QLineEdit(Dialog)
        self.TimeEnd.setGeometry(QtCore.QRect(140, 50, 31, 31))
        self.TimeEnd.setObjectName("TimeEnd")
        self.FsLabel = QtWidgets.QLabel(Dialog)
        self.FsLabel.setGeometry(QtCore.QRect(230, 20, 113, 16))
        self.FsLabel.setObjectName("FsLabel")
        self.Fs = QtWidgets.QLineEdit(Dialog)
        self.Fs.setGeometry(QtCore.QRect(230, 50, 121, 31))
        self.Fs.setObjectName("Fs")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 90, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.StartLabel.setText(_translate("Dialog", "Start time"))
        self.EquationLabel.setText(_translate("Dialog", "Function equation"))
        self.EndLabel.setText(_translate("Dialog", "End time"))
        self.FsLabel.setText(_translate("Dialog", "Sampling frequency"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

