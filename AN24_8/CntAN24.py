# -*- coding: utf-8 -*-

"""
Module implementing CntAN24.
"""
import sys, PyQt4, time, random
from PyQt4 import QtCore
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import (pyqtSignature, QTimer, SIGNAL)

from Ui_CntAN24 import Ui_CntAN24

class CntAN24(QDialog, Ui_CntAN24):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    def connect_start(self, dictChosen):
        self.__init__()
        self.nameChosen = dictChosen.name
        self.show()
        isConnected = self.connectAN24(dictChosen)
        return isConnected
    
    def connectAN24(self, dictChosen):
        
        self.label.setText(self.nameChosen+u"正在连接……") 
        self.repaint()
        
        """
        此处连接蓝牙的函数，参数为SeaAN24.Address,return connected,a bool.
        """
        print time.ctime()
        time.sleep(2)
        connected=dictChosen.rawAN24.sock
        
        if connected:
            print 'successful connection!'
            self.label.setText(self.nameChosen+u"连接成功!")           
            self.repaint()
            time.sleep(1)
            self.accept()
            return True
        else:
            self.label.setText(self.nameChosen+u"连接失败，请重新选择")           
            self.repaint()
            time.sleep(1)
            self.accept()
            return False
