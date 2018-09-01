from res import signIn
import sys
from PyQt5 import QtWidgets, QtGui
from src import DB
import pipeline as pipe
import os
import re
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse

def getAccount():
    result = {}
    if os.path.exists('res/data.xml'):
        try:
            tree = parse("res/data.xml")
            data = tree.getroot()
            result['ip'] = data.findtext("ip")
            result['port'] = data.findtext("port")
            result['loginDB'] = data.findtext('loginDB')
            result['dataDB'] = data.findtext('dataDB')
        except:
            return None

    for val in result.values():
        if val is None: return None
    # port check
    if not result['port'].isdecimal(): result = None
    else: result['port'] = int(result['port'])

    # ip check
    if re.match('^(\d{1,4}.\d{1,4}.\d{1,4}.\d{1,4})$', result['ip']) is None: result = None

    return result

if __name__=='__main__':
	pipe.info = getAccount()
	pipe.app = QtWidgets.QApplication(sys.argv)
	pipe.app.setWindowIcon(QtGui.QIcon('res/icon.ico'))

	if pipe.info is None:
		errMsg = QtWidgets.QErrorMessage()
		errMsg.setFixedHeight(320)
		errMsg.setFixedWidth(480)
		errMsg.showMessage('res/data.xml이 없거나 data.xml 파일이 존재하지 않습니다.<br>'
						   '이 경우 res 폴더에 data.xml을 아래와 같은 방식으로 만들어주십시오.<br>'
						   '&lt;LoginData&gt;<br>'
						   '&nbsp;&nbsp;&nbsp;&nbsp;&lt;ip&gt;데이터베이스 서버 아이피&lt;/ip&gt;<br>'
						   '&nbsp;&nbsp;&nbsp;&nbsp;&lt;port&gt;포트&lt;/port&gt;<br>'
						   '&nbsp;&nbsp;&nbsp;&nbsp;&lt;loginDB&gt;관리자 아이디 테이블 이름&lt;/loginDB&gt;<br>'
						   '&nbsp;&nbsp;&nbsp;&nbsp;&lt;dataDB&gt;작업자 테이블 이름&lt;/dataDB&gt;<br>'
						   '&lt;/LoginData&gt;<br>')
	else:
		pipe.db = DB.DB(ip=pipe.info['ip'], port=pipe.info['port'], table=pipe.info['loginDB'])
		pipe.window = QtWidgets.QWidget()
		pipe.ui = signIn.Ui_Form()
		pipe.ui.setupUi(pipe.window)
		pipe.window.show()
	pipe.app.exec_()
