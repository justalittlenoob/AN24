# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\work in 2015 summer\5-HOLTER\FHR_20150729_edition2.3\_eric4project\FillNote.ui'
#
# Created: Wed Jul 29 14:55:31 2015
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

class Ui_FillNote(object):
    def setupUi(self, FillNote):
        FillNote.setObjectName(_fromUtf8("FillNote"))
        FillNote.resize(400, 201)
        self.textEdit_note = QtGui.QTextEdit(FillNote)
        self.textEdit_note.setGeometry(QtCore.QRect(0, 0, 401, 161))
        self.textEdit_note.setObjectName(_fromUtf8("textEdit_note"))
        self.buttonBox = QtGui.QDialogButtonBox(FillNote)
        self.buttonBox.setGeometry(QtCore.QRect(230, 170, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(FillNote)
        QtCore.QMetaObject.connectSlotsByName(FillNote)

    def retranslateUi(self, FillNote):
        FillNote.setWindowTitle(_translate("FillNote", "Fill in note here:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FillNote = QtGui.QDialog()
    ui = Ui_FillNote()
    ui.setupUi(FillNote)
    FillNote.show()
    sys.exit(app.exec_())

