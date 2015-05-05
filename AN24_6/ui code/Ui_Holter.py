# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\FHR 20150415\_eric4project\Holter.ui'
#
# Created: Wed Apr 15 15:50:58 2015
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
        self.visualChange = QtGui.QPushButton(self.centralWidget)
        self.visualChange.setGeometry(QtCore.QRect(1290, 30, 61, 51))
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
        self.startButton = QtGui.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.restTime = QtGui.QLabel(self.centralWidget)
        self.restTime.setGeometry(QtCore.QRect(1060, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.restTime.setFont(font)
        self.restTime.setObjectName(_fromUtf8("restTime"))
        Holter.setCentralWidget(self.centralWidget)

        self.retranslateUi(Holter)
        QtCore.QMetaObject.connectSlotsByName(Holter)

    def retranslateUi(self, Holter):
        Holter.setWindowTitle(_translate("Holter", "MainWindow", None))
        self.startButton.setText(_translate("Holter", "pinOff", None))
        self.restTime.setText(_translate("Holter", "剩余时间：", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Holter = QtGui.QMainWindow()
    ui = Ui_Holter()
    ui.setupUi(Holter)
    Holter.show()
    sys.exit(app.exec_())

