from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
 
 
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Registros de las Mediciones")
        self.setGeometry(100,100, 680,500)
        self.show()
        self.create_bar()
 
 
 
 
    def create_bar(self):
        #The QBarSet class represents a set of bars in the bar chart.
         # It groups several bars into a bar set
 
        set0 = QBarSet("Campaña 1")
        set1 = QBarSet("Campaña 2")
        set2 = QBarSet("Campaña 3")
 
        set0 << 33 << 33 << 33 << 33
        set1 << 33 << 33 << 33 << 33
        set2 << 33 << 33 << 33 << 33

 
        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
 
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Porcentaje por Estaciones")
        chart.setAnimationOptions(QChart.SeriesAnimations)
 
        categories = ["EP2S1", "EP2S2", "SP2S1", "SP2S2"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
 
        self.setCentralWidget(chartView)
 
 
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
