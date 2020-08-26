from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PandasModel import PandasModel

class widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()
        self.pathLe = QtWidgets.QLineEdit(self)
        hLayout.addWidget(self.pathLe)
        self.loadBtn = QtWidgets.QPushButton("Seleccionar Archivo", self)
        hLayout.addWidget(self.loadBtn)
        vLayout.addLayout(hLayout)
        self.pandasTv = QtWidgets.QTableView(self)
        vLayout.addWidget(self.pandasTv)
        self.loadBtn.clicked.connect(self.loadFile)
        self.pandasTv.setSortingEnabled(True)

    def loadFile(self):
        #fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos CSV (*.csv)");
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos Excel (*.xlsx)");
        self.pathLe.setText(fileName)
        #df = pd.read_csv(fileName)
        df = pd.read_excel(fileName)
        model = PandasModel(df)
        self.pandasTv.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = widget()
    w.show()
    sys.exit(app.exec_())
