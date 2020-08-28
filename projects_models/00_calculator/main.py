import sys
from PyQt5.QtWidgets import QApplication
from calculator import calculatorWindow
 
 
app = QApplication(sys.argv)
calculator = calculatorWindow()
 
 
 
sys.exit(app.exec())
