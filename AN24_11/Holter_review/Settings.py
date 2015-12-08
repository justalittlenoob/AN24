# -*- coding: utf-8 -*-

"""
Module implementing Settings.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_Settings import Ui_Settings

class Settings(QDialog, Ui_Settings):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.FHR_limit = [80, 110,140, 180 ]
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.FHR_limit[0]= self.lineEditBottom.text().toInt()[0]
        self.FHR_limit[1]= self.lineEditLower.text().toInt()[0]
        self.FHR_limit[2]= self.lineEditUpper.text().toInt()[0]
        self.FHR_limit[3]= self.lineEditTop.text().toInt()[0]
        self.print_minutes = self.lineEditMinutes.text().toInt()[0]
        self.accept()
    
    @pyqtSignature("")
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    def change_settings(self):
        self.__init__(self)
        self.exec_() 
        return self.FHR_limit, self.print_minutes
