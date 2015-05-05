# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\FHR_20150504_edition2.0\_eric4project\Holter.ui'
#
# Created: Mon May 04 10:46:19 2015
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

class Ui_Holter(object):
    def setupUi(self, Holter):
        Holter.setObjectName(_fromUtf8("Holter"))
        Holter.resize(1388, 790)
        self.centralWidget = QtGui.QWidget(Holter)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pinTest = QtGui.QPushButton(self.centralWidget)
        self.pinTest.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pinTest.setObjectName(_fromUtf8("pinTest"))
        self.restTime = QtGui.QLabel(self.centralWidget)
        self.restTime.setGeometry(QtCore.QRect(920, 20, 351, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.restTime.setFont(font)
        self.restTime.setObjectName(_fromUtf8("restTime"))
        self.visualChange = QtGui.QPushButton(self.centralWidget)
        self.visualChange.setGeometry(QtCore.QRect(1210, 30, 61, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visualChange.sizePolicy().hasHeightForWidth())
        self.visualChange.setSizePolicy(sizePolicy)
        self.visualChange.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualChange.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/visual.png);\n"
"background-repeat:no-repeat;"))
        self.visualChange.setInputMethodHints(QtCore.Qt.ImhNone)
        self.visualChange.setText(_fromUtf8(""))
        self.visualChange.setDefault(False)
        self.visualChange.setFlat(True)
        self.visualChange.setObjectName(_fromUtf8("visualChange"))
        self.pushSearch = QtGui.QPushButton(self.centralWidget)
        self.pushSearch.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.pushSearch.setObjectName(_fromUtf8("pushSearch"))
        self.pushConnect = QtGui.QPushButton(self.centralWidget)
        self.pushConnect.setGeometry(QtCore.QRect(190, 20, 75, 23))
        self.pushConnect.setObjectName(_fromUtf8("pushConnect"))
        self.pushCheck = QtGui.QPushButton(self.centralWidget)
        self.pushCheck.setGeometry(QtCore.QRect(270, 20, 75, 23))
        self.pushCheck.setObjectName(_fromUtf8("pushCheck"))
        self.pushStart = QtGui.QPushButton(self.centralWidget)
        self.pushStart.setGeometry(QtCore.QRect(350, 20, 75, 23))
        self.pushStart.setObjectName(_fromUtf8("pushStart"))
        self.recvStop = QtGui.QPushButton(self.centralWidget)
        self.recvStop.setGeometry(QtCore.QRect(430, 20, 75, 23))
        self.recvStop.setObjectName(_fromUtf8("recvStop"))
        self.pushSoundSwitch = QtGui.QPushButton(self.centralWidget)
        self.pushSoundSwitch.setGeometry(QtCore.QRect(510, 20, 75, 23))
        self.pushSoundSwitch.setObjectName(_fromUtf8("pushSoundSwitch"))
        self.xscale1 = QtGui.QPushButton(self.centralWidget)
        self.xscale1.setGeometry(QtCore.QRect(1220, 110, 41, 42))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale1.sizePolicy().hasHeightForWidth())
        self.xscale1.setSizePolicy(sizePolicy)
        self.xscale1.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/1.png);\n"
"background-repeat:no-repeat;"))
        self.xscale1.setText(_fromUtf8(""))
        self.xscale1.setAutoDefault(False)
        self.xscale1.setDefault(False)
        self.xscale1.setFlat(True)
        self.xscale1.setObjectName(_fromUtf8("xscale1"))
        self.xscale2 = QtGui.QPushButton(self.centralWidget)
        self.xscale2.setGeometry(QtCore.QRect(1220, 170, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale2.sizePolicy().hasHeightForWidth())
        self.xscale2.setSizePolicy(sizePolicy)
        self.xscale2.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/2.png);\n"
"background-repeat:no-repeat;"))
        self.xscale2.setText(_fromUtf8(""))
        self.xscale2.setAutoDefault(False)
        self.xscale2.setDefault(False)
        self.xscale2.setFlat(True)
        self.xscale2.setObjectName(_fromUtf8("xscale2"))
        self.xscale3 = QtGui.QPushButton(self.centralWidget)
        self.xscale3.setGeometry(QtCore.QRect(1220, 220, 39, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale3.sizePolicy().hasHeightForWidth())
        self.xscale3.setSizePolicy(sizePolicy)
        self.xscale3.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/3.png);\n"
"background-repeat:no-repeat;"))
        self.xscale3.setText(_fromUtf8(""))
        self.xscale3.setAutoDefault(False)
        self.xscale3.setDefault(False)
        self.xscale3.setFlat(True)
        self.xscale3.setObjectName(_fromUtf8("xscale3"))
        Holter.setCentralWidget(self.centralWidget)

        self.retranslateUi(Holter)
        QtCore.QMetaObject.connectSlotsByName(Holter)

    def retranslateUi(self, Holter):
        Holter.setWindowTitle(_translate("Holter", "MainWindow", None))
        self.pinTest.setText(_translate("Holter", "pinTest", None))
        self.restTime.setText(_translate("Holter", "剩余时间：", None))
        self.pushSearch.setText(_translate("Holter", "search", None))
        self.pushConnect.setText(_translate("Holter", "connect", None))
        self.pushCheck.setText(_translate("Holter", "check", None))
        self.pushStart.setText(_translate("Holter", "start", None))
        self.recvStop.setText(_translate("Holter", "stop", None))
        self.pushSoundSwitch.setText(_translate("Holter", "sound off", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Holter = QtGui.QMainWindow()
    ui = Ui_Holter()
    ui.setupUi(Holter)
    Holter.show()
    sys.exit(app.exec_())

