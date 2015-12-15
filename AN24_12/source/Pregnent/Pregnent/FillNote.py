# -*- coding: utf-8 -*-

"""
Module implementing FillNote.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_FillNote import Ui_FillNote

class FillNote(QDialog, Ui_FillNote):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    def fill_note(self):
        self.note = ''
        self.textEdit_note.clear()
        self.exec_()
        return self.note
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        self.note = self.textEdit_note.toPlainText().__unicode__()
        self.accept()
        
    @pyqtSignature("")
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()

    
