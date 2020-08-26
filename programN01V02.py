# -*- coding: utf-8 -*-
# ---------------------
# Nombre:       DMMv02.py (Discharge Measurement Manager)
# Autor:        Jhon Gesell
# Creado:       25 de febrero de 2020
# Modificado:   27 de febrero de 2020
# Licence: GNU V3
# ----------------------

__version__ = "1.0"

"""
Este es un visor de información respecto a las mediciones que se deben
hacer en La Atarjea - SEDAPAL
"""

# Versión Python: 3.6.9
# Versión PyQt5: 5.13.1

import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

df = pd.DataFrame({'Estación': ['Estacion 01', 'Estación 02', 'Estación 03', 'Estación 04'],
                  'Dirección': ['Salida', 'Salida', 'Salida', 'Salida'],
                  'Fecha y hora': ['25/02/2004', '26/02/2002', '27/02/2002', '03/03/2004'],
                   'Caudal (m3/s)': [10.4, 12.6, 16.9, 3.13]})
class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self.__data = data
        #self.setWindowsIcon(QIcon("ADCP.png"))
        

    def rowCount(self, parent=None):
        return self.__data.shape[0]

    def columnCount(self, parnet=None):
        return self.__data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.__data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.__data.columns[col]
        return None
if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = pandasModel(df)
    view = QTableView()
    view.setModel(model)
    view.resize(700, 400)
    view.show()
    sys.exit(app.exec_())
