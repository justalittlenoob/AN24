# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\Holter_mother_20150914_edition3.3\_eric4project\Holter.ui'
#
# Created: Mon Sep 14 19:56:32 2015
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
        Holter.resize(1444, 790)
        Holter.setMinimumSize(QtCore.QSize(925, 700))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        Holter.setFont(font)
        self.centralWidget = QtGui.QWidget(Holter)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pinTest = QtGui.QPushButton(self.centralWidget)
        self.pinTest.setGeometry(QtCore.QRect(1270, 760, 75, 23))
        self.pinTest.setObjectName(_fromUtf8("pinTest"))
        self.restTime = QtGui.QLabel(self.centralWidget)
        self.restTime.setGeometry(QtCore.QRect(750, 690, 71, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.restTime.setFont(font)
        self.restTime.setStyleSheet(_fromUtf8(""))
        self.restTime.setText(_fromUtf8(""))
        self.restTime.setObjectName(_fromUtf8("restTime"))
        self.widget_1 = ChildWindow(self.centralWidget)
        self.widget_1.setGeometry(QtCore.QRect(120, 90, 131, 71))
        self.widget_1.setStyleSheet(_fromUtf8(""))
        self.widget_1.setObjectName(_fromUtf8("widget_1"))
        self.widget_2 = ChildWindow(self.centralWidget)
        self.widget_2.setGeometry(QtCore.QRect(290, 90, 131, 71))
        self.widget_2.setStyleSheet(_fromUtf8(""))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_3 = ChildWindow(self.centralWidget)
        self.widget_3.setGeometry(QtCore.QRect(440, 90, 131, 71))
        self.widget_3.setStyleSheet(_fromUtf8(""))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.widget_5 = ChildWindow(self.centralWidget)
        self.widget_5.setGeometry(QtCore.QRect(120, 200, 131, 71))
        self.widget_5.setStyleSheet(_fromUtf8(""))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.widget_4 = ChildWindow(self.centralWidget)
        self.widget_4.setGeometry(QtCore.QRect(600, 90, 131, 71))
        self.widget_4.setStyleSheet(_fromUtf8(""))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.widget_6 = ChildWindow(self.centralWidget)
        self.widget_6.setGeometry(QtCore.QRect(290, 200, 131, 71))
        self.widget_6.setStyleSheet(_fromUtf8(""))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.widget_7 = ChildWindow(self.centralWidget)
        self.widget_7.setGeometry(QtCore.QRect(440, 200, 131, 71))
        self.widget_7.setStyleSheet(_fromUtf8(""))
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.widget_8 = ChildWindow(self.centralWidget)
        self.widget_8.setGeometry(QtCore.QRect(600, 200, 131, 71))
        self.widget_8.setStyleSheet(_fromUtf8(""))
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.widget_9 = ChildWindow(self.centralWidget)
        self.widget_9.setGeometry(QtCore.QRect(120, 310, 131, 71))
        self.widget_9.setStyleSheet(_fromUtf8(""))
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.widget_10 = ChildWindow(self.centralWidget)
        self.widget_10.setGeometry(QtCore.QRect(290, 310, 131, 71))
        self.widget_10.setStyleSheet(_fromUtf8(""))
        self.widget_10.setObjectName(_fromUtf8("widget_10"))
        self.widget_11 = ChildWindow(self.centralWidget)
        self.widget_11.setGeometry(QtCore.QRect(440, 310, 131, 71))
        self.widget_11.setStyleSheet(_fromUtf8(""))
        self.widget_11.setObjectName(_fromUtf8("widget_11"))
        self.widget_12 = ChildWindow(self.centralWidget)
        self.widget_12.setGeometry(QtCore.QRect(600, 310, 131, 71))
        self.widget_12.setStyleSheet(_fromUtf8(""))
        self.widget_12.setObjectName(_fromUtf8("widget_12"))
        self.widget_13 = ChildWindow(self.centralWidget)
        self.widget_13.setGeometry(QtCore.QRect(120, 410, 131, 71))
        self.widget_13.setStyleSheet(_fromUtf8(""))
        self.widget_13.setObjectName(_fromUtf8("widget_13"))
        self.widget_14 = ChildWindow(self.centralWidget)
        self.widget_14.setGeometry(QtCore.QRect(290, 410, 131, 71))
        self.widget_14.setStyleSheet(_fromUtf8(""))
        self.widget_14.setObjectName(_fromUtf8("widget_14"))
        self.widget_15 = ChildWindow(self.centralWidget)
        self.widget_15.setGeometry(QtCore.QRect(440, 410, 131, 71))
        self.widget_15.setStyleSheet(_fromUtf8(""))
        self.widget_15.setObjectName(_fromUtf8("widget_15"))
        self.widget_16 = ChildWindow(self.centralWidget)
        self.widget_16.setGeometry(QtCore.QRect(600, 410, 131, 71))
        self.widget_16.setStyleSheet(_fromUtf8(""))
        self.widget_16.setObjectName(_fromUtf8("widget_16"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(1200, 10, 171, 671))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/panel-ground.png);\n"
"border:1px solid black;\n"
"border-radius:5px;\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.xscale1 = QtGui.QPushButton(self.frame)
        self.xscale1.setGeometry(QtCore.QRect(10, 90, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale1.sizePolicy().hasHeightForWidth())
        self.xscale1.setSizePolicy(sizePolicy)
        self.xscale1.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/1.png);\n"
"background-repeat:no-repeat;\n"
"border:no;"))
        self.xscale1.setText(_fromUtf8(""))
        self.xscale1.setAutoDefault(False)
        self.xscale1.setDefault(False)
        self.xscale1.setFlat(True)
        self.xscale1.setObjectName(_fromUtf8("xscale1"))
        self.xscale2 = QtGui.QPushButton(self.frame)
        self.xscale2.setGeometry(QtCore.QRect(60, 90, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale2.sizePolicy().hasHeightForWidth())
        self.xscale2.setSizePolicy(sizePolicy)
        self.xscale2.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/2.png);\n"
"background-repeat:no-repeat;\n"
"border:no"))
        self.xscale2.setText(_fromUtf8(""))
        self.xscale2.setAutoDefault(False)
        self.xscale2.setDefault(False)
        self.xscale2.setFlat(True)
        self.xscale2.setObjectName(_fromUtf8("xscale2"))
        self.xscale3 = QtGui.QPushButton(self.frame)
        self.xscale3.setGeometry(QtCore.QRect(120, 90, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale3.sizePolicy().hasHeightForWidth())
        self.xscale3.setSizePolicy(sizePolicy)
        self.xscale3.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/3.png);\n"
"background-repeat:no-repeat;\n"
"border:no;"))
        self.xscale3.setText(_fromUtf8(""))
        self.xscale3.setAutoDefault(False)
        self.xscale3.setDefault(False)
        self.xscale3.setFlat(True)
        self.xscale3.setObjectName(_fromUtf8("xscale3"))
        self.pushButtonSettings = QtGui.QPushButton(self.frame)
        self.pushButtonSettings.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.pushButtonSettings.setAcceptDrops(False)
        self.pushButtonSettings.setAutoFillBackground(False)
        self.pushButtonSettings.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/settings.png);\n"
"background-repeat: no-repeat;\n"
"border:no\n"
""))
        self.pushButtonSettings.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButtonSettings.setText(_fromUtf8(""))
        self.pushButtonSettings.setAutoRepeat(False)
        self.pushButtonSettings.setAutoExclusive(False)
        self.pushButtonSettings.setAutoDefault(True)
        self.pushButtonSettings.setDefault(False)
        self.pushButtonSettings.setFlat(True)
        self.pushButtonSettings.setObjectName(_fromUtf8("pushButtonSettings"))
        self.pushExit = QtGui.QPushButton(self.frame)
        self.pushExit.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushExit.setObjectName(_fromUtf8("pushExit"))
        self.pushMulti = QtGui.QPushButton(self.frame)
        self.pushMulti.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushMulti.setObjectName(_fromUtf8("pushMulti"))
        self.listWidgetUuid = QtGui.QListWidget(self.centralWidget)
        self.listWidgetUuid.setGeometry(QtCore.QRect(10, 10, 171, 331))
        self.listWidgetUuid.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/panel-ground.png);\n"
"border:1px solid black;\n"
"border-radius:5px;"))
        self.listWidgetUuid.setObjectName(_fromUtf8("listWidgetUuid"))
        Holter.setCentralWidget(self.centralWidget)

        self.retranslateUi(Holter)
        QtCore.QMetaObject.connectSlotsByName(Holter)

    def retranslateUi(self, Holter):
        Holter.setWindowTitle(_translate("Holter", "MainWindow", None))
        self.pinTest.setText(_translate("Holter", "pinTest", None))
        self.pushExit.setText(_translate("Holter", "exit", None))
        self.pushMulti.setText(_translate("Holter", "multiWindow", None))

from ChildWindow import ChildWindow
import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Holter = QtGui.QMainWindow()
    ui = Ui_Holter()
    ui.setupUi(Holter)
    Holter.show()
    sys.exit(app.exec_())

