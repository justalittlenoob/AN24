# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\Holter_review_20151116_edition4.0\_eric4project\Holter.ui'
#
# Created: Fri Dec 04 13:18:01 2015
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
        Holter.setMinimumSize(QtCore.QSize(925, 700))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        Holter.setFont(font)
        self.centralWidget = QtGui.QWidget(Holter)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(1280, 70, 101, 451))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/panel-ground.png);"))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.xscale1 = QtGui.QPushButton(self.frame)
        self.xscale1.setGeometry(QtCore.QRect(30, 10, 41, 41))
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
        self.xscale2 = QtGui.QPushButton(self.frame)
        self.xscale2.setGeometry(QtCore.QRect(30, 60, 41, 41))
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
        self.xscale3 = QtGui.QPushButton(self.frame)
        self.xscale3.setGeometry(QtCore.QRect(30, 110, 41, 41))
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
        self.pushButtonSettings = QtGui.QPushButton(self.frame)
        self.pushButtonSettings.setGeometry(QtCore.QRect(20, 170, 71, 71))
        self.pushButtonSettings.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/settings.png);\n"
"background-repeat: no-repeat;"))
        self.pushButtonSettings.setText(_fromUtf8(""))
        self.pushButtonSettings.setFlat(True)
        self.pushButtonSettings.setObjectName(_fromUtf8("pushButtonSettings"))
        self.pushStepForward = QtGui.QPushButton(self.frame)
        self.pushStepForward.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.pushStepForward.setObjectName(_fromUtf8("pushStepForward"))
        self.pushStepBack = QtGui.QPushButton(self.frame)
        self.pushStepBack.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.pushStepBack.setObjectName(_fromUtf8("pushStepBack"))
        self.pushForward = QtGui.QPushButton(self.frame)
        self.pushForward.setGeometry(QtCore.QRect(20, 310, 75, 23))
        self.pushForward.setObjectName(_fromUtf8("pushForward"))
        self.pushBack = QtGui.QPushButton(self.frame)
        self.pushBack.setGeometry(QtCore.QRect(20, 340, 75, 23))
        self.pushBack.setObjectName(_fromUtf8("pushBack"))
        self.pushButtonDownload = QtGui.QPushButton(self.frame)
        self.pushButtonDownload.setGeometry(QtCore.QRect(20, 370, 75, 61))
        self.pushButtonDownload.setObjectName(_fromUtf8("pushButtonDownload"))
        self.frame_2 = QtGui.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1391, 51))
        self.frame_2.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/panel-ground.png);"))
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_hospitalization = QtGui.QLabel(self.frame_2)
        self.label_hospitalization.setGeometry(QtCore.QRect(180, 10, 281, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_hospitalization.setFont(font)
        self.label_hospitalization.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/blank-ground.png);"))
        self.label_hospitalization.setTextFormat(QtCore.Qt.AutoText)
        self.label_hospitalization.setObjectName(_fromUtf8("label_hospitalization"))
        self.label_bed = QtGui.QLabel(self.frame_2)
        self.label_bed.setGeometry(QtCore.QRect(480, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_bed.setFont(font)
        self.label_bed.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/blank-ground.png);"))
        self.label_bed.setTextFormat(QtCore.Qt.AutoText)
        self.label_bed.setObjectName(_fromUtf8("label_bed"))
        self.label_name = QtGui.QLabel(self.frame_2)
        self.label_name.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/blank-ground.png);"))
        self.label_name.setObjectName(_fromUtf8("label_name"))
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
        self.pushPrint = QtGui.QPushButton(self.centralWidget)
        self.pushPrint.setGeometry(QtCore.QRect(80, 70, 75, 23))
        self.pushPrint.setObjectName(_fromUtf8("pushPrint"))
        Holter.setCentralWidget(self.centralWidget)

        self.retranslateUi(Holter)
        QtCore.QMetaObject.connectSlotsByName(Holter)

    def retranslateUi(self, Holter):
        Holter.setWindowTitle(_translate("Holter", "MainWindow", None))
        self.pushStepForward.setText(_translate("Holter", ">", None))
        self.pushStepBack.setText(_translate("Holter", "<", None))
        self.pushForward.setText(_translate("Holter", ">>", None))
        self.pushBack.setText(_translate("Holter", "<<", None))
        self.pushButtonDownload.setText(_translate("Holter", "Download", None))
        self.label_hospitalization.setText(_translate("Holter", "Hospitalization NO:", None))
        self.label_bed.setText(_translate("Holter", "Bed NO:", None))
        self.label_name.setText(_translate("Holter", "Name:", None))
        self.pushPrint.setText(_translate("Holter", "print", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Holter = QtGui.QMainWindow()
    ui = Ui_Holter()
    ui.setupUi(Holter)
    Holter.show()
    sys.exit(app.exec_())

