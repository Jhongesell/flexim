from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator


class calculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    firNumber = None
    typingNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


        #our buttons
        self.pushButton_zero.clicked.connect(self.numberPressed)
        self.pushButton_one.clicked.connect(self.numberPressed)
        self.pushButton_two.clicked.connect(self.numberPressed)
        self.pushButton_three.clicked.connect(self.numberPressed)
        self.pushButton_four.clicked.connect(self.numberPressed)
        self.pushButton_five.clicked.connect(self.numberPressed)
        self.pushButton_six.clicked.connect(self.numberPressed)
        self.pushButton_seven.clicked.connect(self.numberPressed)
        self.pushButton_eight.clicked.connect(self.numberPressed)
        self.pushButton_nine.clicked.connect(self.numberPressed)

        self.pushButton_decimel.clicked.connect(self.decimalPressed)
        self.pushButton_plusminus.clicked.connect(self.unaryOperation)
        self.pushButton_modulus.clicked.connect(self.unaryOperation)

        self.pushButton_plus.clicked.connect(self.binaryOperation)
        self.pushButton_minus.clicked.connect(self.binaryOperation)
        self.pushButton_multiply.clicked.connect(self.binaryOperation)
        self.pushButton_divide.clicked.connect(self.binaryOperation)

        self.pushButton_equal.clicked.connect(self.equl_pressed)
        self.pushButton_clear.clicked.connect(self.clearbtn)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)


    #number pressed method
    def numberPressed(self):
        button = self.sender()

        if ((
                        self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or self.pushButton_divide.isChecked() or self.pushButton_multiply.isChecked()) and (
        not self.typingNumber)):
            lbl = format(float(button.text()), '.15g')
            self.typingNumber = True

        else:

            if (('.' in self.label.text()) and (button.text() == '0')):
                lbl = format(self.label.text() + button.text(), '.15')
            else:
                lbl = format(float(self.label.text() + button.text()), '.15g')

        self.label.setText(lbl)


    #decimel number pressed
    def decimalPressed(self):

         self.label.setText(self.label.text() + '.')


    #unaryopertio
    def unaryOperation(self):
        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == "+/-":
            labelNumber = labelNumber * -1
        else:
            labelNumber = labelNumber * 0.01

        newLabel = format(labelNumber, '.15g')

        self.label.setText(newLabel)


    #binary operation
    def binaryOperation(self):
        button = self.sender()

        self.firNumber = float(self.label.text())

        button.setChecked(True)





    def equl_pressed(self):
        secondNumber = float(self.label.text())

        if(self.pushButton_plus.isChecked()):
            labelNumber = self.firNumber + secondNumber
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_plus.setChecked(False)

        elif (self.pushButton_minus.isChecked()):
            labelNumber = self.firNumber - secondNumber
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_minus.setChecked(False)

        elif (self.pushButton_multiply.isChecked()):
            labelNumber = self.firNumber * secondNumber
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_multiply.setChecked(False)

        elif (self.pushButton_divide.isChecked()):
            labelNumber = self.firNumber / secondNumber
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)
        self.typingNumber = False





    def clearbtn(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)


        self.typingNumber = False

        self.label.setText("0")
