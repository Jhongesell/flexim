# -*- coding: utf-8 -*-p
# -----------------------
# Nombre:     DDMv01.py (Discharge Measurement Manager)
# Autor:      Jhon Gesell
# Creado:     25 de febrero de 2020
# Modificado: 25 de febrero de 2020
# Licence: GNU V3
# -----------------------

__version__ = "1.0"


"""
El módulo *tableWidget* permite mostrar datos del ADCP en una tabla (QTableWidget),
u ocultar las columnas de la tabla, eliminar filas, limpiar toda la tabla y copiar
datos de una fila o columna.
"""

# Versión Python: 3.6.9
# Versión PyQt5: 5.13.1

from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox)


# ============== CLASE tableWidget ================

class tableWidget(QDialog):
    def __init__(self, parent=None):
        super(tableWidget, self).__init__(parent)

        self.setWindowTitle("Gestor de Medición de Caudales")
        self.setWindowIcon(QIcon("ADCP.png"))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint | 
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(850, 400)

        self.initUI()

    def initUI(self):

        # =========== WIDGET QTableWidget ===========

        self.tabla = QTableWidget(self)

        # Deshabilitar edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setDragDropOverwriteMode(False)

        # Seleccionar toda la fila
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Seleccionar una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        # Especifíca dónde deben aparecer los puntos suspensivos "..." cuando
        # se muestran textos que no encajan
        self.tabla.setTextElideMode(Qt.ElideRight) #Qt.ElideNone

        # Establecer el ajuste de palabras del texto
        self.tabla.setWordWrap(False)

        # Deshabilitar clasificación
        self.tabla.setSortingEnabled(False)

        # Establecer el número de columnas
        self.tabla.setColumnCount(5)

        # Establecer el número de filas
        self.tabla.setRowCount(0)

        # Alineación del texto del encabezado
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)

        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setVisible(False)

        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tabla.horizontalHeader().setStretchLastSection(True)

        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)

        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)

        # Establecer alturas de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)

        # self.tabla.verticalHeader().setHightSections(True)

        nombreColumnas = ("Id", "Estación", "Aforo", "Fecha y hora", "N° de medición")

        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)

        # Menú contextual
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)

        # Establecer ancho de las columnas
        for indice, ancho in enumerate((80, 120, 120, 200), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(700, 300)
        self.tabla.move(20, 56)

        # =========== WIDGETS QPUSHBUTTON =============

        botonMostrarDatos = QPushButton("Mostrar mediciones", self)
        botonMostrarDatos.setFixedWidth(140)
        botonMostrarDatos.move(20, 20)

        menu = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, menu)
            accion.setCheckable(True)
            accion.setCheckable(True)
            accion.setData(indice)

            menu.addAction(accion)

        botonMostrarOcultar = QPushButton("Mostrar/ocultar campos", self)
        botonMostrarOcultar.setFixedWidth(180)
        botonMostrarOcultar.setMenu(menu)
        botonMostrarOcultar.move(170, 20)

        botonEliminarFila = QPushButton("Eliminar registro", self)
        botonEliminarFila.setFixedWidth(120)
        botonEliminarFila.move(510, 20)

        botonLimpiar = QPushButton("Limpiar", self)
        botonLimpiar.setFixedWidth(80)
        botonLimpiar.move(640, 20)

        botonCerrar = QPushButton("Cerrar", self)
        botonCerrar.setFixedWidth(80)
        botonCerrar.move(740, 306)

        # ================= EVENTOS ===============

        botonMostrarDatos.clicked.connect(self.datosTabla)
        botonEliminarFila.clicked.connect(self.eliminarFila)
        botonLimpiar.clicked.connect(self.limpiarTabla)
        botonCerrar.clicked.connect(self.close)

        self.tabla.itemDoubleClicked.connect(self.Comunidad)

        menu.triggered.connect(self.mostrarOcultar)

        # ============= FUNCIONES ====================

    def Comunidad(self, celda):
        QMessageBox.warning(self, "Mensaje", "Este es un software open-source en desarrollo."
                            "\nHiciste click en la celda: {}".format(celda.text()), QMessageBox.Ok)

    def datosTabla(self):
        datos = [("1", "Vicentelo", "Estático", "20/02/2020", "1era"),
                 ("2", "Vicentelo", "Dinámico", "20/02/2020", "----"),
                 ("3", "Menacho", "Estático", "21/02/2020", "1era"),
                 ("4", "Menacho", "Dinámico", "21/02/2020", "1era")]









        self.tabla.clearContents()

        row = 0
        for endian in datos:
            self.tabla.setRowCount(row + 1)

            idDato = QTableWidgetItem(endian[0])
            idDato.setTextAlignment(3)

            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla.setItem(row, 3, QTableWidgetItem(endian[3]))
            self.tabla.setItem(row, 4, QTableWidgetItem(endian[4]))

            row += 1

    def mostrarOcultar(self, accion):
        columna = accion.data()

        if accion.isChecked():
            self.tabla.setColumnHidden(columna, False)
        else:
            self.tabla.setColumnHidden(columna, True)

    def eliminarFila(self):
        filaSeleccionada = self.tabla.selectedItems()

        if filaSeleccionada:
            fila = filaSeleccionada[0].row()
            self.tabla.removeRow(fila)

            self.tabla.clearSelection()
        else:
            QMessageBox.critical(self, "Eliminar fila", "Selecione una fila.   ",
                                 QMessageBox.Ok)

    def limpiarTabla(self):
        self.tabla.clearContents()
        self.tabla.setRowCount(0)

    def menuContextual(self, posicion):
        indices = self.tabla.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)

            menu.addAction(QAction("Copiar todo", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            copiarIndividual = menu.addMenu("Copiar individual")
            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)

                copiarIndividual.addAction(accion)

            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)

            menu.exec_(self.tabla.viewport().mapToGlobal(posicion))

    def copiarTableWidgetItem(self, accion):
        filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]

        if accion.text() == "Copiar todo":
            filaSeleccionada = tuple(filaSeleccionada)
        else:
            filaSeleccionada = filaSeleccionada[accion.data()]

        print(filaSeleccionada)

        return
       

# ===============================

if __name__ == "__main__":

    import sys

    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    aplicacion.setFont(fuente)

    ventana = tableWidget()
    ventana.show()

    sys.exit(aplicacion.exec_())
