# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pipeline as pipe
import pandas as pd
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def isFloat(element):
    if type(element) == str and re.match("^\d+?\.\d+?$", element) is None:
        return False
    else:
        return True

class Graph(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setLayout(self.layout)

    def initUI(self):

        mpl.rcParams['font.size'] = 8.0
        mpl.rcParams['font.family'] = 'NanumGothic'
        self.fig = []
        self.canvas = []
        btnLayout = []
        for i in range(4):
            self.fig.append(plt.Figure())
            self.canvas.append(FigureCanvas(self.fig[i]))
            if i % 2  == 0:
                btnLayout.append(QVBoxLayout())
            btnLayout[i//2].addWidget(self.canvas[i])

        self.layout = QHBoxLayout()
        for i in range(2):
            self.layout.addLayout(btnLayout[i])
        self.value = 10

    def drawGraph(self, idx, data):
        title = ['턱끈 연결 현황', '졸음 현황', '통신 연결 현황', '온도 상태']
        self.fig[idx].clear()
        ax = self.fig[idx].subplots()

        # 'Connect' Pie chart
        sizes, labels = self.dataProcessing(idx, data)
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        ax.pie(sizes, autopct='%1.1f%%')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.legend(title=title[idx], labels=labels)
        self.canvas[idx].draw()

    def dataProcessing(self,idx, data):
        index = {
            'connected': 0,
            'sleep': 1,
            'time': 2,
            'temperature': 3
        }
        MAX_TIME = 5.0
        boundTime = {
            'gt' : 30.0,
            'lt' : 0.0
        }
        sizes, labels = None, None
        if idx == index['connected']:
            sizes = data
            labels = ['connect', 'disconnect']
        elif idx == index['sleep']:
            sizes = data
            labels = ['sleep', 'not sleep']
        elif idx == index['time']:
            sizes = [0, 0]
            for T in data.values:
                if time.time() - float(T) < MAX_TIME:
                    sizes[0] += 1 # connect
                else:
                    sizes[1] += 1 # disconnect
            labels = ['connect', 'disconnect']
        elif idx == index['temperature']:
            sizes = [0, 0]
            for T in data.values:
                if boundTime['lt'] < float(T) <= boundTime['gt']:
                    sizes[0] += 1 # NORMAL
                else:
                    sizes[1] += 1 # DANGER
            labels = ['normal', 'danger']

        return sizes, labels

class Ui_Form(object):
    def setupUi(self, Form):
        pipe.db.changeCollection('employees')
        Form.setObjectName("Form")
        Form.resize(921, 610)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 891, 581))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.workerTab = QtWidgets.QTabWidget(self.groupBox)
        self.workerTab.setGeometry(QtCore.QRect(210, 40, 661, 531))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        self.workerTab.setFont(font)
        self.workerTab.setAutoFillBackground(True)
        self.workerTab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.workerTab.setTabBarAutoHide(True)
        self.workerTab.setObjectName("workerTab")
        self.List = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setKerning(True)
        self.List.setFont(font)
        self.List.setObjectName("List")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.List)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableTitle = QtWidgets.QLabel(self.List)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 ExtraBold")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.tableTitle.setFont(font)
        self.tableTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.tableTitle.setObjectName("tableTitle")
        self.verticalLayout.addWidget(self.tableTitle)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.List)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.workerTab.addTab(self.List, "")
        '''
        self.Status = QtWidgets.QWidget()
        self.Status.setObjectName("Status")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Status)
        self.gridLayout_3.setObjectName("gridLayout_3")
        '''
        self.graph = Graph()
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        self.graph.setFont(font)
        self.workerTab.addTab(self.graph, "")
        self.searchTitle = QtWidgets.QLabel(self.groupBox)
        self.searchTitle.setGeometry(QtCore.QRect(20, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.searchTitle.setFont(font)
        self.searchTitle.setObjectName("searchTitle")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 180, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.searchButton = QtWidgets.QPushButton(self.groupBox)
        self.searchButton.setGeometry(QtCore.QRect(20, 210, 61, 21))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.exportButton = QtWidgets.QPushButton(self.groupBox)
        self.exportButton.setGeometry(QtCore.QRect(20, 280, 61, 21))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        self.exportButton.setFont(font)
        self.exportButton.setObjectName("exportButton")
        self.excelTitle = QtWidgets.QLabel(self.groupBox)
        self.excelTitle.setGeometry(QtCore.QRect(20, 240, 131, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.excelTitle.setFont(font)
        self.excelTitle.setObjectName("excelTitle")
        self.ListBox = QtWidgets.QComboBox(self.groupBox)
        self.ListBox.setGeometry(QtCore.QRect(60, 150, 101, 21))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        self.ListBox.setFont(font)
        self.ListBox.setObjectName("ListBox")
        self.ListBox.addItem("")
        self.ListBox.addItem("")
        self.ListBox.addItem("")
        self.ListBox.addItem("")
        self.ListBox.addItem("")
        self.ListBox.addItem("")
        self.ListBox.addItem("")
        self.method = QtWidgets.QLabel(self.groupBox)
        self.method.setGeometry(QtCore.QRect(20, 140, 41, 41))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.method.setFont(font)
        self.method.setObjectName("method")
        self.Logo = QtWidgets.QLabel(self.groupBox)
        self.Logo.setGeometry(QtCore.QRect(20, 20, 161, 91))
        self.Logo.setText("")
        self.Logo.setTextFormat(QtCore.Qt.RichText)
        self.Logo.setPixmap(QtGui.QPixmap(":/logoIMG/logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")

        self.retranslateUi(Form)
        self.workerTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.ListBox, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.searchButton)
        Form.setTabOrder(self.searchButton, self.exportButton)
        Form.setTabOrder(self.exportButton, self.workerTab)
        Form.setTabOrder(self.workerTab, self.tableWidget)

        self.databaseTimer = QtCore.QTimer(Form)
        self.databaseTimer.timeout.connect(self.getDataFromDatabase)
        self.databaseTimer.start(1500)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Status"))
        self.tableTitle.setText(_translate("Form", "전체 작업자 상태"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "직원번호"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "이름"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "온도"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "연결 상태"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "졸음 상태"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "연결 위치"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "마지막 접속 시간"))
        self.workerTab.setTabText(self.workerTab.indexOf(self.List), _translate("Form", "Workers List"))
        self.workerTab.setTabText(self.workerTab.indexOf(self.graph), _translate("Form", "Workers Status"))
        self.searchTitle.setText(_translate("Form", "작업자 검색"))
        self.searchButton.setText(_translate("Form", "Search"))
        self.exportButton.setText(_translate("Form", "Export"))
        self.excelTitle.setText(_translate("Form", "엑셀 출력"))
        self.ListBox.setItemText(0, _translate("Form", "직원번호"))
        self.ListBox.setItemText(1, _translate("Form", "이름"))
        self.ListBox.setItemText(2, _translate("Form", "온도"))
        self.ListBox.setItemText(3, _translate("Form", "연결 상태"))
        self.ListBox.setItemText(4, _translate("Form", "졸음 상태"))
        self.ListBox.setItemText(5, _translate("Form", "연결 위치"))
        self.ListBox.setItemText(6, _translate("Form", "접속 시간"))
        self.method.setText(_translate("Form", "방  법"))

    def getDataFromDatabase(self):
        data = pipe.db.collection.find()
        dict = {}
        for key in data[0].keys():
            dict[key] = []
        for row in data:
            for key, val in row.items():
                dict[key].append(val)
        self.df = pd.DataFrame(data=dict)
        self.getAllData()
        self.drawGraph()

    def drawGraph(self):
        index = {
            'connected': 0,
            'sleep' : 1,
            'time' : 2,
            'temperature' : 3
        }
        self.graph.drawGraph(index['connected'], self.df['connected'].value_counts())
        self.graph.drawGraph(index['sleep'], self.df['sleep'].value_counts())
        self.graph.drawGraph(index['time'], self.df['Time'])
        self.graph.drawGraph(index['temperature'], self.df['temper'])

    def getAllData(self):
        index = {
            '_id': 0,
            'connected': 3,
            'temper': 2,
            'name': 1,
            'sleep': 4,
            'WiFi': 5,
            'Time': 6
        }
        self.tableWidget.setRowCount(len(self.df.index))
        self.tableWidget.setColumnCount(len(self.df.columns))

        for key, content in self.df.items():
            col = index[key]
            for row, val in enumerate(content):
                raw = val # time을 재변환 하는 것 보단 변수를 하나 더 사용하는 것이 이득이라 판단.
                if key == 'Time':
                    val = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(val)))
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(val)))
                if self.statusCheck(row, col, str(raw)):
                    self.tableWidget.item(row, col).setBackground(QtGui.QColor(255, 0, 0))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def statusCheck(self, row, col, data = ""):
        field = {
            '_id': 0,
            'connected': 3,
            'temper': 2,
            'name': 1,
            'sleep': 4,
            'WiFi': 5,
            'Time': 6
        }
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

from res import LOGO_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
