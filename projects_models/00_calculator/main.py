
1
2
3
4
5
6
7
8
9
10
11
	
import sys
from PyQt5.QtWidgets import QApplication
from calculator import calculatorWindow
 
 
app = QApplication(sys.argv)
calculator = calculatorWindow()
 
 
 
sys.exit(app.exec())
