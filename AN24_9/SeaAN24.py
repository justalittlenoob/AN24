# -*- coding: utf-8 -*-

"""
Module implementing SeaAN24.
"""
import sys, PyQt4
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_SeaAN24 import Ui_SeaAN24

from AN24 import scan_bt

class SeaAN24(QDialog, Ui_SeaAN24):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.AN24_nameDict = {}
        self.AN24_nameList = []
        self.deviceChosen = {}
    def scan_AN24(self):
        self.__init__()
        self.AN24_nameDict = scan_bt()
        self.AN24_nameList = self.addItems(self.AN24_nameDict)
        self.exec_() 
        return self.deviceChosen
        
        
    def addItems(self, dict):
        namelist= []
        for key in dict:
            namelist.append(key)
        n = len(namelist)
        for i in range(n):
            self.listWidget.addItems([namelist[i]])
        return namelist
        
    @pyqtSignature("QListWidgetItem*")
    def on_listWidget_itemClicked(self, item):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        foot=self.listWidget.currentRow()
        nameChosen=self.AN24_nameList[foot]
        addrChosen=self.AN24_nameDict[nameChosen]
        self.deviceChosen = {}
        self.deviceChosen['name']= nameChosen  
        self.deviceChosen['address'] = addrChosen
        #print self.deviceChosen
        self.pushButton.setEnabled(True)

    
    @pyqtSignature("bool")
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented ye
        self.accept()        
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)          
    DlgSearch = SeaAN24()
    app.exit(app.exec_())
