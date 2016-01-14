# -*- coding: utf-8 -*-

"""
Module implementing Holter.
"""
import sys, PyQt4,  time

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import (pyqtSignature, QTimer,  SIGNAL, QPropertyAnimation, Qt)
from Ui_Holter import Ui_Holter
from PaintRealTime import  *
from FillPatient import  FillPatient
from FillNote import FillNote
from UiData import UiData
from Settings import  *
from PaintCalculation import PaintCalculation
from DoctorClient import DoctorClient
import os

class Holter(QMainWindow, Ui_Holter):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        self.create_animation() 
        self.init_settings()   
        self.init_var()
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
    
    def init_var(self):
        self.childWidget_list = [
                            self.widget_1, 
                            self.widget_2, 
                            self.widget_3, 
                            self.widget_4, 
                            self.widget_5, 
                            self.widget_6, 
                            self.widget_7, 
                            self.widget_8, 
                            self.widget_9, 
                            self.widget_10, 
                            self.widget_11, 
                            self.widget_12, 
                            self.widget_13, 
                            self.widget_14, 
                            self.widget_15, 
                            self.widget_16
                            ]        
        self.an24Dict = {} 
        self.an24List= []
        self.PCalList= []
        self.is_single_max = False
        self.single_widget = ''
        self.PCal = PaintCalculation()
        self.PCal.evment_calculation(self.size(), self.xyRatio,  self.screen_ratio, self.FHR_limit)
        self.d_c = DoctorClient()
    
    def init_settings(self):
        self.xyRatio = 1
        self.screen_ratio = 0.8
        self.FHR_limit = [80, 110,140, 180]
        self.is_frame_shown = True
        
    def create_animation(self):
        self.animation_hide = QPropertyAnimation(self.frame, "geometry")
        self.animation_hide.setDuration(200)
        self.animation_show = QPropertyAnimation(self.frame, "geometry")
        self.animation_show.setDuration(200)
  
    def set_animation(self):
        self.animation_hide.setStartValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        self.animation_hide.setEndValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setStartValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setEndValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))

    def eventFilter(self, source, event):
        if event.type() == PyQt4.QtCore.QEvent.MouseMove:
            pointX = event.globalX()-self.pos().x()
            if pointX >(self.width() -188):
                if not self.is_frame_shown:
                    self.animation_show.start()
                    self.is_frame_shown = True
            elif self.is_frame_shown:
                self.animation_hide.start()
                self.is_frame_shown = False
        return PyQt4.QtGui.QMainWindow.eventFilter(self, source, event)
        
    def mousePressEvent(self, event):
        pass
        
    def resizeEvent(self, event):
        self.set_animation()
        self.button_position()
        self.widget_changed()
        self.PCal.evment_calculation(self.size(), self.xyRatio,  self.screen_ratio, self.FHR_limit)
        if len(self.an24Dict) ==0:
            self.childWidget_list[0].update_paint(self.PCal)
        self.update()
    
    def paintEvent(self, event):
#        try:
#            qp = PyQt4.QtGui.QPainter() 
#            self.an24Dict[self.an24List[0]]
#        except Exception, reason:     
#            qp.begin(self)
#            paintBg(self, qp, self.PCal.window_rect, self.PCal.bg_rgb, self.PCal.bg_rect, self.PCal.bg_scaleY, self.PCal.FHR_rect, self.PCal.FHR_rgb, self.PCal.ytext_info) 
#            drawInitXScale(self, qp,  self.PCal.window_rect, self.PCal.unitXY['FHR'], self.PCal.all_count,  self.PCal.xyRatio)
#            qp.end()
        pass

    def update_paint(self):
        try:
            self.an24Dict[self.an24List[0]]
        except Exception, reason: 
            self.childWidget_list[0].update_paint(self.PCal)
            #print 'no an24', Exception, reason
        else:
            if self.is_single_max ==False:
                for i in range(len(self.an24Dict)):
                    #print 'painting', time.time()
                    self.is_single_max = self.childWidget_list[i].update_paint(self.PCalList[i], self.an24Dict[self.an24List[i]])
                    if self.is_single_max == True:
                        self.single_widget = i 
                        self.childWidget_list[i].is_max = False
                        #print self.childWidget_list[i].is_max
                        self.widget_changed()
                        break
            else:
                self.childWidget_list[self.single_widget].update_paint(self.PCal , self.an24Dict[self.an24List[self.single_widget]])
        self.update_listWiget()
        self.update()
    
    def update_listWiget(self):
        try:
            self.listWidgetUuid.clear()
            self.listWidgetUuid.addItems(self.an24List)
        except Exception, reason:
            print 'update_listWiget failed.'
    def cal_widget_PCal(self, PCalList):
        amt =  len(PCalList)
        for i in range(amt):
            size = self.childWidget_list[i].size()
            PCalList[i].evment_calculation(size, self.xyRatio,  self.screen_ratio, self.FHR_limit)
        return PCalList
        
 
    def set_widget_position(self, widget_amt, single_widget):
        if widget_amt == 0:
            widget_amt = 1
        if single_widget:    
            self.childWidget_list[single_widget].setGeometry(QtCore.QRect(0, 0 , self.width(), self.height()))
            for i in range(16):
                if single_widget != i:
                    self.childWidget_list[i].hide()
        else:
            xList, yList, single_width, single_height = self.cal_widget_position(widget_amt)
            for i in range(widget_amt):
                self.childWidget_list[i].setGeometry(QtCore.QRect(xList[i], yList[i], single_width[i], single_height[i]))
                self.childWidget_list[i].show()
            for i in range(widget_amt, 16):
                self.childWidget_list[i].hide()
    
    
    def widget_changed(self):
        widget_amt = len(self.an24Dict)
        self.set_widget_position(widget_amt, self.single_widget)
        if self.single_widget:
            self.PCal.evment_calculation(self.size(), self.xyRatio,  self.screen_ratio, self.FHR_limit)
            self.childWidget_list[self.single_widget].resize_cal(self.PCal , self.an24Dict[self.an24List[self.single_widget]])
        else:
            self.PCalList = self.cal_widget_PCal(self.PCalList)
            for i in range(len(self.an24Dict)):
                self.childWidget_list[i].resize_cal(self.PCalList[i] , self.an24Dict[self.an24List[i]])        
            
    def button_position(self):
        if self.is_frame_shown:
            self.frame.setGeometry(QtCore.QRect(self.size().width()-188,70, 171,671))
        else:
            self.frame.setGeometry(QtCore.QRect(self.size().width(),70, 171,671))
            
        #self.frame_2.setGeometry(QtCore.QRect(0,0, self.size().width(),51))
#        self.label_user.setGeometry(QtCore.QRect(self.size().width()-40,10, 32,32))
#        self.label_battry.setGeometry(QtCore.QRect(self.size().width()-80,10, 32,32))
#        self.label_blueTooth.setGeometry(QtCore.QRect(self.size().width()-120,10, 32,32))
        
  
    def get_rest_time(self, start_time, all_battry_time):
        runTime=int(time.time()-start_time) 
        rest_battry_time = int(all_battry_time*3600 - runTime)
        self.update_rest_battry_time(rest_battry_time)
        Hour=rest_battry_time/3600
        Minute=(rest_battry_time%3600)/60
        Second=(rest_battry_time%3600)%60
        if Hour<10:
            Hour='0'+str(Hour)
        else:
            Hour=str(Hour)
        if Minute<10:
            Minute='0'+str(Minute)
        else:
            Minute=str(Minute)
        if Second<10:
            Second='0'+str(Second)
        else:
            Second=str(Second)
        return Hour, Minute, Second        
        
    @pyqtSignature("")
    def on_xscale1_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 1
        self.widget_changed()
        self.update()
    
    @pyqtSignature("")
    def on_xscale2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 2
        self.widget_changed()
        self.update()
    
    @pyqtSignature("")
    def on_xscale3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 3
        self.widget_changed()
        self.update()
    
#    @pyqtSignature("")
#    def on_pushSearch_clicked(self):
#        """
#        Slot documentation goes here.
#        """
#        uuid_Dict = self.d_c.get_online_p()
#        if uuid_Dict:
#            self.update_userList(uuid_Dict)
#            self.widget_changed()
#            self.update()
#        else:
#            print 'no patient online'
            
    def update_patient(self):
        uuid_Dict = self.d_c.get_online_p()        
        is_changed = self.update_userList(uuid_Dict)
        if is_changed:
            self.widget_changed()
            self.update()
        if not uuid_Dict:     
            pass
                 
    def start_detecting(self):
        self.timerPaint = QTimer()             
        QtCore.QObject.connect(self.timerPaint, SIGNAL("timeout()"),self.update_paint)
        self.timerOnline = QTimer()             
        QtCore.QObject.connect(self.timerOnline, SIGNAL("timeout()"),self.update_patient)
        self.timerPaint.start(2000)
        self.timerOnline.start(3000)
        
    def update_patient_info(self, dictChosen):
        try:
            self.label_name.setText(u'名字：'+dictChosen.patient.name)
            #self.label_age.setText(u'年龄：'+str(patient_info['age']))
            #self.label_weeks.setText(u'孕周：'+str(patient_info['weeks']))
            #self.label_outpatient.setText(u'门诊号：'+patient_info['outpatient_num'])
            self.label_hospitalization.setText(u'住院号：'+dictChosen.patient.hospitalization_num)
            self.label_bed.setText(u'病床号：'+dictChosen.patient.bed_num)
            #self.label_guardianship.setText(u'监护号：'+patient_info['guardianship_num'])
            self.update()
        except AttributeError, reason:
            self.label_name.setText(u'名字：')
            self.label_hospitalization.setText(u'住院号：')
            self.label_bed.setText(u'病床号：')
            self.update()
        
    @pyqtSignature("bool")    
    def on_pinTest_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        for key in self.an24Dict:
            run_chk = self.an24Dict[key].data_handler.run_chk    
            if run_chk != [0, 0, 0, 0, 0]:
                self.an24Dict[key].data_handler.run_chk  = [0, 0, 0, 0, 0]
                print self.an24Dict[key].data_handler.run_chk 
            else:
                self.an24Dict[key].data_handler.run_chk  = [0, 0, 1, 0, 1]
                print self.an24Dict[key].data_handler.run_chk 
    
    @pyqtSignature("bool")     
    def on_recvStop_clicked(self, checked): 
#        try:
#            nameChosen =self.an24Chosen['name']
#            self.an24Dict[nameChosen]
#        except KeyError, reason:
#            QtGui.QMessageBox.information( self, "notice", "please start detection first." )
#        else:
#            self.an24Dict[nameChosen].rawAN24.stop_recv()       
#            self.an24Dict.pop(nameChosen)
#            if self.an24Dict:
#                for key in self.an24Dict:
#                    self.an24Chosen['name'] = key
#                    self.an24Chosen['address'] = self.an24Dict[key].address
#                    break
#                self.update_button_look()
#                self.update_patient_info(self.an24Dict[self.an24Chosen['name']])
#            else:
#                self.an24Chosen = {}
#                self.update_button_look()
#                self.update_patient_info({})
            pass
            
    
    @pyqtSignature("")
    def on_pushButtonSettings_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.FHR_limit = DlgSettings.change_settings()
    
    @pyqtSignature("")
    def on_pushButtonAlarm_clicked(self):
        """
        Slot documentation goes here.
        """
        self.pushButtonAlarm.setStyleSheet("background-image: url(:/picture/imgs/normal.png);background-repeat:no-repeat;") 
        self.repaint()
        self.is_alarm = False  
    
    @pyqtSignature("")
    def on_pushExit_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()
    
    def closeEvent(self, event):
        print 'closed'
        event.accept()

    @pyqtSignature("")
    def on_pushMulti_clicked(self):
        """
        Slot documentation goes here.
        """
        self.is_single_max = False
        self.single_widget = ''
        self.widget_changed()
        self.update()
    
#    @pyqtSignature("")
#    def on_pushGetPatient_clicked(self):
#        """
#        Slot documentation goes here.
#        """
#        self.add_data()
#        self.widget_changed()
#        self.update()
#    
#  
#    def add_data(self):
#        uuid_Dict = self.d_c.get_online_p()
#        if uuid_Dict:
#            self.update_userList(uuid_Dict)
#            print 'patient list', self.an24List
#        else:
#            print 'no patient online'
#        
    def closeEvent(self, event):
        for uuid in self.an24List:
            #another way: pop the instance of 
            self.an24Dict.pop(uuid)
            #self.an24Dict[uuid].data_handler.download_thread(uuid, 'close')
        self.an24List = []    
    def update_userList(self, uuid_Dict):
        is_changed = False        
        for i in range(len(self.an24List))[::-1]:
            if self.an24List[i] not in  uuid_Dict:
                self.an24Dict.pop(self.an24List[i])
                self.an24List.pop(i)
                self.PCalList.pop(i)
                is_changed = True
        for uuid in uuid_Dict:
            if uuid not in self.an24List:
                self.an24List.append(uuid)
                self.PCalList.append(PaintCalculation())
                self.an24Dict[uuid] = UiData(uuid, uuid_Dict[uuid])        
                self.an24Dict[uuid].start_time=time.time()
                self.an24Dict[uuid].data_handler.download_thread(uuid)
                is_changed = True
#                  真实流程
#                  self.an24Dict[self.an24List[i]].data_handler.download(self.an24List[i])
        return is_changed
                
    def cal_widget_position(self, widget_amt):
        size = self.size()
        height = size.height()
        width = size.width()
        interval = 10
        xList = []
        yList = []
        widthList = []
        heightList = []
        if widget_amt == 1:
            xList = [0]
            yList = [0]
            widthList = [width]
            heightList = [height]
            
        elif widget_amt == 2:
            single_width = ((width-3*interval))/2
            single_height = height-2*interval
            xList = [interval, interval*2+single_width]
            yList = [interval, interval]
            widthList = [single_width, single_width]
            heightList = [single_height, single_height]
            
        elif widget_amt ==3:
            single_width = ((width-4*interval))/3
            single_height = height-2*interval
            for i in range(3):
                xList.append(interval*(i+1) + single_width*i) 
                yList.append(interval)
                widthList.append(single_width)
                heightList.append(single_height)
                
        elif widget_amt ==4:
            single_width = (width-3*interval)/2
            single_height = (height-3*interval)/2            
            for i in range(2):
                xList.append(interval*(i+1) + single_width*i) 
                yList.append(interval)
                widthList.append(single_width)
                heightList.append(single_height)
            for i in range(2, 4):
                xList.append(interval*(i%2+1) + single_width*(i%2)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width)
                heightList.append(single_height)
                
        elif widget_amt ==5:
            single_width1 = (width-4*interval)/3
            single_width2 = (width-3*interval)/2
            single_height = (height-3*interval)/2            
            for i in range(3):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(3, 5):
                xList.append(interval*(i%3+1) + single_width2*(i%3)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width2)
                heightList.append(single_height)
            
        elif widget_amt ==6:
            single_width1 = (width-4*interval)/3
            single_height = (height-3*interval)/2            
            for i in range(3):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(3, 6):
                xList.append(interval*(i%3+1) + single_width1*(i%3)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width1)
                heightList.append(single_height)
        
        elif widget_amt ==7:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-4*interval)/3
            single_height = (height-3*interval)/2            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 7):
                xList.append(interval*(i%4+1) + single_width2*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width2)
                heightList.append(single_height)
        
        elif widget_amt ==8:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-5*interval)/4
            single_height = (height-3*interval)/2            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 8):
                xList.append(interval*(i%4+1) + single_width2*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width2)
                heightList.append(single_height)
        
        elif widget_amt ==9:
            single_width1 = (width-4*interval)/3
            single_width2 = (width-4*interval)/3
            single_height = (height-4*interval)/3            
            for i in range(3):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(3, 6):
                xList.append(interval*(i%3+1) + single_width2*(i%3)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width2)
                heightList.append(single_height)
            for i in range(6, 9):
                xList.append(interval*(i%3+1) + single_width2*(i%3)) 
                yList.append(interval*3 + single_height*2)
                widthList.append(single_width2)
                heightList.append(single_height)
        
        elif widget_amt ==10:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-4*interval)/3
            single_height = (height-4*interval)/3            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 7):
                xList.append(interval*(i%4+1) + single_width2*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width2)
                heightList.append(single_height)
            for i in range(7, 10):
                xList.append(interval*(i%7+1) + single_width2*(i%7)) 
                yList.append(interval*3 + single_height*2)
                widthList.append(single_width2)
                heightList.append(single_height)
        
        elif widget_amt ==11:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-4*interval)/3
            single_height = (height-4*interval)/3            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 8):
                xList.append(interval*(i%4+1) + single_width1*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(8, 11):
                xList.append(interval*(i%8+1) + single_width2*(i%8)) 
                yList.append(interval*3 + single_height*2)
                widthList.append(single_width2)
                heightList.append(single_height)
        
        elif widget_amt ==12:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-5*interval)/4
            single_height = (height-4*interval)/3            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 8):
                xList.append(interval*(i%4+1) + single_width1*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(8, 12):
                xList.append(interval*(i%8+1) + single_width2*(i%8)) 
                yList.append(interval*3 + single_height*2)
                widthList.append(single_width2)
                heightList.append(single_height)
        
        elif widget_amt ==13:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-2*interval)/1
            single_height = (height-5*interval)/4            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 8):
                xList.append(interval*(i%4+1) + single_width1*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(8, 12):
                xList.append(interval*(i%8+1) + single_width1*(i%8)) 
                yList.append(interval*3 + single_height*2)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(12, 13):
                xList.append(interval*(i%12+1) + single_width2*(i%12)) 
                yList.append(interval*4 + single_height*3)
                widthList.append(single_width2)
                heightList.append(single_height)
        
        elif widget_amt ==14:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-3*interval)/2
            single_height = (height-5*interval)/4            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 8):
                xList.append(interval*(i%4+1) + single_width1*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(8, 12):
                xList.append(interval*(i%8+1) + single_width1*(i%8)) 
                yList.append(interval*3 + single_height*2)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(12, 14):
                xList.append(interval*(i%12+1) + single_width2*(i%12)) 
                yList.append(interval*4 + single_height*3)
                widthList.append(single_width2)
                heightList.append(single_height)
        
        elif widget_amt ==15:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-4*interval)/3
            single_height = (height-5*interval)/4            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 8):
                xList.append(interval*(i%4+1) + single_width1*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(8, 12):
                xList.append(interval*(i%8+1) + single_width1*(i%8)) 
                yList.append(interval*3 + single_height*2)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(12, 15):
                xList.append(interval*(i%12+1) + single_width2*(i%12)) 
                yList.append(interval*4 + single_height*3)
                widthList.append(single_width2)
                heightList.append(single_height)
                
        elif widget_amt ==16:
            single_width1 = (width-5*interval)/4
            single_width2 = (width-5*interval)/4
            single_height = (height-5*interval)/4            
            for i in range(4):
                xList.append(interval*(i+1) + single_width1*i) 
                yList.append(interval)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(4, 8):
                xList.append(interval*(i%4+1) + single_width1*(i%4)) 
                yList.append(interval*2 + single_height)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(8, 12):
                xList.append(interval*(i%8+1) + single_width1*(i%8)) 
                yList.append(interval*3 + single_height*2)
                widthList.append(single_width1)
                heightList.append(single_height)
            for i in range(12, 16):
                xList.append(interval*(i%12+1) + single_width2*(i%12)) 
                yList.append(interval*4 + single_height*3)
                widthList.append(single_width2)
                heightList.append(single_height)
        return xList, yList, widthList,  heightList 
    
    


    def add_note(self):
        '''
        菜单中的具体action调用的函数
        '''
        try:
            print 'aaaaaaaaa'
            PCal = self.PCal
            
        except Exception, reason:
            print Exception, reason
        else:
            if self.single_widget:
                noteDict = self.an24Dict[self.an24List[self.single_widget]].noteDict
                count = xy2count(self,  self.cursor_pos.x(), PCal.start_count, PCal.unitXY['FHR'])
                note_y = self.cursor_pos.y()            
                note = DlgFillNote.fill_note()
                noteDict[count] = (note_y, note)
                self.repaint()   
 
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)    
    qTranslator = PyQt4.QtCore.QTranslator()
    qTranslator.load("./Chinese.qm")
    app.installTranslator(qTranslator)
    ist = Holter()
    app.installEventFilter(ist)    
    DlgSettings = Settings()
    ist.show()   
    ist.start_detecting()   

    sys.exit(app.exec_() )
    app.exec_()
    app.quit()
    
    
