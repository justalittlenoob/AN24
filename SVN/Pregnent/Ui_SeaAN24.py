# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\FHR 20150414\_eric4project\SeaAN24.ui'
#
# Created: Tue Apr 14 21:57:48 2015
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

class Ui_SeaAN24(object):
    def setupUi(self, SeaAN24):
        SeaAN24.setObjectName(_fromUtf8("SeaAN24"))
        SeaAN24.resize(642, 287)
        SeaAN24.setModal(True)
        self.label = QtGui.QLabel(SeaAN24)
        self.label.setGeometry(QtCore.QRect(360, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SeaAN24)
        self.label_2.setGeometry(QtCore.QRect(360, 100, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listWidget = QtGui.QListWidget(SeaAN24)
        self.listWidget.setGeometry(QtCore.QRect(50, 60, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton = QtGui.QPushButton(SeaAN24)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(360, 190, 121, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(SeaAN24)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(SeaAN24)
        QtCore.QMetaObject.connectSlotsByName(SeaAN24)

    def retranslateUi(self, SeaAN24):
        SeaAN24.setWindowTitle(_translate("SeaAN24", "Dialog", None))
        self.label.setText(_translate("SeaAN24", "<html><head/><body><p><span style=\" font-size:16pt;\">请选择相应的AN24设备</span></p></body></html>", None))
        self.label_2.setText(_translate("SeaAN24", "<html><head/><body><p><span style=\" font-size:16pt;\">并继续。</span></p></body></html>", None))
        self.pushButton.setText(_translate("SeaAN24", "选择", None))
        self.label_3.setText(_translate("SeaAN24", "<html><head/><body><p>已查找到AN24</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SeaAN24 = QtGui.QDialog()
    ui = Ui_SeaAN24()
    ui.setupUi(SeaAN24)
    SeaAN24.show()
    sys.exit(app.exec_())

