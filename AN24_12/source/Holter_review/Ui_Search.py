# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-HOLTER\Holter_review_20151116_edition4.0\_eric4project\Search.ui'
#
# Created: Fri Dec 04 13:12:49 2015
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

class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName(_fromUtf8("Search"))
        Search.resize(725, 585)
        self.lineEditName = QtGui.QLineEdit(Search)
        self.lineEditName.setGeometry(QtCore.QRect(70, 490, 113, 20))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.label = QtGui.QLabel(Search)
        self.label.setGeometry(QtCore.QRect(40, 10, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Search)
        self.label_2.setGeometry(QtCore.QRect(380, 10, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Search)
        self.label_3.setGeometry(QtCore.QRect(30, 490, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditID = QtGui.QLineEdit(Search)
        self.lineEditID.setGeometry(QtCore.QRect(250, 490, 113, 20))
        self.lineEditID.setObjectName(_fromUtf8("lineEditID"))
        self.label_4 = QtGui.QLabel(Search)
        self.label_4.setGeometry(QtCore.QRect(210, 490, 61, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Search)
        self.label_5.setGeometry(QtCore.QRect(30, 530, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Search)
        self.label_6.setGeometry(QtCore.QRect(320, 530, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tablePatient = QtGui.QTableWidget(Search)
        self.tablePatient.setGeometry(QtCore.QRect(20, 40, 311, 411))
        self.tablePatient.setObjectName(_fromUtf8("tablePatient"))
        self.tablePatient.setColumnCount(0)
        self.tablePatient.setRowCount(0)
        self.tableRecords = QtGui.QTableWidget(Search)
        self.tableRecords.setGeometry(QtCore.QRect(375, 40, 331, 411))
        self.tableRecords.setObjectName(_fromUtf8("tableRecords"))
        self.tableRecords.setColumnCount(0)
        self.tableRecords.setRowCount(0)
        self.pushSearch = QtGui.QPushButton(Search)
        self.pushSearch.setGeometry(QtCore.QRect(580, 480, 121, 71))
        self.pushSearch.setObjectName(_fromUtf8("pushSearch"))
        self.dateTimeST = QtGui.QDateTimeEdit(Search)
        self.dateTimeST.setGeometry(QtCore.QRect(100, 530, 194, 22))
        self.dateTimeST.setObjectName(_fromUtf8("dateTimeST"))
        self.dateTimeET = QtGui.QDateTimeEdit(Search)
        self.dateTimeET.setGeometry(QtCore.QRect(370, 530, 194, 22))
        self.dateTimeET.setObjectName(_fromUtf8("dateTimeET"))
        self.label_7 = QtGui.QLabel(Search)
        self.label_7.setGeometry(QtCore.QRect(390, 490, 41, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEditAmount = QtGui.QLineEdit(Search)
        self.lineEditAmount.setGeometry(QtCore.QRect(440, 490, 113, 20))
        self.lineEditAmount.setObjectName(_fromUtf8("lineEditAmount"))

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        Search.setWindowTitle(_translate("Search", "Dialog", None))
        self.label.setText(_translate("Search", "patients", None))
        self.label_2.setText(_translate("Search", "records", None))
        self.label_3.setText(_translate("Search", "Name:", None))
        self.label_4.setText(_translate("Search", "ID:", None))
        self.label_5.setText(_translate("Search", "StartTime:", None))
        self.label_6.setText(_translate("Search", "EndTime:", None))
        self.pushSearch.setText(_translate("Search", "Search", None))
        self.label_7.setText(_translate("Search", "Amount:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Search = QtGui.QDialog()
    ui = Ui_Search()
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec_())

