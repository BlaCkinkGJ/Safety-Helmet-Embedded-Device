# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pipeline as pipe
import re
import hashlib
from res import signIn
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        pipe.db.changeCollection(pipe.info['loginDB'])
        Form.setObjectName("Form")
        Form.resize(288, 297)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 281))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.Email = QtWidgets.QLabel(self.groupBox)
        self.Email.setGeometry(QtCore.QRect(30, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.EmailText = QtWidgets.QLineEdit(self.groupBox)
        self.EmailText.setGeometry(QtCore.QRect(140, 60, 113, 21))
        self.EmailText.setObjectName("EmailText")
        self.UsernameText = QtWidgets.QLineEdit(self.groupBox)
        self.UsernameText.setGeometry(QtCore.QRect(140, 30, 113, 21))
        self.UsernameText.setObjectName("UsernameText")
        self.userName = QtWidgets.QLabel(self.groupBox)
        self.userName.setGeometry(QtCore.QRect(30, 30, 91, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        self.userName.setFont(font)
        self.userName.setObjectName("userName")
        self.FirstNameText = QtWidgets.QLineEdit(self.groupBox)
        self.FirstNameText.setGeometry(QtCore.QRect(140, 90, 113, 21))
        self.FirstNameText.setObjectName("FirstNameText")
        self.firstName = QtWidgets.QLabel(self.groupBox)
        self.firstName.setGeometry(QtCore.QRect(30, 90, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        self.firstName.setFont(font)
        self.firstName.setObjectName("firstName")
        self.LastNameText = QtWidgets.QLineEdit(self.groupBox)
        self.LastNameText.setGeometry(QtCore.QRect(140, 120, 113, 21))
        self.LastNameText.setObjectName("LastNameText")
        self.lastName = QtWidgets.QLabel(self.groupBox)
        self.lastName.setGeometry(QtCore.QRect(30, 120, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        self.lastName.setFont(font)
        self.lastName.setObjectName("lastName")
        self.PasswordText = QtWidgets.QLineEdit(self.groupBox)
        self.PasswordText.setGeometry(QtCore.QRect(140, 150, 113, 21))
        self.PasswordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordText.setObjectName("PasswordText")
        self.password = QtWidgets.QLabel(self.groupBox)
        self.password.setGeometry(QtCore.QRect(30, 150, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.PasswordchkText = QtWidgets.QLineEdit(self.groupBox)
        self.PasswordchkText.setGeometry(QtCore.QRect(140, 180, 113, 21))
        self.PasswordchkText.setObjectName("PasswordchkText")
        self.PasswordchkText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordCHK = QtWidgets.QLabel(self.groupBox)
        self.passwordCHK.setGeometry(QtCore.QRect(30, 180, 111, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(10)
        self.passwordCHK.setFont(font)
        self.passwordCHK.setObjectName("passwordCHK")
        self.ChkLabel = QtWidgets.QLabel(self.groupBox)
        self.ChkLabel.setGeometry(QtCore.QRect(30, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(7)
        self.ChkLabel.setFont(font)
        self.ChkLabel.setObjectName("ChkLabel")
        self.submit = QtWidgets.QPushButton(self.groupBox)
        self.submit.setGeometry(QtCore.QRect(100, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.UsernameText, self.EmailText)
        Form.setTabOrder(self.EmailText, self.FirstNameText)
        Form.setTabOrder(self.FirstNameText, self.LastNameText)
        Form.setTabOrder(self.LastNameText, self.PasswordText)
        Form.setTabOrder(self.PasswordText, self.PasswordchkText)
        Form.setTabOrder(self.PasswordchkText, self.submit)

        self.submit.clicked.connect(self.submitButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "작업자 통합 관리 시스템"))
        self.groupBox.setTitle(_translate("Form", "Registration"))
        self.Email.setText(_translate("Form", "E-mail"))
        self.userName.setText(_translate("Form", "Username"))
        self.firstName.setText(_translate("Form", "First Name"))
        self.lastName.setText(_translate("Form", "Last Name"))
        self.password.setText(_translate("Form", "Password"))
        self.passwordCHK.setText(_translate("Form", "Password"))
        self.ChkLabel.setText(_translate("Form", "( Check again )"))
        self.submit.setText(_translate("Form", "Submit"))


    def msgbox(self, title, content):
        return QMessageBox.question(pipe.window, title, content, QMessageBox.Yes, QMessageBox.Yes)

    def errorCheck(self, data):
        emailRegex = '[^@]+@[^@]+\.[^@]+'

        if re.match(emailRegex, data['email']) is None:
            self.msgbox('이메일 형 불일치', '이메일 형식이 불일치합니다.')
            return True

        if data['password'] != self.PasswordchkText.text():
            self.msgbox('비밀번호 불일치', '비밀번호가 불일치합니다.')
            return True

        for value in data.values():
            if len(value) == 0:
                self.msgbox('입력 오류', '빈 칸을 가진 필드가 존재합니다.')
                return True

        isExist = (pipe.db.collection.find_one({'email': data['email']}) is not None) \
                  or (pipe.db.collection.find_one({'username': data['username']}) is not None)

        if isExist:
            self.msgbox('계정 오류', '이미 있는 계정입니다.')
            return True
        return False

    def pushDatabase(self, data):
        data['password'] = hashlib.sha256(data['password'].encode()).hexdigest()
        pipe.db.collection.insert(data)
        return self.msgbox('등록 성공', '계정이 정상적으로 데이터베이스에 등록되었습니다.')

    def submitButton(self):
        data = {}
        data['username'] = self.UsernameText.text()
        data['email'] = self.EmailText.text()
        data['firstName'] = self.FirstNameText.text()
        data['lastName'] = self.LastNameText.text()
        data['password'] = self.PasswordText.text()

        if self.errorCheck(data) : return

        if self.pushDatabase(data) == QMessageBox.Yes:
            temp = pipe.window
            pipe.window = QtWidgets.QWidget()
            pipe.ui = signIn.Ui_Form()
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

