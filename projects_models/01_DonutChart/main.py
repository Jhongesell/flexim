from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt
 
 
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Gráfico de Resultados")
        self.setGeometry(100,100, 1280,600)
 
        self.show()
 
        
        self.crear_grafico()

    def crear_grafico(self):
 
        series = QPieSeries()
        series.setHoleSize(0.35)
        series.append("Entrada Planta 2 - Sector 1, 7.0%", 7)
        slice = QPieSlice()
        slice = series.append("Entrada Planta 2 - Sector 2, 30.0%", 30)
        slice.setExploded()
        slice.setLabelVisible()
        series.append("Salida Planta 2 - Sector 1, 8.0%", 8);
        series.append("Salida Planta 2 - Sector 2, 55.0%", 55);
 
 
 
 
 
        chart = QChart()
        #chart.legend().hide()
        chart.addSeries(series)
 
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Estaciones de Medición")
        #chart.setTheme(QChart.ChartThemeBlueCerulean)
        #chart.setTheme(QChart.ChartThemeBrownSand)
        #chart.setTheme(QChart.ChartThemeLight)
        chart.setTheme(QChart.ChartThemeDark)
 
 
 
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
 
 
        self.setCentralWidget(chartview)
 
 
 
 
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
