# -*- coding: utf-8 -*-

"""
Module implementing Searching.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_Searching import Ui_Searching

class Searching(QDialog, Ui_Searching):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    def showself(self):
        self.show()
        self.update()
