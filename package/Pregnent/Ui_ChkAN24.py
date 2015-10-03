# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\FHR_20150427_edition2.0\_eric4project\ChkAN24.ui'
#
# Created: Mon Apr 27 16:16:26 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ChkAN24(object):
    def setupUi(self, ChkAN24):
        ChkAN24.setObjectName(_fromUtf8("ChkAN24"))
        ChkAN24.setWindowModality(QtCore.Qt.NonModal)
        ChkAN24.resize(460, 332)
        ChkAN24.setModal(True)
        self.CheckPic = QtGui.QLabel(ChkAN24)
        self.CheckPic.setGeometry(QtCore.QRect(20, 30, 271, 231))
        self.CheckPic.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/visual.png);\n"
"background-image: url(:/picture/imgs/monicaCheck.png);"))
        self.CheckPic.setObjectName(_fromUtf8("CheckPic"))
        self.Check = QtGui.QLabel(ChkAN24)
        self.Check.setGeometry(QtCore.QRect(30, 280, 41, 41))
        self.Check.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check.setText(_fromUtf8(""))
        self.Check.setObjectName(_fromUtf8("Check"))
        self.Check_2 = QtGui.QLabel(ChkAN24)
        self.Check_2.setGeometry(QtCore.QRect(90, 280, 41, 41))
        self.Check_2.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check_2.setText(_fromUtf8(""))
        self.Check_2.setObjectName(_fromUtf8("Check_2"))
        self.Check_3 = QtGui.QLabel(ChkAN24)
        self.Check_3.setGeometry(QtCore.QRect(140, 280, 41, 41))
        self.Check_3.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check_3.setText(_fromUtf8(""))
        self.Check_3.setObjectName(_fromUtf8("Check_3"))
        self.Check_4 = QtGui.QLabel(ChkAN24)
        self.Check_4.setGeometry(QtCore.QRect(190, 280, 41, 41))
        self.Check_4.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check_4.setText(_fromUtf8(""))
        self.Check_4.setObjectName(_fromUtf8("Check_4"))
        self.Check_5 = QtGui.QLabel(ChkAN24)
        self.Check_5.setGeometry(QtCore.QRect(240, 280, 41, 41))
        self.Check_5.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check_5.setText(_fromUtf8(""))
        self.Check_5.setObjectName(_fromUtf8("Check_5"))
        self.ButtonCheck = QtGui.QPushButton(ChkAN24)
        self.ButtonCheck.setGeometry(QtCore.QRect(350, 100, 91, 31))
        self.ButtonCheck.setObjectName(_fromUtf8("ButtonCheck"))
        self.ButtonStart = QtGui.QPushButton(ChkAN24)
        self.ButtonStart.setEnabled(False)
        self.ButtonStart.setGeometry(QtCore.QRect(350, 160, 91, 31))
        self.ButtonStart.setObjectName(_fromUtf8("ButtonStart"))

        self.retranslateUi(ChkAN24)
        QtCore.QObject.connect(ChkAN24, QtCore.SIGNAL(_fromUtf8("destroyed()")), self.Check_2.show)
        QtCore.QMetaObject.connectSlotsByName(ChkAN24)

    def retranslateUi(self, ChkAN24):
        ChkAN24.setWindowTitle(_translate("ChkAN24", "Dialog", None))
        self.CheckPic.setText(_translate("ChkAN24", "<html><head/><body><p><br/></p></body></html>", None))
        self.ButtonCheck.setText(_translate("ChkAN24", "检查电极", None))
        self.ButtonStart.setText(_translate("ChkAN24", "开始检测", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ChkAN24 = QtGui.QDialog()
    ui = Ui_ChkAN24()
    ui.setupUi(ChkAN24)
    ChkAN24.show()
    sys.exit(app.exec_())

