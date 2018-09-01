import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pymongo
from pymongo import MongoClient
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
import copy

# 불러올 ui파일
form_class1 = uic.loadUiType("Sign_in.ui")[0]
form_class2 = uic.loadUiType("Sign_up.ui")[0]
form_class3 = uic.loadUiType("Status.ui")[0]

# 데이터베이스 구축 (accounts db)
client = MongoClient("mongodb://34.214.27.59:27017/")
db1     = client.accounts
col1     = db1.users

# 데이터서버 구축 (SFSH db)
db2      = client.SFSH
col2     = db2.employees

safe    = {"temper": {"$gte": 11, "$lte": 30}}  # 11 ~ 30

caution = {
            "lower": {"temper": {"$gte": 1, "$lte": 11}},  # 1 ~ 10
            "higher": {"temper": {"$gt": 30, "$lte": 40}}
          }

danger = {
            "lower": {"temper": {"$gt": 40}},
            "higher": {"temper": {"$lte": 0}}
         }

label1 = 'connect', 'disconnect'
label2 = 'awake', 'sleep'
label3 = 'in WiFi', 'Out of WiFi'
label4 = 'safe', 'caution', 'danger'


class MainPage(QWidget, form_class1):  # 계정 등록 페이지
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_signIn)
        self.pushButton_2.clicked.connect(self.btn_signUp)

    def btn_signIn(self):
        uname = self.lineEdit_2.text()
        pwd   = self.lineEdit_3.text()

        count = 0
        for val in col1.find():
            if val['uname'] == uname and val['pwd'] == pwd:
                form.show()
                main.close()
            else:
                count += 1

        if count == col1.count():
            ans = QMessageBox.question(self, "로그인 실패", "아이디 또는 비밀번호가 틀렸습니다.",
                                  QMessageBox.Yes, QMessageBox.Yes)
            if ans == QMessageBox.Yes:
                main.show()

    def btn_signUp(self):
        sign_up.show()
        main.close()


class Sign_up(QWidget, form_class2):  # 계정 등록 페이지

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.submit_Button)

    def submit_Button(self):
        data = {}

        data['uname']     = self.lineEdit_2.text()
        data['email']     = self.lineEdit_3.text()
        data['firstName'] = self.lineEdit_4.text()
        data['lastName']  = self.lineEdit_5.text()
        data['pwd']       = self.lineEdit_6.text()
        data['repwd']     = self.lineEdit_7.text()

        empty_count = 0  # 빈칸의 개수

        for var in data.values():
            if len(var) == 0:
                empty_count += 1

        if empty_count != 0:
             QMessageBox.question(self, "등록 실패", "빈칸이 존재합니다",
                                  QMessageBox.Yes, QMessageBox.Yes)
        elif data['pwd'] != data['repwd']:
            QMessageBox.question(self, "입력 오류", "잘못 입력하셨습니다",
                                 QMessageBox.Yes, QMessageBox.Yes)
        else:
            col1.insert_one(data)
            ans = QMessageBox.question(self, "등록 성공", "당신의 계정이 데이터베이스에 등록되었습니다",
                                 QMessageBox.Yes, QMessageBox.Yes)

            if ans == QMessageBox.Yes:
                main.show()
                sign_up.close()


class Status(QWidget, form_class3):  # 실제 데이터 결과 페이지
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setLayout(self.layout)

    def initUI(self):

        self.pushButton = QPushButton("Check Status")
        self.pushButton.clicked.connect(self.btnClicked)

        self.fig = []
        self.canvas = []
        btnLayout = []
        for i in range(4):
            self.fig.append(plt.Figure(figsize=(3, 3), dpi = 100))
            self.canvas.append(FigureCanvas(self.fig[i]))
            if i % 2 == 0:
                btnLayout.append(QVBoxLayout())
            btnLayout[i // 2].addWidget(self.canvas[i])
            btnLayout[i // 2].addWidget(self.canvas[i])

        # canvas Layout
        canvasLayout = QVBoxLayout()
        canvasLayout.addWidget(self.pushButton)
        canvasLayout.addStretch(1)

        self.layout = QHBoxLayout()
        for i in range(2):
            self.layout.addLayout(btnLayout[i])
        self.layout.addLayout(canvasLayout)

    def btnClicked(self):

        self.draw_graph(0, {"connected": '1'}, label1)
        self.draw_graph(1, {"WiFi": 'zeus7000-2'}, label2)
        self.draw_graph(2, {"sleep": True}, label3)
        self.draw_graph(3,  {
            "safe": copy.deepcopy(safe),
            "caution": copy.deepcopy(caution),
            "danger": copy.deepcopy(danger)
        }, label4)

    def draw_graph(self, i, query, labels):
        length = col2.count()

        if i != 3:
            connect_size = 0

            for post in col2.find(query):
                connect_size += 100 / length
            ax = self.fig[i].subplots()

            colors = ['#99ff99', '#fccc99']
            sizes = [connect_size, 100 - connect_size]
            explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

            ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            self.canvas[i].draw()
        else:

            ax = self.fig[i].subplots()

            safe_size = 5
            caution_size = 0
            danger_size = 0

            for post in col2.find(query['safe']):
                safe_size += 100 / length

            for post in col2.find(query['caution']['lower']):
                caution_size += 100 / length

            for post in col2.find(query['caution']['higher']):
                caution_size += 100 / length

            for post in col2.find(query['danger']['lower']):
                danger_size += 100 / length

            for post in col2.find(query['danger']['higher']):
                danger_size += 100 / length

            sizes = [safe_size, caution_size, danger_size]
            colors = ['#99ff99', '#fccc99', '#fc9999']
            explode = (0, 0.1, 0)

            ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            self.canvas[i].draw()


class Form(QWidget):
    def __init__(self):
        super().__init__(flags=Qt.Widget)
        self.tbw = QTabWidget()

        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Worker Page")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        self.setGeometry(300, 300, 800, 600)

        form_lbx.addWidget(self.tbw)

        self.tbw.addTab(QTextEdit(), QTextEdit.__name__)
        self.tbw.addTab(Status(), Status.__name__)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainPage()
    main.show()
    sign_up = Sign_up()
    status = Status()
    form = Form()

    app.exec_()

