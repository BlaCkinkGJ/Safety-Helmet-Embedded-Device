from src import DB
import pandas as pd
import sys
import time
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import pyqtSlot, QTimer

field = {
   '_id': 0,
    'connected': 1,
    'temper': 2,
    'name': 3,
    'sleep': 4,
    'WiFi': 5,
    'Time': 6
}
db = DB.DB(ip='34.214.27.59', port=27017)

db.changeCollection('employees')

df = None


def getData():
    global df
    data = db.collection.find()

    dict = {}

    for key in data[0].keys():
        dict[key] = []

    for temp in data:
        for key, val in temp.items():
            dict[key].append(val)

    df = pd.DataFrame(data=dict)


def isFloat(element):
    if type(element) == str and re.match("^\d+?\.\d+?$", element) is None:
        return False
    else:
        return True


def statusCheck(row, col, data = ""):
    result = False
    if col == field['_id']: pass
    elif col == field['connected']:
        if data == '0':
            result = True
    elif col == field['temper']: pass
    elif col == field['name']: pass
    elif col == field['sleep']:
        if data == 'True':
            result = True
    elif col == field['WiFi']: pass
    elif col == field['Time']:
        if isFloat(data) or data.isdecimal():
            if time.time() - float(data) > 5.0:
                result = True
    else: print("Invalid Value Occur")
    return result


class TableWidget(QTableWidget):
    def __init__(self, df, parent=None):
        QTableWidget.__init__(self, parent)
        getData()
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
                if statusCheck(i, j, str(x)):
                    self.item(i, j).setBackground(QColor(255, 0, 0))

        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global df
        self.setGeometry(700, 100, 800, 600)
        self.tableWidget = TableWidget(df, self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.button = QPushButton('Print DataFrame', self)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.print_my_df)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.print_my_df)
        self.timer.start(1500)

    @pyqtSlot()
    def print_my_df(self):
        getData()
        self.tableWidget.df = df
        nRows = len(self.tableWidget.df.index)
        nColumns = len(self.tableWidget.df.columns)
        self.tableWidget.setRowCount(nRows)
        self.tableWidget.setColumnCount(nColumns)

        self.tableWidget.setHorizontalHeaderLabels(self.tableWidget.df.keys())

        # check the all table
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                x = self.tableWidget.df.iloc[i, j]
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(x)))
                if statusCheck(i, j, str(x)):
                    self.tableWidget.item(i, j).setBackground(QColor(255, 0, 0))

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


if __name__ == '__main__':
    getData()
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())