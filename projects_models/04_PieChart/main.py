from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gráfico de Resultados")
        self.setGeometry(100, 100, 1280, 600)

        self.show()

        self.create_piechart()

    def create_piechart(self):

        series = QPieSeries()
        series.append("EP2S2", 434)
        series.append("EP2S1", 434)
        series.append("SP2S2", 434)
        series.append("SP2S1", 434)

        #adding slice
        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkYellow, 2))
        slice.setBrush(Qt.yellow)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Caudales promedio para cada Estación")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)
                      
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
