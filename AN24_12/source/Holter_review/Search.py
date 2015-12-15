# -*- coding: utf-8 -*-

"""
Module implementing Search.
"""

from PyQt4.QtGui import QDialog, QTableWidgetItem
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QAbstractItemView

from Ui_Search import Ui_Search

class Search(QDialog, Ui_Search):
    """
    Class documentation goes here.
    """
    def __init__(self, review_cl, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.init_var()
        
        self.tablePatient.setColumnCount(3)
        self.tablePatient.setRowCount(10)
        self.tablePatient.setHorizontalHeaderLabels([u'姓名',u'年龄',u'病人ID'])
        self.tablePatient.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.tablePatient.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePatient.setSelectionMode(QAbstractItemView.SingleSelection)
        
        self.tableRecords.setColumnCount(3)
        self.tableRecords.setRowCount(10)
        self.tableRecords.setHorizontalHeaderLabels([u'开始时间', u'结束时间', u'记录ID'])
        self.tableRecords.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.tableRecords.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableRecords.setSelectionMode(QAbstractItemView.SingleSelection)
        self.review_cl = review_cl

    def init_var(self):
        self.patientList =  []     
        self.recordList = []
        self.chose_uuid =''
        self.patient_info = []
    def show_self(self):
        self.init_var()
        self.tableRecords.clear()
        self.tablePatient.clear()
        self.tablePatient.setHorizontalHeaderLabels([u'姓名',u'年龄',u'病人ID'])
        self.tableRecords.setHorizontalHeaderLabels([u'开始时间', u'结束时间', u'记录ID'])
        self.exec_()
        return self.patient_info, self.chose_uuid
    
    def search_patients(self):
        Name = self.lineEditName.text().__unicode__().encode('utf-8')
        ID = self.lineEditID.text().__unicode__().encode('utf-8')
        Amount = self.lineEditAmount.text().__unicode__().encode('utf-8')
        startTime = self.dateTimeST.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        endTime = self.dateTimeET.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        if len(Amount) == 0:
            Amount = '10'
        if len(Name) == 0:
            Name = 'None'
        if len(ID) == 0:
            ID = '000000000000000000'
        if startTime == '2000-01-01 00:00:00':
            startTime = '0000-00-00 00:00:00'
        if endTime == '2000-01-01 00:00:00':
            endTime = '0000-00-00 00:00:00'
        #self.patient.age = self.lineEdit_Age.text().toInt()[0]
        self.review_cl.get_his_p(Amount, ID, startTime, endTime, Name)  
                       
    @pyqtSignature("")
    def on_pushSearch_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.search_patients()
        i=0
        patient_List = []
        for key in self.review_cl.his_patient:
            temp_patient = key[0:8]
            if temp_patient not in patient_List:
                patient_List.append(temp_patient)
                newItem = QTableWidgetItem(temp_patient[0])  
                self.tablePatient.setItem(i, 0, newItem)
                newItem = QTableWidgetItem(temp_patient[2])  
                self.tablePatient.setItem(i, 1, newItem)
                newItem = QTableWidgetItem(temp_patient[4])  
                self.tablePatient.setItem(i, 2, newItem)
                i+=1

    @pyqtSignature("int, int")
    def on_tablePatient_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            print self.tablePatient.item(row,1).text()
        except AttributeError, reason:
            print 'None type'
        else:
            patientID = self.tablePatient.item(row,2).text().__unicode__().encode('utf-8')
            i = 0
            for key in self.review_cl.his_patient:
                if key[4] == patientID:
                    newItem = QTableWidgetItem(key[8])   
                    self.tableRecords.setItem(i, 0, newItem)
                    newItem = QTableWidgetItem(key[9])   
                    self.tableRecords.setItem(i, 1, newItem)
                    newItem = QTableWidgetItem(self.review_cl.his_patient[key])   
                    self.tableRecords.setItem(i, 2, newItem)
                    i+=1
    
   
    @pyqtSignature("int, int")
    def on_tableRecords_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        """
        self.chose_uuid = self.tableRecords.item(row,2).text().__unicode__().encode('utf-8')
        for key in self.review_cl.his_patient:
            if self.review_cl.his_patient[key] == self.chose_uuid:
                self.patient_info = key
        self.accept()
