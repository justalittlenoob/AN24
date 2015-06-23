# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\FHR_20150504_edition2.0\_eric4project\ChkAN24_Run.ui'
#
# Created: Mon May 04 22:08:12 2015
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

class Ui_ChkAN24_Run(object):
    def setupUi(self, ChkAN24_Run):
        ChkAN24_Run.setObjectName(_fromUtf8("ChkAN24_Run"))
        ChkAN24_Run.setWindowModality(QtCore.Qt.NonModal)
        ChkAN24_Run.resize(328, 416)
        ChkAN24_Run.setModal(False)
        self.CheckPic = QtGui.QLabel(ChkAN24_Run)
        self.CheckPic.setGeometry(QtCore.QRect(20, 100, 271, 231))
        self.CheckPic.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/visual.png);\n"
"background-image: url(:/picture/imgs/monicaCheck.png);"))
        self.CheckPic.setObjectName(_fromUtf8("CheckPic"))
        self.Check = QtGui.QLabel(ChkAN24_Run)
        self.Check.setGeometry(QtCore.QRect(30, 350, 41, 41))
        self.Check.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check.setText(_fromUtf8(""))
        self.Check.setObjectName(_fromUtf8("Check"))
        self.Check_2 = QtGui.QLabel(ChkAN24_Run)
        self.Check_2.setGeometry(QtCore.QRect(90, 350, 41, 41))
        self.Check_2.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check_2.setText(_fromUtf8(""))
        self.Check_2.setObjectName(_fromUtf8("Check_2"))
        self.Check_3 = QtGui.QLabel(ChkAN24_Run)
        self.Check_3.setGeometry(QtCore.QRect(140, 350, 41, 41))
        self.Check_3.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check_3.setText(_fromUtf8(""))
        self.Check_3.setObjectName(_fromUtf8("Check_3"))
        self.Check_4 = QtGui.QLabel(ChkAN24_Run)
        self.Check_4.setGeometry(QtCore.QRect(190, 350, 41, 41))
        self.Check_4.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check_4.setText(_fromUtf8(""))
        self.Check_4.setObjectName(_fromUtf8("Check_4"))
        self.Check_5 = QtGui.QLabel(ChkAN24_Run)
        self.Check_5.setGeometry(QtCore.QRect(240, 350, 41, 41))
        self.Check_5.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/questionMark.png);\n"
"background-repeat:no-repeat;"))
        self.Check_5.setText(_fromUtf8(""))
        self.Check_5.setObjectName(_fromUtf8("Check_5"))
        self.label = QtGui.QLabel(ChkAN24_Run)
        self.label.setGeometry(QtCore.QRect(10, 20, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(ChkAN24_Run)
        QtCore.QMetaObject.connectSlotsByName(ChkAN24_Run)

    def retranslateUi(self, ChkAN24_Run):
        ChkAN24_Run.setWindowTitle(_translate("ChkAN24_Run", "Dialog", None))
        self.CheckPic.setText(_translate("ChkAN24_Run", "<html><head/><body><p><br/></p></body></html>", None))
        self.label.setText(_translate("ChkAN24_Run", "电极脱落，请重连电极。", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ChkAN24_Run = QtGui.QDialog()
    ui = Ui_ChkAN24_Run()
    ui.setupUi(ChkAN24_Run)
    ChkAN24_Run.show()
    sys.exit(app.exec_())

