from res import signIn
import sys
from PyQt5 import QtWidgets
from src import DB
import pipeline as pipe


if __name__ == "__main__":
    pipe.db = DB.DB(ip='34.214.27.59', port=27017, table='admin')
    pipe.app = QtWidgets.QApplication(sys.argv)
    pipe.window = QtWidgets.QWidget()
    pipe.ui = signIn.Ui_Form()
    pipe.ui.setupUi(pipe.window)
    pipe.window.show()
    # sys exit 사용시 DB에 치명적인 문제가 발생함
    pipe.app.exec_()
