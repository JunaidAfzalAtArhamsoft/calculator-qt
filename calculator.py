# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(573, 292)
        Calculator.setMinimumSize(QtCore.QSize(573, 292))
        self.centralwidget = QtWidgets.QWidget(Calculator)
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
        self.sum_button.setGeometry(QtCore.QRect(210, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sum_button.setFont(font)
        self.sum_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sum_button.setObjectName("sum_button")
        self.subtract_button = QtWidgets.QPushButton(self.centralwidget)
        self.subtract_button.setGeometry(QtCore.QRect(210, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.subtract_button.setFont(font)
        self.subtract_button.setObjectName("subtract_button")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(320, 30, 67, 17))
        self.result_label.setObjectName("result_label")
        self.result_show = QtWidgets.QTextEdit(self.centralwidget)
        self.result_show.setEnabled(False)
        self.result_show.setGeometry(QtCore.QRect(320, 120, 71, 71))
        self.result_show.setObjectName("result_show")
        self.mul_button = QtWidgets.QPushButton(self.centralwidget)
        self.mul_button.setGeometry(QtCore.QRect(160, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.mul_button.setFont(font)
        self.mul_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mul_button.setObjectName("mul_button")
        self.div_button = QtWidgets.QPushButton(self.centralwidget)
        self.div_button.setGeometry(QtCore.QRect(160, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.div_button.setFont(font)
        self.div_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.div_button.setObjectName("div_button")
        self.result_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.result_lcd.setGeometry(QtCore.QRect(320, 60, 201, 51))
        self.result_lcd.setObjectName("result_lcd")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 22))
        self.menubar.setObjectName("menubar")
        self.menuCalculator = QtWidgets.QMenu(self.menubar)
        self.menuCalculator.setObjectName("menuCalculator")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.num1_label.setText(_translate("Calculator", "Number 1"))
        self.num2_label.setText(_translate("Calculator", "Number 2"))
        self.sum_button.setText(_translate("Calculator", "+"))
        self.subtract_button.setText(_translate("Calculator", "-"))
        self.result_label.setText(_translate("Calculator", "Result"))
        self.mul_button.setText(_translate("Calculator", "*"))
        self.div_button.setText(_translate("Calculator", "/"))
        self.menuCalculator.setTitle(_translate("Calculator", "Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
