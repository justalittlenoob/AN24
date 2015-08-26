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
        self.nameChosen = "no device"
        self.is_connected = False
    def connect_start(self, dictChosen):
        self.nameChosen = "no device"
        self.is_connected = False
        self.nameChosen = dictChosen.name
        self.is_connected = self.connectAN24(dictChosen)
        return self.is_connected
    
    def connectAN24(self, dictChosen):        
        
        """
        此处连接蓝牙的函数，参数为SeaAN24.Address,return connected,a bool.
        """
        self.init_paint()
        is_connected=dictChosen.rawAN24.sock 
        self.update_paint(is_connected)       
        return is_connected  
    
    def init_paint(self):
        self.label.setText(self.nameChosen+u"正在连接……") 
        self.show()
        self.repaint()
        #time.sleep(1)
    
    def update_paint(self, is_connected):
        if  is_connected:
            new_text = self.nameChosen+u"连接成功!"
        else:
            new_text = self.nameChosen+u"连接失败，请重新选择"  
        self.label.setText(new_text)           
        self.repaint()
        time.sleep(1)
        self.accept()
