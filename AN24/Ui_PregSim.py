# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\FHR 20150318\_eric4project\PregSim.ui'
#
# Created: Wed Mar 18 20:23:22 2015
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

class Ui_PregSim(object):
    def setupUi(self, PregSim):
        PregSim.setObjectName(_fromUtf8("PregSim"))
        PregSim.resize(416, 587)
        PregSim.setModal(False)
        self.MoBeatmin = QtGui.QLabel(PregSim)
        self.MoBeatmin.setGeometry(QtCore.QRect(210, 140, 158, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        self.MoBeatmin.setFont(font)
        self.MoBeatmin.setObjectName(_fromUtf8("MoBeatmin"))
        self.ChHr = QtGui.QLabel(PregSim)
        self.ChHr.setGeometry(QtCore.QRect(210, 190, 158, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        self.ChHr.setFont(font)
        self.ChHr.setObjectName(_fromUtf8("ChHr"))
        self.MoHr = QtGui.QLabel(PregSim)
        self.MoHr.setGeometry(QtCore.QRect(210, 70, 158, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        self.MoHr.setFont(font)
        self.MoHr.setObjectName(_fromUtf8("MoHr"))
        self.ChHrNum = QtGui.QLabel(PregSim)
        self.ChHrNum.setGeometry(QtCore.QRect(40, 200, 141, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.ChHrNum.setFont(font)
        self.ChHrNum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ChHrNum.setObjectName(_fromUtf8("ChHrNum"))
        self.RunTimeNum = QtGui.QLabel(PregSim)
        self.RunTimeNum.setGeometry(QtCore.QRect(300, 520, 84, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        self.RunTimeNum.setFont(font)
        self.RunTimeNum.setObjectName(_fromUtf8("RunTimeNum"))
        self.ChBeatmin = QtGui.QLabel(PregSim)
        self.ChBeatmin.setGeometry(QtCore.QRect(210, 260, 158, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        self.ChBeatmin.setFont(font)
        self.ChBeatmin.setObjectName(_fromUtf8("ChBeatmin"))
        self.MoMov = QtGui.QLabel(PregSim)
        self.MoMov.setGeometry(QtCore.QRect(30, 460, 281, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        self.MoMov.setFont(font)
        self.MoMov.setObjectName(_fromUtf8("MoMov"))
        self.MoHrNum = QtGui.QLabel(PregSim)
        self.MoHrNum.setGeometry(QtCore.QRect(30, 80, 151, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.MoHrNum.setFont(font)
        self.MoHrNum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MoHrNum.setObjectName(_fromUtf8("MoHrNum"))
        self.pushButton = QtGui.QPushButton(PregSim)
        self.pushButton.setGeometry(QtCore.QRect(30, 520, 151, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.RunTime = QtGui.QLabel(PregSim)
        self.RunTime.setGeometry(QtCore.QRect(210, 520, 91, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        self.RunTime.setFont(font)
        self.RunTime.setObjectName(_fromUtf8("RunTime"))
        self.Bulb = QtGui.QLabel(PregSim)
        self.Bulb.setGeometry(QtCore.QRect(310, 440, 41, 51))
        self.Bulb.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/BulbOff.png);\n"
"background-repeat: no-repeat"))
        self.Bulb.setText(_fromUtf8(""))
        self.Bulb.setObjectName(_fromUtf8("Bulb"))

        self.retranslateUi(PregSim)
        QtCore.QMetaObject.connectSlotsByName(PregSim)

    def retranslateUi(self, PregSim):
        PregSim.setWindowTitle(_translate("PregSim", "Monica母婴监护", None))
        self.MoBeatmin.setText(_translate("PregSim", "Beat/min", None))
        self.ChHr.setText(_translate("PregSim", "宝宝心率", None))
        self.MoHr.setText(_translate("PregSim", "母亲心率", None))
        self.ChHrNum.setText(_translate("PregSim", "0", None))
        self.RunTimeNum.setText(_translate("PregSim", "00:00:00", None))
        self.ChBeatmin.setText(_translate("PregSim", "Beat/min", None))
        self.MoMov.setText(_translate("PregSim", "母亲活动强度：1~3/S", None))
        self.MoHrNum.setText(_translate("PregSim", "0", None))
        self.pushButton.setText(_translate("PregSim", "切换窗口", None))
        self.RunTime.setText(_translate("PregSim", "运行时间:", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PregSim = QtGui.QDialog()
    ui = Ui_PregSim()
    ui.setupUi(PregSim)
    PregSim.show()
    sys.exit(app.exec_())

