# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Holter_mother_20150925_edition2.4\_eric4project\NoAN24.ui'
#
# Created: Tue Oct 06 16:33:52 2015
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

class Ui_NoAN24(object):
    def setupUi(self, NoAN24):
        NoAN24.setObjectName(_fromUtf8("NoAN24"))
        NoAN24.resize(500, 1)

        self.retranslateUi(NoAN24)
        QtCore.QMetaObject.connectSlotsByName(NoAN24)

    def retranslateUi(self, NoAN24):
        NoAN24.setWindowTitle(_translate("NoAN24", "没有找到可用的AN24设备", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NoAN24 = QtGui.QDialog()
    ui = Ui_NoAN24()
    ui.setupUi(NoAN24)
    NoAN24.show()
    sys.exit(app.exec_())

