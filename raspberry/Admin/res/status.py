# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pipeline as pipe
import pandas as pd


class Ui_Form(object):
    def setupUi(self, Form):
        self.dataFrame = {}
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
        self.Status = QtWidgets.QWidget()
        self.Status.setObjectName("Status")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Status)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.workerTab.addTab(self.Status, "")
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
        self.workerTab.setTabText(self.workerTab.indexOf(self.Status), _translate("Form", "Workers Status"))
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

        for (key, content) in self.df.items():
            for row, val in enumerate(content):
                self.tableWidget.setItem(row, index[key], QtWidgets.QTableWidgetItem(str(val)))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


from res import LOGO_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
