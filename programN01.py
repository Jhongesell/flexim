import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

df = pd.DataFrame({'Campo 1': ['Mary', 'Jimy', 'John'],
                   'Campo 2': [100, 200, 300],
                   'Campo 3': ['a', 'b', 'c']})
class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self.__data = data

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
    view.resize(800, 600)
    view.show()
    sys.exit(app.exec_())
