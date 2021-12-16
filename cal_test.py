# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 292)
        MainWindow.setMinimumSize(QtCore.QSize(573, 292))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.num1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.num1_input.setGeometry(QtCore.QRect(130, 20, 113, 25))
        self.num1_input.setObjectName("num1_input")
        self.num2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.num2_input.setGeometry(QtCore.QRect(130, 50, 113, 25))
        self.num2_input.setObjectName("num2_input")
        self.num1_label = QtWidgets.QLabel(self.centralwidget)
        self.num1_label.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.num1_label.setObjectName("num1_label")
        self.num2_label = QtWidgets.QLabel(self.centralwidget)
        self.num2_label.setGeometry(QtCore.QRect(20, 50, 67, 17))
        self.num2_label.setObjectName("num2_label")
        self.sum_button = QtWidgets.QPushButton(self.centralwidget)
        self.sum_button.setGeometry(QtCore.QRect(160, 90, 89, 25))
        self.sum_button.setObjectName("sum_button")
        self.subtract_button = QtWidgets.QPushButton(self.centralwidget)
        self.subtract_button.setGeometry(QtCore.QRect(160, 130, 89, 25))
        self.subtract_button.setObjectName("subtract_button")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(330, 30, 67, 17))
        self.result_label.setObjectName("result_label")
        self.result_show = QtWidgets.QTextEdit(self.centralwidget)
        self.result_show.setEnabled(False)
        self.result_show.setGeometry(QtCore.QRect(330, 50, 191, 91))
        self.result_show.setObjectName("result_show")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 22))
        self.menubar.setObjectName("menubar")
        self.menuCalculator = QtWidgets.QMenu(self.menubar)
        self.menuCalculator.setObjectName("menuCalculator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.num1_label.setText(_translate("MainWindow", "Number 1"))
        self.num2_label.setText(_translate("MainWindow", "Number 2"))
        self.sum_button.setText(_translate("MainWindow", "Sum ( + )"))
        self.subtract_button.setText(_translate("MainWindow", "Subtract ( - )"))
        self.result_label.setText(_translate("MainWindow", "Result"))
        self.menuCalculator.setTitle(_translate("MainWindow", "Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
