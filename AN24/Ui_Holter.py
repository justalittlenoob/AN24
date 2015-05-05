# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\FHR 20150318\_eric4project\Holter.ui'
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

class Ui_Holter(object):
    def setupUi(self, Holter):
        Holter.setObjectName(_fromUtf8("Holter"))
        Holter.resize(1388, 790)
        self.centralWidget = QtGui.QWidget(Holter)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.visualChange = QtGui.QPushButton(self.centralWidget)
        self.visualChange.setGeometry(QtCore.QRect(1300, 20, 61, 51))
        self.visualChange.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualChange.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/visual.png);\n"
"background-repeat:no-repeat;"))
        self.visualChange.setInputMethodHints(QtCore.Qt.ImhNone)
        self.visualChange.setText(_fromUtf8(""))
        self.visualChange.setDefault(False)
        self.visualChange.setFlat(True)
        self.visualChange.setObjectName(_fromUtf8("visualChange"))
        Holter.setCentralWidget(self.centralWidget)

        self.retranslateUi(Holter)
        QtCore.QMetaObject.connectSlotsByName(Holter)

    def retranslateUi(self, Holter):
        Holter.setWindowTitle(_translate("Holter", "MainWindow", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Holter = QtGui.QMainWindow()
    ui = Ui_Holter()
    ui.setupUi(Holter)
    Holter.show()
    sys.exit(app.exec_())

