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
    
    @pyqtSignature("")
    def on_pushButtonOK_clicked(self):   
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.FHR_limit[0]= self.lineEditBottom.text().toInt()[0]
        self.FHR_limit[1]= self.lineEditLower.text().toInt()[0]
        self.FHR_limit[2]= self.lineEditUpper.text().toInt()[0]
        self.FHR_limit[3]= self.lineEditTop.text().toInt()[0]
        self.print_minutes = self.lineEditMinutes.text().toInt()[0]
        if self.radioAlarmOn.isChecked():
            self.is_alarm_sound = 'ON'
        if self.radioAlarmOff.isChecked():
            self.is_alarm_sound = 'OFF'
        if self.radioHeartOn.isChecked():
            self.init_soundOn = 'True'
        if self.radioHeartOff.isChecked():
            self.init_soundOn = 'False'
        if self.radioXy1.isChecked():
            self.xyRatio = 1
        if self.radioXy2.isChecked():
            self.xyRatio = 2
        if self.radioXy3.isChecked():
            self.xyRatio = 3
        self.screen_ratio = round(self.lineEditScrRatio.text().toFloat()[0], 2)
        self.config.set('Local Settings', 'xyRatio', str(self.xyRatio))
        self.config.set('Local Settings', 'screen_ratio', str(self.screen_ratio))
        self.config.set('Local Settings', 'FHR_bottom_limit', str(self.FHR_limit[0]))
        self.config.set('Local Settings', 'FHR_lower_limit', str(self.FHR_limit[1]))
        self.config.set('Local Settings', 'FHR_upper_limit', str(self.FHR_limit[2]))
        self.config.set('Local Settings', 'FHR_top_limit', str(self.FHR_limit[3]))
        self.config.set('Local Settings', 'is_alarm_sound', self.is_alarm_sound)
        self.config.set('Local Settings', 'init_soundOn', self.init_soundOn)
        self.config.set('Local Settings', 'print_minutes', str(self.print_minutes))
        fh = open("conf.ini" ,'w')
        self.config.write(fh)#把要修改的节点的内容写到文件中
        fh.close()
        self.accept()
    
    @pyqtSignature("")
    def on_pushButtonCancel_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.reject()
        
#    @pyqtSignature("")
#    def on_buttonBox_accepted(self):
#        """
#        Slot documentation goes here.
#        """
#        # TODO: not implemented yet
#        self.FHR_limit[0]= self.lineEditBottom.text().toInt()[0]
#        self.FHR_limit[1]= self.lineEditLower.text().toInt()[0]
#        self.FHR_limit[2]= self.lineEditUpper.text().toInt()[0]
#        self.FHR_limit[3]= self.lineEditTop.text().toInt()[0]
#        self.print_minutes = self.lineEditMinutes.text().toInt()[0]
#        if self.radioAlarmOn.isChecked():
#            self.is_alarm_sound = 'ON'
#        if self.radioAlarmOff.isChecked():
#            self.is_alarm_sound = 'OFF'
#        if self.radioHeartOn.isChecked():
#            self.init_soundOn = 'True'
#        if self.radioHeartOff.isChecked():
#            self.init_soundOn = 'False'
#        if self.radioXy1.isChecked():
#            self.xyRatio = 1
#        if self.radioXy2.isChecked():
#            self.xyRatio = 2
#        if self.radioXy3.isChecked():
#            self.xyRatio = 3
#        self.screen_ratio = round(self.lineEditScrRatio.text().toFloat()[0], 2)
#        self.config.set('Local Settings', 'xyRatio', str(self.xyRatio))
#        self.config.set('Local Settings', 'screen_ratio', str(self.screen_ratio))
#        self.config.set('Local Settings', 'FHR_bottom_limit', str(self.FHR_limit[0]))
#        self.config.set('Local Settings', 'FHR_lower_limit', str(self.FHR_limit[1]))
#        self.config.set('Local Settings', 'FHR_upper_limit', str(self.FHR_limit[2]))
#        self.config.set('Local Settings', 'FHR_top_limit', str(self.FHR_limit[3]))
#        self.config.set('Local Settings', 'is_alarm_sound', self.is_alarm_sound)
#        self.config.set('Local Settings', 'init_soundOn', self.init_soundOn)
#        self.config.set('Local Settings', 'print_minutes', str(self.print_minutes))
#        fh = open("conf.ini" ,'w')
#        self.config.write(fh)#把要修改的节点的内容写到文件中
#        fh.close()
#        self.accept()
#    
#    @pyqtSignature("")
#    def on_buttonBox_rejected(self):
#        """
#        Slot documentation goes here.
#        """
#        # TODO: not implemented yet
#        self.reject()
    
    def change_settings(self, config):
        self.config = config
        self.__init__(self)
        
        self.xyRatio = int(self.config.get('Local Settings', 'xyRatio'))
        self.screen_ratio = float(self.config.get('Local Settings', 'screen_ratio'))
        self.init_soundOn = self.config.get('Local Settings', 'init_soundOn')
        self.is_alarm_sound = self.config.get('Local Settings', 'is_alarm_sound')
        FHR_bottom_limit = int(self.config.get('Local Settings', 'FHR_bottom_limit'))
        FHR_lower_limit = int(self.config.get('Local Settings', 'FHR_lower_limit'))
        FHR_upper_limit = int(self.config.get('Local Settings', 'FHR_upper_limit'))
        FHR_top_limit = int(self.config.get('Local Settings', 'FHR_top_limit'))
        self.FHR_limit = [FHR_bottom_limit, FHR_lower_limit, FHR_upper_limit,  FHR_top_limit]            
        self.print_minutes = int(self.config.get('Local Settings', 'print_minutes'))
        
        #show settings
        if self.init_soundOn == 'True':
            self.radioHeartOn.setChecked(True)
        else:
            self.radioHeartOff.setChecked(True)
        if self.is_alarm_sound == 'ON':
            self.radioAlarmOn.setChecked(True)
        else:
            self.radioAlarmOff.setChecked(True)
        if self.xyRatio == 1:
            self.radioXy1.setChecked(True)
        elif self.xyRatio == 2:
            self.radioXy2.setChecked(True)
        else:
            self.radioXy3.setChecked(True)
        self.lineEditScrRatio.setText(str(self.screen_ratio))
        self.lineEditTop.setText(str(FHR_top_limit))
        self.lineEditUpper.setText(str(FHR_upper_limit))
        self.lineEditLower.setText(str(FHR_lower_limit))
        self.lineEditBottom.setText(str(FHR_bottom_limit))
        self.lineEditMinutes.setText(str(self.print_minutes))
        self.exec_() 
       
        return self.FHR_limit, self.print_minutes,  self.xyRatio, self.screen_ratio,  self.is_alarm_sound,  self.init_soundOn
