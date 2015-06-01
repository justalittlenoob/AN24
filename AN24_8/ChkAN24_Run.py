# -*- coding: utf-8 -*-

"""
Module implementing ChkAN24_Run.
"""
import time
from PyQt4 import QtCore
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import (pyqtSignature, QTimer,  SIGNAL)

from Ui_ChkAN24_Run import Ui_ChkAN24_Run

class ChkAN24_Run(QDialog, Ui_ChkAN24_Run):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.labelList=[self.Check, self.Check_2, self.Check_3,self.Check_4, self.Check_5]

    def paintEvent(self, event):
        for i in range(5):            
            if self.check_value[i]==0:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/OK.png);background-repeat:no-repeat;") 
            elif self.check_value[i]==1:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/questionMark.png);background-repeat:no-repeat;")
            else:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/No.png);background-repeat:no-repeat;")
        try:        
            self.label.setText(self.an24_name + u"电极脱落，请重连电极。")
        except AttributeError, reason:
            print 'run check failed. did not get the run_chk', reason
    def run_check(self, an24dict_chosen):
        self.dictChosen = an24dict_chosen
        self.check_value = self.dictChosen.rawAN24.run_chk
        self.an24_name = self.dictChosen.name
        self.timer_check = QTimer()
        QtCore.QObject.connect(self.timer_check, SIGNAL("timeout()"),self.pin_check)  
        self.timer_check.start(500) 
        self.show()
    
    def pin_check(self):
        self.check_value = self.dictChosen.rawAN24.run_chk
        self.update
        if self.check_value == [0, 0, 0, 0, 0]:            
            self.accept()
            self.timer_check.stop()
        else:
            self.is_checked = False
