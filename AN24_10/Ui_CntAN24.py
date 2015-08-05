# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\FHR_20150427_edition2.0\_eric4project\CntAN24.ui'
#
# Created: Mon Apr 27 14:18:15 2015
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

class Ui_CntAN24(object):
    def setupUi(self, CntAN24):
        CntAN24.setObjectName(_fromUtf8("CntAN24"))
        CntAN24.resize(657, 181)
        CntAN24.setModal(True)
        self.label = QtGui.QLabel(CntAN24)
        self.label.setGeometry(QtCore.QRect(50, 70, 341, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(CntAN24)
        QtCore.QMetaObject.connectSlotsByName(CntAN24)

    def retranslateUi(self, CntAN24):
        CntAN24.setWindowTitle(_translate("CntAN24", "Dialog", None))
        self.label.setText(_translate("CntAN24", "正在连接AN24……", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CntAN24 = QtGui.QDialog()
    ui = Ui_CntAN24()
    ui.setupUi(CntAN24)
    CntAN24.show()
    sys.exit(app.exec_())

