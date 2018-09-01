# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signIn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from res import signUp, status
import pipeline as pipe
from PyQt5.QtWidgets import QMessageBox as msgbox

class Ui_Form(object):
    def setupUi(self, Form):
        pipe.db.changeCollection(pipe.info['loginDB'])
        Form.setObjectName("Form")
        Form.resize(338, 277)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.frame_8 = QtWidgets.QFrame(Form)
        self.frame_8.setGeometry(QtCore.QRect(10, 10, 321, 261))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setLineWidth(19)
        self.frame_8.setMidLineWidth(0)
        self.frame_8.setObjectName("frame_8")
        self.MainLabel = QtWidgets.QLabel(self.frame_8)
        self.MainLabel.setGeometry(QtCore.QRect(30, 10, 261, 51))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MainLabel.setFont(font)
        self.MainLabel.setTextFormat(QtCore.Qt.PlainText)
        self.MainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabel.setObjectName("MainLabel")
        self.LogInBox = QtWidgets.QGroupBox(self.frame_8)
        self.LogInBox.setGeometry(QtCore.QRect(10, 70, 301, 181))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setBold(True)
        font.setWeight(75)
        self.LogInBox.setFont(font)
        self.LogInBox.setObjectName("LogInBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.LogInBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 120, 202, 34))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.Button = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.Button.setContentsMargins(0, 0, 0, 0)
        self.Button.setObjectName("Button")
        self.SignIn = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SignIn.setFont(font)
        self.SignIn.setObjectName("SignIn")
        self.Button.addWidget(self.SignIn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Button.addItem(spacerItem)
        self.SignUp = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SignUp.setFont(font)
        self.SignUp.setObjectName("SignUp")
        self.Button.addWidget(self.SignUp)
        self.Password = QtWidgets.QLabel(self.LogInBox)
        self.Password.setGeometry(QtCore.QRect(30, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.PasswordText = QtWidgets.QLineEdit(self.LogInBox)
        self.PasswordText.setGeometry(QtCore.QRect(140, 80, 113, 21))
        self.PasswordText.setObjectName("PasswordText")
        self.PasswordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.UsernameText = QtWidgets.QLineEdit(self.LogInBox)
        self.UsernameText.setGeometry(QtCore.QRect(140, 40, 113, 21))
        self.UsernameText.setObjectName("UsernameText")
        self.Username = QtWidgets.QLabel(self.LogInBox)
        self.Username.setGeometry(QtCore.QRect(30, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.UsernameText, self.PasswordText)
        Form.setTabOrder(self.PasswordText, self.SignIn)
        Form.setTabOrder(self.SignIn, self.SignUp)

        self.SignIn.clicked.connect(self.signInButton)
        self.SignUp.clicked.connect(self.signUpButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "작업자 통합 관리 시스템"))
        self.MainLabel.setText(_translate("Form", "작업자 통합 관리시스템"))
        self.LogInBox.setTitle(_translate("Form", "Log-in"))
        self.SignIn.setText(_translate("Form", "Sign In"))
        self.SignUp.setText(_translate("Form", "Sign Up"))
        self.Password.setText(_translate("Form", "Password"))
        self.Username.setText(_translate("Form", "Username"))

    def signInButton(self):
        import hashlib
        username = self.UsernameText.text()
        password = self.PasswordText.text()

        password = hashlib.sha256(password.encode()).hexdigest()

        isExist = pipe.db.collection.find_one({'username': username, 'password': password}) is not None
        if isExist:
            temp = pipe.window
            pipe.window = QtWidgets.QWidget()
            pipe.ui = status.Ui_Form()
            pipe.ui.setupUi(pipe.window)
            pipe.window.show()
            temp.close()
        else:
            msgbox.question(pipe.window, '로그인 실패', '계정을 찾을 수 없습니다.', msgbox.Yes, msgbox.Yes)


    def signUpButton(self):
        temp = pipe.window
        pipe.window = QtWidgets.QWidget()
        pipe.ui = signUp.Ui_Form()
        pipe.ui.setupUi(pipe.window)
        pipe.window.show()
        temp.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

