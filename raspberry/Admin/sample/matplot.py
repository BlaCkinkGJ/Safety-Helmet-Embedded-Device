
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QTabWidget, QBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pymongo import MongoClient

client = MongoClient('34.214.27.59:27017')
db = client.SFSH
col = db.employees

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setLayout(self.layout)

    def initUI(self):

        self.pushButton = QPushButton("DRAW Graph")
        self.pushButton.clicked.connect(self.btnClicked)

        self.fig = []
        self.canvas = []
        btnLayout = []
        for i in range(4):
            self.fig.append(plt.Figure())
            self.canvas.append(FigureCanvas(self.fig[i]))
            if i % 2  == 0:
                btnLayout.append(QVBoxLayout())
            btnLayout[i//2].addWidget(self.canvas[i])
            btnLayout[i//2].addWidget(self.canvas[i])

        # canvas Layout
        canvasLayout = QVBoxLayout()
        canvasLayout.addWidget(self.pushButton)
        canvasLayout.addStretch(1)

        self.layout = QHBoxLayout()
        for i in range(2):
            self.layout.addLayout(btnLayout[i])
        self.layout.addLayout(canvasLayout)

    def btnClicked(self):
        self.draw_graph(0, {"connected": '1'})
        self.draw_graph(1, {"WiFi": 'zeus7000-2'})
        self.draw_graph(2, {"sleep": True})
        self.draw_graph(3, {"temper": {"$gte" : 11}})

    def draw_graph(self, i, query):
        global col
        connect_size = 0

        length = 0

        for post in col.find():
            length += 1

        for post in col.find(query):
            connect_size += 100 / length

        ax = self.fig[i].subplots()

        # 'Connect' Pie chart
        colors = ['#99ff99', '#fccc99']
        sizes = [connect_size, 100 - connect_size]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        ax.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        self.canvas[i].draw()

class Form(QWidget):
    def __init__(self):
        super().__init__(flags=Qt.Widget)
        self.tbw = QTabWidget()
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Tab Widget")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        self.setGeometry(300,300,800,600)

        form_lbx.addWidget(self.tbw)

        self.tbw.addTab(MyWindow(), MyWindow.__name__)
        self.tbw.addTab(QTextEdit(), QTextEdit.__name__)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    app.exec_()
