# -*- coding: utf-8 -*-

"""
Module implementing ChkAN24.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_ChkAN24 import Ui_ChkAN24

class ChkAN24(QDialog, Ui_ChkAN24):
    """
    Class documentation goes here.
    """
    def __init__(self,  parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.labelList=[self.Check, self.Check_2, self.Check_3,self.Check_4, self.Check_5]
        self.check_value  = [1, 1, 1, 1, 1]
        self.is_checked = False
    def paintEvent(self, event):
        for i in range(5):            
            if self.check_value[i]==0:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/OK.png);background-repeat:no-repeat;") 
            elif self.check_value[i]==1:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/questionMark.png);background-repeat:no-repeat;")
            else:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/No.png);background-repeat:no-repeat;")
        
    def init_check(self, dictChosen):
        self.check_value  = [1, 1, 1, 1, 1]
        self.is_checked = False
        self.dictChosen = dictChosen
        self.exec_()
        return self.is_checked
        
    @pyqtSignature("bool")
    def on_ButtonCheck_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        """
        此处checkList为返回的电极检查结果
        """
        self.check_value = self.dictChosen.rawAN24.init_chk        
        self.update()
        if self.check_value == [0, 0, 0, 0, 0]:
            self.is_checked = True
            self.ButtonStart.setEnabled(True)
        else: 
            self.is_checked = False
    @pyqtSignature("bool")
    def on_ButtonStart_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet 
        self.accept()
