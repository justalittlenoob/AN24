# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\work in 2015 summer\5-HOLTER\FHR_20150729_edition2.3\_eric4project\Settings.ui'
#
# Created: Wed Jul 29 15:44:11 2015
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

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(350, 527)
        self.tabWidget = QtGui.QTabWidget(Settings)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 331, 511))
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.init = QtGui.QWidget()
        self.init.setObjectName(_fromUtf8("init"))
        self.tabWidget.addTab(self.init, _fromUtf8(""))
        self.view = QtGui.QWidget()
        self.view.setObjectName(_fromUtf8("view"))
        self.buttonBox = QtGui.QDialogButtonBox(self.view)
        self.buttonBox.setGeometry(QtCore.QRect(150, 450, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.view)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 281, 101))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditTop = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEditTop.setObjectName(_fromUtf8("lineEditTop"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditTop)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditUpper = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEditUpper.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditUpper.setObjectName(_fromUtf8("lineEditUpper"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditUpper)
        self.lineEditLower = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEditLower.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditLower.setObjectName(_fromUtf8("lineEditLower"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditLower)
        self.lineEditBottom = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEditBottom.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditBottom.setObjectName(_fromUtf8("lineEditBottom"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditBottom)
        self.tabWidget.addTab(self.view, _fromUtf8(""))
        self.storage = QtGui.QWidget()
        self.storage.setObjectName(_fromUtf8("storage"))
        self.tabWidget.addTab(self.storage, _fromUtf8(""))
        self.printer = QtGui.QWidget()
        self.printer.setObjectName(_fromUtf8("printer"))
        self.tabWidget.addTab(self.printer, _fromUtf8(""))
        self.note = QtGui.QWidget()
        self.note.setObjectName(_fromUtf8("note"))
        self.tabWidget.addTab(self.note, _fromUtf8(""))

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.init), _translate("Settings", "init", None))
        self.label.setText(_translate("Settings", "top_limit:", None))
        self.label_3.setText(_translate("Settings", "upper_limit:", None))
        self.label_4.setText(_translate("Settings", "lower_limit:", None))
        self.label_2.setText(_translate("Settings", "bottom_limit:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view), _translate("Settings", "view", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.storage), _translate("Settings", "storage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.printer), _translate("Settings", "printer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.note), _translate("Settings", "note", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Settings = QtGui.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())

