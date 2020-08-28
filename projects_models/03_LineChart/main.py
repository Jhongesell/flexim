from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Resultados Gráficos")
        self.setGeometry(100,100, 680,500)
 
        self.show()
 
        self.create_linechart()
 
 
 
    def create_linechart(self):
 
        series = QLineSeries(self)
        series.append(0,4.50)
        series.append(6, 5.10)
        series.append(12, 4.11)
        series.append(18, 3.99)
        series.append(24, 5.36)
 
        series << QPointF(30, 4.78) << QPointF(36, 5.18) << QPointF(42, 4.78) << QPointF(48, 5.03) << QPointF(54, 5.45)
 
 
        chart =  QChart()
 
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Número de Mediciones VS. Caudales")
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
 
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
 
        self.setCentralWidget(chartview)
 
 
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
