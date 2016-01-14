# -*- coding: utf-8 -*-

"""
Module implementing FillPatient.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import (pyqtSignature,  QTimer,  SIGNAL, QObject)

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
        self.timerEnable = QTimer()             
        QObject.connect(self.timerEnable, SIGNAL("timeout()"),self.switchEnable)
    
    def fill_in_information(self, patient, refill):
        self.patient = patient
        self.refill = refill
        self.__init__()
        self.lineEdit_Person_No.setText(self.patient.person_num)
        self.lineEdit_Name.setText(self.patient.name)
        if self.patient.age == 0:
            self.lineEdit_Age.setText('')
        else:
            self.lineEdit_Age.setText(str(self.patient.age))
        if self.patient.weeks == 0:
            self.lineEdit_Weeks.setText('')
        else:
            self.lineEdit_Weeks.setText(str(self.patient.weeks))
        self.lineEdit_Outpatient_NO.setText(self.patient.outpatient_num)
        self.lineEdit_Hospitalization_NO.setText(self.patient.hospitalization_num)
        self.lineEdit_Bed_NO.setText(self.patient.bed_num)
        self.lineEdit_Guardianship_NO.setText(self.patient.guardianship_num)
        if refill:
            self.lineEdit_Person_No.setEnabled(False)
        else:
            self.lineEdit_Person_No.setEnabled(True)
        self.timerEnable.start(100)
        self.exec_()
        return self.patient
    
    def switchEnable(self):
        if len(self.lineEdit_Person_No.text().__unicode__()) ==18:
            self.pushButton_OK.setEnabled(True)
        else:
            self.pushButton_OK.setEnabled(False)
    
    @pyqtSignature("")
    def on_pushButton_OK_clicked(self):
        """
        Slot documentation goes here.
        """
        self.patient.person_num = self.lineEdit_Person_No.text().__unicode__()
        self.patient.name = self.lineEdit_Name.text().__unicode__()
        self.patient.age = self.lineEdit_Age.text().toInt()[0]
        self.patient.weeks = self.lineEdit_Weeks.text().toInt()[0]
        self.patient.outpatient_num = self.lineEdit_Outpatient_NO.text().__unicode__()
        self.patient.hospitalization_num = self.lineEdit_Hospitalization_NO.text().__unicode__()
        self.patient.bed_num = self.lineEdit_Bed_NO.text().__unicode__()
        self.patient.guardianship_num = self.lineEdit_Guardianship_NO.text().__unicode__()
        self.timerEnable.stop()
        self.accept()
        
    
    @pyqtSignature("")
    def on_pushButton_Reset_clicked(self):
        """
        Slot documentation goes here.
        """
        self.reset_text()
    
    def reset_text(self):
        if not self.refill:
            self.lineEdit_Person_No.clear()
        self.lineEdit_Name.clear()
        self.lineEdit_Age.clear()
        self.lineEdit_Weeks.clear()
        self.lineEdit_Outpatient_NO.clear()
        self.lineEdit_Hospitalization_NO.clear()
        self.lineEdit_Bed_NO.clear()
        self.lineEdit_Guardianship_NO.clear()
        
    @pyqtSignature("")
    def on_accepted(self):
        self.reset_text()
