# -*- coding: utf-8 -*-

"""
Module implementing FillPatient.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_FillPatient import Ui_FillPatient

class FillPatient(QDialog, Ui_FillPatient):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.dict= {}
    
    def fill_in_information(self):
        self.exec_()
        return self.dict
    
    @pyqtSignature("")
    def on_pushButton_OK_clicked(self):
        """
        Slot documentation goes here.
        """
        self.dict['name'] = self.lineEdit_Name.text().__unicode__()
        self.dict['age'] = self.lineEdit_Age.text().toInt()[0]
        self.dict['weeks'] = self.lineEdit_Weeks.text().toInt()[0]
        self.dict['outpatient_num'] = self.lineEdit_Outpatient_NO.text().__unicode__()
        self.dict['hospitalization_num'] = self.lineEdit_Hospitalization_NO.text().__unicode__()
        self.dict['bed_num'] = self.lineEdit_Bed_NO.text().__unicode__()
        self.dict['guardianship_num'] = self.lineEdit_Guardianship_NO.text().__unicode__()
        self.accept()
        
    
    @pyqtSignature("")
    def on_pushButton_Reset_clicked(self):
        """
        Slot documentation goes here.
        """
        self.lineEdit_Name.clear()
        self.lineEdit_Age.clear()
        self.lineEdit_Weeks.clear()
        self.lineEdit_Outpatient_NO.clear()
        self.lineEdit_Hospitalization_NO.clear()
        self.lineEdit_Bed_NO.clear()
        self.lineEdit_Guardianship_NO.clear()
        
