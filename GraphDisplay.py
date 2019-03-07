# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartTime = QtWidgets.QLineEdit(self.centralwidget)
        self.StartTime.setGeometry(QtCore.QRect(640, 80, 113, 22))
        self.StartTime.setObjectName("StartTime")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 30, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 110, 91, 31))
        self.label_2.setObjectName("label_2")
        self.EndTime = QtWidgets.QLineEdit(self.centralwidget)
        self.EndTime.setGeometry(QtCore.QRect(640, 150, 113, 22))
        self.EndTime.setObjectName("EndTime")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 200, 131, 31))
        self.label_3.setObjectName("label_3")
        self.Fs = QtWidgets.QLineEdit(self.centralwidget)
        self.Fs.setGeometry(QtCore.QRect(640, 260, 113, 22))
        self.Fs.setObjectName("Fs")
        self.TimeButton = QtWidgets.QPushButton(self.centralwidget)
        self.TimeButton.setGeometry(QtCore.QRect(612, 310, 111, 31))
        self.TimeButton.setObjectName("TimeButton")
        self.FreqButton = QtWidgets.QPushButton(self.centralwidget)
        self.FreqButton.setGeometry(QtCore.QRect(612, 350, 121, 31))
        self.FreqButton.setObjectName("FreqButton")
        self.Display = MplWidget(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(10, 10, 591, 521))
        self.Display.setObjectName("Display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.newFunc = QtWidgets.QAction(MainWindow)
        self.newFunc.setObjectName("newFunc")
        self.actionFreq = QtWidgets.QAction(MainWindow)
        self.actionFreq.setObjectName("actionFreq")
        self.menuMenu.addAction(self.newFunc)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartTime.setInputMask(_translate("MainWindow", "#009"))
        self.StartTime.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Start Time"))
        self.label_2.setText(_translate("MainWindow", "End Time"))
        self.EndTime.setInputMask(_translate("MainWindow", "#009"))
        self.EndTime.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "Sampling frequency"))
        self.Fs.setInputMask(_translate("MainWindow", "0009"))
        self.Fs.setText(_translate("MainWindow", "200"))
        self.TimeButton.setText(_translate("MainWindow", "Time domain"))
        self.FreqButton.setText(_translate("MainWindow", "Frequency domain"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.newFunc.setText(_translate("MainWindow", "New"))
        self.actionFreq.setText(_translate("MainWindow", "Freq"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

