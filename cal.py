# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit


class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLineEdit.mousePressEvent(self, event)


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(575, 758)
        Calculator.setMinimumSize(QtCore.QSize(575, 758))
        Calculator.setMaximumSize(QtCore.QSize(575, 758))
        Calculator.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.num1_input = ClickableLineEdit(self.centralwidget)
        self.num1_input.setGeometry(QtCore.QRect(60, 240, 171, 25))
        self.num1_input.setText("")
        self.num1_input.setObjectName("num1_input")
        self.num2_input = ClickableLineEdit(self.centralwidget)
        self.num2_input.setGeometry(QtCore.QRect(60, 270, 171, 25))
        self.num2_input.setObjectName("num2_input")
        self.num1_label = QtWidgets.QLabel(self.centralwidget)
        self.num1_label.setGeometry(QtCore.QRect(30, 240, 67, 17))
        self.num1_label.setObjectName("num1_label")
        self.num2_label = QtWidgets.QLabel(self.centralwidget)
        self.num2_label.setGeometry(QtCore.QRect(30, 270, 67, 17))
        self.num2_label.setObjectName("num2_label")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(330, 290, 67, 17))
        self.result_label.setObjectName("result_label")
        self.result_show = QtWidgets.QTextEdit(self.centralwidget)
        self.result_show.setEnabled(False)
        self.result_show.setGeometry(QtCore.QRect(330, 320, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(50)
        self.result_show.setFont(font)
        self.result_show.setObjectName("result_show")
        self.binary_label = QtWidgets.QLineEdit(self.centralwidget)
        self.binary_label.setEnabled(False)
        self.binary_label.setGeometry(QtCore.QRect(20, 330, 201, 21))
        self.binary_label.setObjectName("binary_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 410, 221, 17))
        self.label.setObjectName("label")
        self.numpad_label = QtWidgets.QLineEdit(self.centralwidget)
        self.numpad_label.setEnabled(False)
        self.numpad_label.setGeometry(QtCore.QRect(350, 480, 221, 25))
        self.numpad_label.setObjectName("numpad_label")
        self.one_button = QtWidgets.QPushButton(self.centralwidget)
        self.one_button.setGeometry(QtCore.QRect(370, 520, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.one_button.setFont(font)
        self.one_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.one_button.setObjectName("one_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget)
        self.three_button.setGeometry(QtCore.QRect(510, 520, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.three_button.setFont(font)
        self.three_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.three_button.setObjectName("three_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget)
        self.two_button.setGeometry(QtCore.QRect(440, 520, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.two_button.setFont(font)
        self.two_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.two_button.setObjectName("two_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget)
        self.six_button.setGeometry(QtCore.QRect(510, 570, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.six_button.setFont(font)
        self.six_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.six_button.setObjectName("six_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget)
        self.five_button.setGeometry(QtCore.QRect(440, 570, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.five_button.setFont(font)
        self.five_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.five_button.setObjectName("five_button")
        self.four_button = QtWidgets.QPushButton(self.centralwidget)
        self.four_button.setGeometry(QtCore.QRect(370, 570, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.four_button.setFont(font)
        self.four_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.four_button.setObjectName("four_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget)
        self.nine_button.setGeometry(QtCore.QRect(510, 620, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.nine_button.setFont(font)
        self.nine_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.nine_button.setObjectName("nine_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget)
        self.eight_button.setGeometry(QtCore.QRect(440, 620, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.eight_button.setFont(font)
        self.eight_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.eight_button.setObjectName("eight_button")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget)
        self.seven_button.setGeometry(QtCore.QRect(370, 620, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.seven_button.setFont(font)
        self.seven_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.seven_button.setObjectName("seven_button")
        self.backspace_button = QtWidgets.QPushButton(self.centralwidget)
        self.backspace_button.setGeometry(QtCore.QRect(510, 670, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.backspace_button.setFont(font)
        self.backspace_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.backspace_button.setObjectName("backspace_button")
        self.dot_button = QtWidgets.QPushButton(self.centralwidget)
        self.dot_button.setGeometry(QtCore.QRect(440, 670, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.dot_button.setFont(font)
        self.dot_button.setMouseTracking(False)
        self.dot_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dot_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.dot_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dot_button.setObjectName("dot_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(370, 670, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.zero_button.setFont(font)
        self.zero_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.zero_button.setObjectName("zero_button")
        self.unary_label = QtWidgets.QLineEdit(self.centralwidget)
        self.unary_label.setEnabled(False)
        self.unary_label.setGeometry(QtCore.QRect(20, 485, 201, 21))
        self.unary_label.setObjectName("unary_label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 520, 191, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mod_button_3 = QtWidgets.QPushButton(self.frame)
        self.mod_button_3.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.mod_button_3.setFont(font)
        self.mod_button_3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button_3.setObjectName("mod_button_3")
        self.mod_button_4 = QtWidgets.QPushButton(self.frame)
        self.mod_button_4.setGeometry(QtCore.QRect(70, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.mod_button_4.setFont(font)
        self.mod_button_4.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button_4.setObjectName("mod_button_4")
        self.mod_button_5 = QtWidgets.QPushButton(self.frame)
        self.mod_button_5.setGeometry(QtCore.QRect(130, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.mod_button_5.setFont(font)
        self.mod_button_5.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button_5.setObjectName("mod_button_5")
        self.mod_button_6 = QtWidgets.QPushButton(self.frame)
        self.mod_button_6.setGeometry(QtCore.QRect(10, 130, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.mod_button_6.setFont(font)
        self.mod_button_6.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button_6.setObjectName("mod_button_6")
        self.cos_button = QtWidgets.QPushButton(self.frame)
        self.cos_button.setGeometry(QtCore.QRect(70, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.cos_button.setFont(font)
        self.cos_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.cos_button.setObjectName("cos_button")
        self.sin_button = QtWidgets.QPushButton(self.frame)
        self.sin_button.setGeometry(QtCore.QRect(10, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.sin_button.setFont(font)
        self.sin_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sin_button.setObjectName("sin_button")
        self.tan_button = QtWidgets.QPushButton(self.frame)
        self.tan_button.setGeometry(QtCore.QRect(130, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.tan_button.setFont(font)
        self.tan_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tan_button.setObjectName("tan_button")
        self.sinh_button = QtWidgets.QPushButton(self.frame)
        self.sinh_button.setGeometry(QtCore.QRect(10, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.sinh_button.setFont(font)
        self.sinh_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sinh_button.setObjectName("sinh_button")
        self.cosh_button = QtWidgets.QPushButton(self.frame)
        self.cosh_button.setGeometry(QtCore.QRect(70, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.cosh_button.setFont(font)
        self.cosh_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.cosh_button.setObjectName("cosh_button")
        self.tanh_button_2 = QtWidgets.QPushButton(self.frame)
        self.tanh_button_2.setGeometry(QtCore.QRect(130, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.tanh_button_2.setFont(font)
        self.tanh_button_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tanh_button_2.setObjectName("tanh_button_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 370, 191, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.mod_button = QtWidgets.QPushButton(self.frame_2)
        self.mod_button.setGeometry(QtCore.QRect(10, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.mod_button.setFont(font)
        self.mod_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mod_button.setObjectName("mod_button")
        self.pow_button = QtWidgets.QPushButton(self.frame_2)
        self.pow_button.setGeometry(QtCore.QRect(70, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.pow_button.setFont(font)
        self.pow_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pow_button.setObjectName("pow_button")
        self.sum_button = QtWidgets.QPushButton(self.frame_2)
        self.sum_button.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sum_button.setFont(font)
        self.sum_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sum_button.setObjectName("sum_button")
        self.subtract_button = QtWidgets.QPushButton(self.frame_2)
        self.subtract_button.setGeometry(QtCore.QRect(70, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.subtract_button.setFont(font)
        self.subtract_button.setObjectName("subtract_button")
        self.mul_button = QtWidgets.QPushButton(self.frame_2)
        self.mul_button.setGeometry(QtCore.QRect(130, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.mul_button.setFont(font)
        self.mul_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mul_button.setObjectName("mul_button")
        self.div_button = QtWidgets.QPushButton(self.frame_2)
        self.div_button.setGeometry(QtCore.QRect(130, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.div_button.setFont(font)
        self.div_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.div_button.setObjectName("div_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.operations_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.operations_comboBox.setGeometry(QtCore.QRect(390, 220, 161, 31))
        self.operations_comboBox.setObjectName("operations_comboBox")
        self.operations_comboBox.addItem("")
        self.operations_comboBox.addItem("")
        self.operations_label = QtWidgets.QLabel(self.centralwidget)
        self.operations_label.setGeometry(QtCore.QRect(390, 190, 161, 21))
        self.operations_label.setObjectName("operations_label")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(330, 430, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.clear_button.setFont(font)
        self.clear_button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.clear_button.setObjectName("clear_button")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 22))
        self.menubar.setObjectName("menubar")
        self.menuCalculator = QtWidgets.QMenu(self.menubar)
        self.menuCalculator.setObjectName("menuCalculator")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)
        self.menuCalculator.addSeparator()
        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

        self.pointer = True  # if true means head pointed to num1_input

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.num1_label.setText(_translate("Calculator", "X"))
        self.num2_label.setText(_translate("Calculator", "Y"))
        self.result_label.setText(_translate("Calculator", "Result"))
        self.binary_label.setText(_translate("Calculator", "Binary Operations"))
        self.label.setText(_translate("Calculator", "-------------------------------------------------"))
        self.numpad_label.setText(_translate("Calculator", "NumPad"))
        self.one_button.setText(_translate("Calculator", "1"))
        self.three_button.setText(_translate("Calculator", "3"))
        self.two_button.setText(_translate("Calculator", "2"))
        self.six_button.setText(_translate("Calculator", "6"))
        self.five_button.setText(_translate("Calculator", "5"))
        self.four_button.setText(_translate("Calculator", "4"))
        self.nine_button.setText(_translate("Calculator", "9"))
        self.eight_button.setText(_translate("Calculator", "8"))
        self.seven_button.setText(_translate("Calculator", "7"))
        self.backspace_button.setText(_translate("Calculator", "<--"))
        self.dot_button.setText(_translate("Calculator", "."))
        self.zero_button.setText(_translate("Calculator", "0"))
        self.unary_label.setText(_translate("Calculator", "Unary Operations"))
        self.mod_button_3.setText(_translate("Calculator", "|x|"))
        self.mod_button_4.setText(_translate("Calculator", "sqrt"))
        self.mod_button_5.setText(_translate("Calculator", "log"))
        self.mod_button_6.setText(_translate("Calculator", "x-1"))
        self.cos_button.setText(_translate("Calculator", "Cos"))
        self.sin_button.setText(_translate("Calculator", "Sin"))
        self.tan_button.setText(_translate("Calculator", "Tan"))
        self.sinh_button.setText(_translate("Calculator", "Sin"))
        self.cosh_button.setText(_translate("Calculator", "Cos"))
        self.tanh_button_2.setText(_translate("Calculator", "Tan"))
        self.mod_button.setText(_translate("Calculator", "%"))
        self.pow_button.setText(_translate("Calculator", "x^y"))
        self.sum_button.setText(_translate("Calculator", "+"))
        self.subtract_button.setText(_translate("Calculator", "-"))
        self.mul_button.setText(_translate("Calculator", "*"))
        self.div_button.setText(_translate("Calculator", "/"))
        self.label_2.setText(_translate("Calculator", "The Amazing Calculator"))
        self.operations_comboBox.setItemText(0, _translate("Calculator", "Binary Operations"))
        self.operations_comboBox.setItemText(1, _translate("Calculator", "Unary Operations"))
        self.operations_label.setText(_translate("Calculator", "Select Operations type"))
        self.clear_button.setText(_translate("Calculator", "C"))
        self.menuCalculator.setTitle(_translate("Calculator", "Calculator"))

        # register event +, -, /, *, %
        self.sum_button.clicked.connect(self.sum_handle)
        self.subtract_button.clicked.connect(self.sub_handle)
        self.mul_button.clicked.connect(self.mul_handle)
        self.div_button.clicked.connect(self.div_handle)
        self.pow_button.clicked.connect(self.pow_handle)

        self.num1_input.clicked.connect(self.pointer1_handle)
        self.num2_input.clicked.connect(self.pointer2_handle)

        # numpad events
        self.one_button.clicked.connect(self.one_handle)
        self.two_button.clicked.connect(self.two_handle)
        self.three_button.clicked.connect(self.three_handle)
        self.four_button.clicked.connect(self.four_handle)
        self.five_button.clicked.connect(self.five_handle)
        self.six_button.clicked.connect(self.six_handle)
        self.seven_button.clicked.connect(self.seven_handle)
        self.eight_button.clicked.connect(self.eight_handle)
        self.nine_button.clicked.connect(self.nine_handle)
        self.zero_button.clicked.connect(self.zero_handle)
        self.dot_button.clicked.connect(self.dot_handle)
        self.backspace_button.clicked.connect(self.backspace_handle)

        # clear button handler
        self.clear_button.clicked.connect(self.clear_handle)

    def pointer1_handle(self):
        print('m is clicked')
        self.pointer = True

    def pointer2_handle(self):
        self.pointer = False

    def get_inputs(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            return num1, num2
        except ValueError:
            return 'error'

    def sum_handle(self):
        data = self.get_inputs()
        if data != 'error':
            num1, num2 = data
            self.result_show.setText(str(num1 + num2))
        else:
            self.result_show.setText('Kindly Enter valid input.')

    def sub_handle(self):
        data = self.get_inputs()
        if data != 'error':
            num1, num2 = data
            self.result_show.setText(str(num1 - num2))
        else:
            self.result_show.setText('Kindly Enter valid input.')

    def mul_handle(self):
        data = self.get_inputs()
        if data != 'error':
            num1, num2 = data
            self.result_show.setText(str(num1 * num2))
        else:
            self.result_show.setText('Kindly Enter valid input.')

    def div_handle(self):
        data = self.get_inputs()
        if data == 'error':
            self.result_show.setText('Kindly Enter valid input.')
        elif data[1] == 0:
            self.result_show.setText('undefined')
        else:
            num1, num2 = data
            self.result_show.setText(str(num1 / num2))

    def one_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(1))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(1))

    def two_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(2))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(2))

    def three_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(3))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(3))

    def four_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(4))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(4))

    def five_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(5))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(5))

    def six_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(6))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(6))

    def seven_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(7))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(7))

    def eight_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(8))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(8))

    def nine_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(9))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(9))

    def zero_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + str(0))
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + str(0))

    def dot_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text + '.')
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text + '.')

    def backspace_handle(self):
        if self.pointer:
            text = self.num1_input.text()
            self.num1_input.setText(text[:-1])
        else:
            text = self.num2_input.text()
            self.num2_input.setText(text[:-1])

    def pow_handle(self):
        x = float(self.num1_input.text())
        y = float(self.num2_input.text())
        try:
            self.result_show.setText(str(x**y))
        except OverflowError:
            self.result_show.setText('Overflow')

    def clear_handle(self):
        self.result_show.clear()
        self.num1_input.clear()
        self.num2_input.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
