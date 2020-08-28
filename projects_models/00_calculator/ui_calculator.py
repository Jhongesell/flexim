# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 398)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"\n"
"border:1px solid green;\n"
"background-color:white;\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"\n"
"\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.pushButton_clear = QtWidgets.QPushButton(Dialog)
        self.pushButton_clear.setGeometry(QtCore.QRect(20, 80, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
"border:1px solid green;\n"
"\n"
"background-color:#2AFF55\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#2AFFAA\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_divide = QtWidgets.QPushButton(Dialog)
        self.pushButton_divide.setGeometry(QtCore.QRect(230, 80, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid gree;\n"
"background-color:#55FFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFFF;\n"
"\n"
"\n"
"}")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_modulus = QtWidgets.QPushButton(Dialog)
        self.pushButton_modulus.setGeometry(QtCore.QRect(160, 80, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_modulus.setFont(font)
        self.pushButton_modulus.setStyleSheet("QPushButton {\n"
"border:1px solid green;\n"
"\n"
"background-color:#2AFF55\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#2AFFAA\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_modulus.setObjectName("pushButton_modulus")
        self.pushButton_plusminus = QtWidgets.QPushButton(Dialog)
        self.pushButton_plusminus.setGeometry(QtCore.QRect(90, 80, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plusminus.setFont(font)
        self.pushButton_plusminus.setStyleSheet("QPushButton {\n"
"border:1px solid green;\n"
"\n"
"background-color:#2AFF55\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#2AFFAA\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_plusminus.setObjectName("pushButton_plusminus")
        self.pushButton_multiply = QtWidgets.QPushButton(Dialog)
        self.pushButton_multiply.setGeometry(QtCore.QRect(230, 140, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid gree;\n"
"background-color:#55FFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFFF;\n"
"\n"
"\n"
"}")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_nine = QtWidgets.QPushButton(Dialog)
        self.pushButton_nine.setGeometry(QtCore.QRect(160, 140, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_nine.setFont(font)
        self.pushButton_nine.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_nine.setObjectName("pushButton_nine")
        self.pushButton_eight = QtWidgets.QPushButton(Dialog)
        self.pushButton_eight.setGeometry(QtCore.QRect(90, 140, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_eight.setFont(font)
        self.pushButton_eight.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_eight.setObjectName("pushButton_eight")
        self.pushButton_seven = QtWidgets.QPushButton(Dialog)
        self.pushButton_seven.setGeometry(QtCore.QRect(20, 140, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_seven.setFont(font)
        self.pushButton_seven.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_seven.setObjectName("pushButton_seven")
        self.pushButton_minus = QtWidgets.QPushButton(Dialog)
        self.pushButton_minus.setGeometry(QtCore.QRect(230, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid gree;\n"
"background-color:#55FFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFFF;\n"
"\n"
"\n"
"}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_four = QtWidgets.QPushButton(Dialog)
        self.pushButton_four.setGeometry(QtCore.QRect(160, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_four.setFont(font)
        self.pushButton_four.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_four.setObjectName("pushButton_four")
        self.pushButton_five = QtWidgets.QPushButton(Dialog)
        self.pushButton_five.setGeometry(QtCore.QRect(90, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_five.setFont(font)
        self.pushButton_five.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_five.setObjectName("pushButton_five")
        self.pushButton_six = QtWidgets.QPushButton(Dialog)
        self.pushButton_six.setGeometry(QtCore.QRect(20, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_six.setFont(font)
        self.pushButton_six.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_six.setObjectName("pushButton_six")
        self.pushButton_plus = QtWidgets.QPushButton(Dialog)
        self.pushButton_plus.setGeometry(QtCore.QRect(230, 260, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid gree;\n"
"background-color:#55FFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFFF;\n"
"\n"
"\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_one = QtWidgets.QPushButton(Dialog)
        self.pushButton_one.setGeometry(QtCore.QRect(160, 260, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_one.setFont(font)
        self.pushButton_one.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_one.setObjectName("pushButton_one")
        self.pushButton_two = QtWidgets.QPushButton(Dialog)
        self.pushButton_two.setGeometry(QtCore.QRect(90, 260, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_two.setFont(font)
        self.pushButton_two.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_two.setObjectName("pushButton_two")
        self.pushButton_three = QtWidgets.QPushButton(Dialog)
        self.pushButton_three.setGeometry(QtCore.QRect(20, 260, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_three.setFont(font)
        self.pushButton_three.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_three.setObjectName("pushButton_three")
        self.pushButton_zero = QtWidgets.QPushButton(Dialog)
        self.pushButton_zero.setGeometry(QtCore.QRect(20, 320, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_zero.setFont(font)
        self.pushButton_zero.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid green;\n"
"background-color:#AAFFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFD4\n"
"\n"
"\n"
"}")
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_equal = QtWidgets.QPushButton(Dialog)
        self.pushButton_equal.setGeometry(QtCore.QRect(230, 320, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("QPushButton {\n"
"\n"
"border:1px solid gree;\n"
"background-color:#55FFAA;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#AAFFFF;\n"
"\n"
"\n"
"}")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_decimel = QtWidgets.QPushButton(Dialog)
        self.pushButton_decimel.setGeometry(QtCore.QRect(160, 320, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_decimel.setFont(font)
        self.pushButton_decimel.setStyleSheet("QPushButton {\n"
"border:1px solid green;\n"
"\n"
"background-color:#2AFF55\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color:#2AFFAA\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_decimel.setObjectName("pushButton_decimel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "0"))
        self.pushButton_clear.setText(_translate("Dialog", "C"))
        self.pushButton_divide.setText(_translate("Dialog", "/"))
        self.pushButton_modulus.setText(_translate("Dialog", "%"))
        self.pushButton_plusminus.setText(_translate("Dialog", "+/-"))
        self.pushButton_multiply.setText(_translate("Dialog", "x"))
        self.pushButton_nine.setText(_translate("Dialog", "9"))
        self.pushButton_eight.setText(_translate("Dialog", "8"))
        self.pushButton_seven.setText(_translate("Dialog", "7"))
        self.pushButton_minus.setText(_translate("Dialog", "-"))
        self.pushButton_four.setText(_translate("Dialog", "4"))
        self.pushButton_five.setText(_translate("Dialog", "5"))
        self.pushButton_six.setText(_translate("Dialog", "6"))
        self.pushButton_plus.setText(_translate("Dialog", "+"))
        self.pushButton_one.setText(_translate("Dialog", "1"))
        self.pushButton_two.setText(_translate("Dialog", "2"))
        self.pushButton_three.setText(_translate("Dialog", "3"))
        self.pushButton_zero.setText(_translate("Dialog", "0"))
        self.pushButton_equal.setText(_translate("Dialog", "="))
        self.pushButton_decimel.setText(_translate("Dialog", "."))
