# -*- coding: utf-8 -*-
# Widget para la calibración de caudal
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from GUI_calibracion_N01 import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        variable1 = float(self.ui.lineEdit_flexim.text())
        variable2 = float(self.ui.lineEdit_sedapal.text())
        if variable1 < variable2:
            variable3 = (variable1/variable2)*100
            variable4 = abs(100-variable3)
        elif variable2 < variable1:
            variable3 = (variable2/variable1)*100
            variable4 = abs(100-variable3)
        #else:
        #    variable3 = "son iguales ambos caudales"
        self.ui.label_response1.setText(str(variable3))
        self.ui.label_response2.setText(str(variable4))
        self.ui.label_response3.setText(str(variable3 + variable4))
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())