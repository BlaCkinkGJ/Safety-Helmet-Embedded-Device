import DB
import pandas as pd
import copy
import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot, Qt, QTimer


db = DB.DB(ip='34.214.27.59', port=27017)

db.changeCollection('employees')
data = copy.deepcopy(db.collection.find())

dict = {}

for key in data[0].keys():
    dict[key] = []

for temp in data:
    for key, val in temp.items():
        dict[key].append(val)

df = pd.DataFrame(data=dict)


class TableWidget(QTableWidget):
    def __init__(self, df, parent=None):
        QTableWidget.__init__(self, parent)
        self.df = df
        nRows = len(self.df.index)
        nColumns = len(self.df.columns)
        self.setRowCount(nRows)
        self.setColumnCount(nColumns)

        self.setHorizontalHeaderLabels(self.df.keys())

        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                x = self.df.iloc[i, j]
                self.setItem(i, j, QTableWidgetItem(str(x)))

        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.cellChanged.connect(self.onCellChanged)

    @pyqtSlot(int, int)
    def onCellChanged(self, row, column):
        text = self.item(row, column).text()
        self.df.set_value(row, column, text)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global df
        self.setGeometry(700, 100, 350, 380)
        self.tableWidget = TableWidget(df, self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.button = QPushButton('Print DataFrame', self)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.print_my_df)

    @pyqtSlot()
    def print_my_df(self):
        print(self.tableWidget.df)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())