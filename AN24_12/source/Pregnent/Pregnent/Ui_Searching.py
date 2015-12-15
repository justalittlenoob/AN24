# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Holter_mother_20150925_edition2.4\_eric4project\Searching.ui'
#
# Created: Tue Oct 06 16:19:08 2015
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

class Ui_Searching(object):
    def setupUi(self, Searching):
        Searching.setObjectName(_fromUtf8("Searching"))
        Searching.resize(500, 1)
        Searching.setWindowTitle(_fromUtf8("正在查找AN24，请稍候……"))
        Searching.setSizeGripEnabled(False)
        self.label = QtGui.QLabel(Searching)
        self.label.setGeometry(QtCore.QRect(30, 20, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Searching)
        QtCore.QMetaObject.connectSlotsByName(Searching)

    def retranslateUi(self, Searching):
        self.label.setText(_translate("Searching", "正在查找AN24……", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Searching = QtGui.QDialog()
    ui = Ui_Searching()
    ui.setupUi(Searching)
    Searching.show()
    sys.exit(app.exec_())

