# -*- coding: utf-8 -*-

"""
Module implementing Holter.
"""
import sys, PyQt4, winsound, time

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import (pyqtSignature, QTimer,  SIGNAL, QPropertyAnimation, Qt)
from Ui_Holter import Ui_Holter
from SeaAN24 import SeaAN24
from CntAN24 import CntAN24
from ChkAN24 import ChkAN24
from ChkAN24_Run import ChkAN24_Run
from PregSim import PregSim
from PaintRealTime import *
from FillPatient import  FillPatient
from FillNote import FillNote
from UiAN24 import UiAN24
from pregClient import send2server
from Settings import  *
        
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
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.createContextMenu()
        self.create_animation()   
        self.init_var()
        self.init_settings() 
        self.paint_calculation()
        
    
    def init_var(self):
        self.an24Dict = {}        
        self.an24Chosen = {}    
    
    def init_settings(self):
        self.xyRatio = 1
        self.screen_ratio = 0.8
        self.is_soundOn = True
        self.FHR_limit = [80, 110,140, 180]
        self.is_alarm = False
        self.is_frame_shown = True
    
    def paint_calculation(self):
        self.window_rect = self.size()
        self.bg_scaleY = {'FHR':cal_ScaleY(self.window_rect,'FHR'), 
                            'EHG':cal_ScaleY(self.window_rect,'EHG'), 
                            'MHR':cal_ScaleY( self.window_rect,'MHR'), 
                            'MMov':cal_ScaleY(self.window_rect,'MMov'), 
                            'SNR':cal_ScaleY(self.window_rect,'SNR')
                            }
        self.bg_rgb = {'EHG':(255, 255, 255, 200), 
                            'MHR':(191, 229, 253, 150), 
                            'MMov':(220, 248, 146, 100), 
                            'SNR':(251, 249, 116, 100)
                            }
        self.bg_rect = {'FHR':cal_rect(self.window_rect, self.bg_scaleY['FHR']) , 
                            'EHG':cal_rect(self.window_rect, self.bg_scaleY['EHG']) , 
                            'MHR':cal_rect(self.window_rect, self.bg_scaleY['MHR']) , 
                            'MMov':cal_rect(self.window_rect, self.bg_scaleY['MMov']) , 
                            'SNR':cal_rect(self.window_rect, self.bg_scaleY['SNR']) 
                            }
        self.FHR_rect = cal_FHRrect(self.window_rect, self.bg_scaleY['FHR'], self.FHR_limit)
        self.FHR_rgb = [(247, 220, 230, 200), 
                            (255, 251, 190, 160), 
                            (255, 255, 255, 200), 
                            (255, 251, 190, 160), 
                            (247, 220, 230, 200)
                            ]
        width = self.window_rect.width()
        self.ytext_info = {'FHR':[50, 10, 5], 
                                'EHG':[0, 25,width-30], 
                                'MHR':[40, 10, 5]
                                }    
        self.xstep = self.bg_scaleY['FHR'][2]*2                            
        self.unitXY = {'FHR': cal_unitXY('FHR',self.xstep, self.bg_scaleY['FHR'], self.xyRatio), 
                        'EHG': cal_unitXY('EHG',self.xstep, self.bg_scaleY['EHG'], self.xyRatio), 
                        'MHR': cal_unitXY('MHR',self.xstep, self.bg_scaleY['MHR'], self.xyRatio), 
                        'MMov': cal_unitXY('MMov',self.xstep, self.bg_scaleY['MMov'], self.xyRatio), 
                        'SNR': cal_unitXY('SNR',self.xstep, self.bg_scaleY['SNR'], self.xyRatio) 
                        }
        self.line_rgb = {'FHR':(35, 78, 220), 
                            'EHG':(0, 0, 0), 
                            'MHR':(148, 48, 34), 
                            'MMov':(116, 186, 106), 
                            'SNR':(144, 159, 248, 100), 
                            'Event': (204, 138, 138)
                            }
        self.all_count = cal_realCount(self.window_rect, self.xstep, self.xyRatio, 1)
        self.pen ={'FHR': QtGui.QPen(QtGui.QColor(35, 78, 220), 1, QtCore.Qt.SolidLine), 
                        'EHG':QtGui.QPen(QtGui.QColor(0, 0, 0), 1, QtCore.Qt.SolidLine), 
                        'MHR':QtGui.QPen(QtGui.QColor(148, 48, 34), 1, QtCore.Qt.SolidLine), 
                        'MMov':QtGui.QPen(QtGui.QColor(116, 186, 106), 1, QtCore.Qt.SolidLine), 
                        'SNR': QtGui.QPen(QtGui.QColor(144, 159, 248, 100), 1, QtCore.Qt.SolidLine), 
                        'Event':QtGui.QPen(QtGui.QColor(204, 138, 138), 1, QtCore.Qt.SolidLine) 
                        }
        
        
    def create_animation(self):
        self.animation_hide = QPropertyAnimation(self.frame, "geometry")
        self.animation_hide.setDuration(500)
#        self.animation_hide.setStartValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
#        self.animation_hide.setEndValue(PyQt4.QtCore.QRect(self.size().width()-100, 70, 171, 671))
        self.animation_show = QPropertyAnimation(self.frame, "geometry")
        self.animation_show.setDuration(500)
#        self.animation_show.setStartValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
#        self.animation_show.setEndValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        
    def paintEvent(self, event):        
        qp = PyQt4.QtGui.QPainter()       
        qp.begin(self)
        paintBg(self, qp, self.window_rect, self.bg_rgb, self.bg_rect, self.bg_scaleY, self.FHR_rect, self.FHR_rgb, self.ytext_info)
        try:
            nameChosen =self.an24Chosen['name']
        except AttributeError, reason:
            is_detecting = False
            #print 'paintEvent-> you have not add an divice. <reason>', reason
        except KeyError, reason:
            is_detecting = False
            #print 'paintEvent-> you need to choose one divice. <reason>', reason
        else:
            is_detecting = self.an24Dict[nameChosen].is_detecting
        
        if is_detecting:
            draw_current_time = self.an24Dict[nameChosen].draw_current_time
            Cache = self.an24Dict[nameChosen].rawAN24.cache
            start_time = self.an24Dict[nameChosen].start_time
            end_count = len(self.an24Dict[nameChosen].rawAN24.cache)
            realCount = cal_realCount(self.window_rect, self.xstep, self.xyRatio, self.screen_ratio)
            if end_count>realCount:
                start_count=end_count-int(realCount)
            else:
                start_count = 0
            note = self.an24Dict[nameChosen].note
            realtime_monitor(self, qp, Cache, start_count, end_count, self.bg_scaleY,  self.unitXY, self.pen)
#            realFHR(self, qp,  Cache, start_count, end_count, self.bg_scaleY['FHR'],  self.unitXY['FHR'], self.line_rgb['FHR'])
#            realEHG(self, qp, Cache, start_count, end_count, self.bg_scaleY['EHG'],  self.unitXY['EHG'], self.line_rgb['EHG'])
#            realMHR(self, qp, Cache, start_count, end_count, self.bg_scaleY['MHR'],  self.unitXY['MHR'], self.line_rgb['MHR'])
#            realMMov(self, qp, Cache, start_count, end_count, self.bg_scaleY['MMov'],  self.unitXY['MMov'], self.line_rgb['MMov'])
#            realSNR(self, qp, Cache, start_count, end_count, self.bg_scaleY['SNR'],  self.unitXY['SNR'], self.line_rgb['SNR'])
#            realEvent(self, qp, Cache, start_count, end_count, self.unitXY['FHR'], self.line_rgb['Event'])       
            drawXScale(self, qp,  self.window_rect, self.unitXY['FHR'], self.all_count, start_count, end_count , self.xyRatio, start_time)
            drawNote(self, qp, self.unitXY['FHR'], self.all_count,  start_count,  end_count, self.xyRatio, note)
            Hour, Minute, Second = self.get_rest_time(self.an24Dict[nameChosen].start_time,self.an24Dict[nameChosen].all_battry_time ) 
            #self.restTime.setText(u'电量剩余时间： ' + Hour+ ':'+Minute+ ':'+Second) 
            self.update_battry_pic(int(Hour))
        else:
            drawXScale(self, qp,  self.window_rect, self.unitXY['FHR'], self.all_count,  self.xyRatio)
            #drawXScale(self, qp, self.unitXY['FHR'])
        qp.end()
        
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if not self.is_frame_shown:
                self.animation_show.start()
            else:
                self.animation_hide.start()
            self.is_frame_shown = not self.is_frame_shown 
    
    def resizeEvent(self, event):
        self.paint_calculation()
        self.animation_hide.setStartValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        self.animation_hide.setEndValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setStartValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setEndValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        self.button_position()
        print 'resize'
        
    def update_paint(self):
        try:
            nameChosen =self.an24Chosen['name']
        except KeyError, reason:
            self.repaint()
        else:
            #print self.an24Dict[nameChosen].name, self.an24Dict[nameChosen].is_checked
            if self.an24Dict[nameChosen].is_detecting ==True:
                self.listen_alarm()
                self.an24Dict[nameChosen].draw_current_time = time.time()
                if self.an24Dict[nameChosen].rawAN24.low_battry[0]:
                    message = QtGui.QMessageBox.warning( self, "notice", "warning,low battery.", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No )
                self.print_second_cache()
                self.run_check()
                self.listen_info()
                self.update_patient_info(self.an24Dict[nameChosen])
                self.repaint()
               
    def listen_info(self):
        if self.an24Dict:
            for key in self.an24Dict:
                if self.an24Dict[key].handler.syni:
                    try:
                        self.an24Dict[key].patient.person_num = self.an24Dict[key].handler.syni['person_num']
                    except KeyError, reason:
                        pass
                    try:
                        self.an24Dict[key].patient.name = self.an24Dict[key].handler.syni['name']
                    except KeyError, reason:
                        pass
                    try:
                        self.an24Dict[key].patient.age = self.an24Dict[key].handler.syni['age']
                    except KeyError, reason:
                        pass
                    try:
                        self.an24Dict[key].patient.weeks = self.an24Dict[key].handler.syni['weeks']
                    except KeyError, reason:
                        pass
                    try:
                        self.an24Dict[key].patient.outpatient_num = self.an24Dict[key].handler.syni['outpatient_num']
                    except KeyError, reason:
                        pass
                    try:
                        self.an24Dict[key].patient.hospitalization_num = self.an24Dict[key].handler.syni['hospitalization_num']
                    except KeyError, reason:
                        pass
                    try:
                        self.an24Dict[key].patient.bed_num = self.an24Dict[key].handler.syni['bed_num']
                    except KeyError, reason:
                        pass
                    try:
                        self.an24Dict[key].patient.guardianship_num = self.an24Dict[key].handler.syni['guardianship_num']
                    except KeyError, reason:
                        pass            
        
    def update_battry_pic(self, Hour):
        if Hour>17.5:
            self.label_battry.setStyleSheet("background-image: url(:/picture/imgs/power7.png);background-repeat:no-repeat;") 
        elif Hour>15:
            self.label_battry.setStyleSheet("background-image: url(:/picture/imgs/power6.png);background-repeat:no-repeat;") 
        elif Hour>12.5:
            self.label_battry.setStyleSheet("background-image: url(:/picture/imgs/power5.png);background-repeat:no-repeat;") 
        elif Hour>10:
            self.label_battry.setStyleSheet("background-image: url(:/picture/imgs/power4.png);background-repeat:no-repeat;") 
        elif Hour>7.5:
            self.label_battry.setStyleSheet("background-image: url(:/picture/imgs/power3.png);background-repeat:no-repeat;") 
        elif Hour>5:
            self.label_battry.setStyleSheet("background-image: url(:/picture/imgs/power2.png);background-repeat:no-repeat;") 
        elif Hour>2.5:
            self.label_battry.setStyleSheet("background-image: url(:/picture/imgs/power1.png);background-repeat:no-repeat;") 
        else:
            self.label_battry.setStyleSheet("background-image: url(:/picture/imgs/power0.png);background-repeat:no-repeat;") 

    def button_position(self):
        if self.is_frame_shown:
            self.frame.setGeometry(QtCore.QRect(self.size().width()-188,70, 171,671))
        else:
            self.frame.setGeometry(QtCore.QRect(self.size().width(),70, 171,671))
            
        self.frame_2.setGeometry(QtCore.QRect(0,0, self.size().width(),51))
        self.label_user.setGeometry(QtCore.QRect(self.size().width()-40,10, 32,32))
        self.label_battry.setGeometry(QtCore.QRect(self.size().width()-80,10, 32,32))
        self.label_blueTooth.setGeometry(QtCore.QRect(self.size().width()-120,10, 32,32))
        
    def update_button_look(self):
        device_button_list = [self.device_1, self.device_2,self.device_3,self.device_4]
        i = 0
        m = 0
        try:
            for device in device_button_list:
                device.setText(str(i+1))
                i+=1
            for key in self.an24Dict:
                device_button_list[m].setText(key)
                m+=1
        except Exception, reason:
            print 'button text error', reason
        
        j = 0
        try:
            nameChosen = self.an24Chosen['name'] 
        except KeyError, reason:
            nameChosen = ''
        for device in device_button_list:
            if  str(device.text())==nameChosen:
                device.setStyleSheet("background-image: url(:/picture/imgs/button_1234_chosen.png);background-repeat:no-repeat;")   
            elif j<m:
                device.setStyleSheet("background-image: url(:/picture/imgs/button_1234.png);background-repeat:no-repeat;")   
            else:
                device.setStyleSheet("background-image: url(:/picture/imgs/button_1234_blank.png);background-repeat:no-repeat;")   
            j+=1
    
    @pyqtSignature("")
    def on_device_1_clicked(self):
        nameChosen = str(self.device_1.text())
        try:
            addressChosen = self.an24Dict[nameChosen].address
        except KeyError, reason:
            QtGui.QMessageBox.information( self, "notice", 'you did not add the device %s' % nameChosen)
        else:
            self.an24Chosen['name'] = nameChosen
            self.an24Chosen['address'] = addressChosen
            self.update_button_look()
            self.update_patient_info(self.an24Dict[nameChosen])
    
    @pyqtSignature("")
    def on_device_2_clicked(self):
        nameChosen = str(self.device_2.text())
        try:
            addressChosen = self.an24Dict[nameChosen].address
        except KeyError, reason:
            QtGui.QMessageBox.information( self, "notice", 'you did not add the device %s' % nameChosen)
        else:
            self.an24Chosen['name'] = nameChosen
            self.an24Chosen['address'] = addressChosen
            self.update_button_look()
            self.update_patient_info(self.an24Dict[nameChosen])
    @pyqtSignature("")
    def on_device_3_clicked(self):
        nameChosen = str(self.device_3.text())
        try:
            addressChosen = self.an24Dict[nameChosen].address
        except KeyError, reason:
            QtGui.QMessageBox.information( self, "notice", 'you did not add the device %s' % nameChosen)
        else:
            self.an24Chosen['name'] = nameChosen
            self.an24Chosen['address'] = addressChosen
            self.update_button_look()
            self.update_patient_info(self.an24Dict[nameChosen])
    
    @pyqtSignature("")
    def on_device_4_clicked(self):
        nameChosen = str(self.device_4.text())
        try:
            addressChosen = self.an24Dict[nameChosen].address
        except KeyError, reason:
            QtGui.QMessageBox.information( self, "notice", 'you did not add the device %s' % nameChosen)
        else:
            self.an24Chosen['name'] = nameChosen
            self.an24Chosen['address'] = addressChosen
            self.update_button_look()
            self.update_patient_info(self.an24Dict[nameChosen])
        
    def print_second_cache(self):
        try:
            nameChosen =self.an24Chosen['name']
            Cache = self.an24Dict[nameChosen].rawAN24.cache
            end_count = len(self.an24Dict[nameChosen].rawAN24.cache)
            end_count_pre = self.an24Dict[nameChosen].end_count_pre
            #print 'gotdata--start:', end_count_pre, Cache[end_count_pre:end_count], 'end:', end_count
            self.an24Dict[nameChosen].end_count_pre = end_count
        except Exception, reason:
            print 'can not print cache now.', reason    
    
    def run_check(self):
        try:
            DlgCheck_Run_List = [DlgCheck_Run_0, DlgCheck_Run_1, DlgCheck_Run_2, DlgCheck_Run_3]
            i = 0
            for key in self.an24Dict:
                an24Dict_check = self.an24Dict[key]
                self.an24Dict[key].is_checked = DlgCheck_Run_List[i].run_check(an24Dict_check)
                i+=1
        except Exception, reason:
            QtGui.QMessageBox.information( self, "notice", 'not run_check well')    
    
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
    
    def update_rest_battry_time(self, rest_battry_time):
        nameChosen =self.an24Chosen['name']
        self.an24Dict[nameChosen].rest_battry_time = rest_battry_time
        
    @pyqtSignature("")
    def on_xscale1_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 1
        self.paint_calculation()
        self.repaint()

    
    @pyqtSignature("")
    def on_xscale2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 2
        self.paint_calculation()
        self.repaint()
    
    @pyqtSignature("")
    def on_xscale3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 3
        self.paint_calculation()
        self.repaint()
    
    @pyqtSignature("")
    def on_pushSearch_clicked(self):
        """
        Slot documentation goes here.
        """
        self.search_an24()
        self.fill_info()
        self.connect_an24()
        self.init_check_pin()
        self.start_detecting()
        
    def search_an24(self):
        self.an24Chosen = DlgSearch.scan_AN24()
        if self.an24Chosen:
            nameChosen = self.an24Chosen['name']
            addrChosen = self.an24Chosen['address']
            self.an24Dict[nameChosen] = UiAN24(nameChosen, addrChosen)
            print 'you add device %s.' %self.an24Dict[nameChosen].name, self.an24Dict
        else:
            QtGui.QMessageBox.information( self, "notice", 'please choose one device' )
        self.update_button_look()
        
    def fill_info(self):
        try:
            nameChosen =self.an24Chosen['name']
            an24_chosen = self.an24Dict[nameChosen]
        except KeyError, reason:
            QtGui.QMessageBox.information( self, 'notice',  'start AN24 First')
        else:
            self.an24Dict[nameChosen].patient = DlgFillPatient.fill_in_information(self.an24Dict[nameChosen].patient)
            if self.an24Dict[nameChosen].patient:
                self.an24Dict[nameChosen].handler.handle(self.an24Dict[nameChosen].patient, 0)
                self.update_patient_info(self.an24Dict[nameChosen])   
                self.infoed = True
        
    def connect_an24(self):
        try:
            self.an24Chosen['name']
        except KeyError,  reason:
            QtGui.QMessageBox.information( self, "notice", "connecte failed." )
        else:
            nameChosen = self.an24Chosen['name']
            if self.an24Dict[nameChosen].patient.person_num !='': 
                self.an24Dict[nameChosen].is_connected = DlgConnect.connect_start(self.an24Dict[nameChosen])
                if self.an24Dict[nameChosen].is_connected:
                    self.label_blueTooth.setStyleSheet("background-image: url(:/picture/imgs/blueToothOk.png);background-repeat:no-repeat;") 
                else:
                    print 'you have to fill in patient information before start.'
    def init_check_pin(self):
        try:
            self.an24Chosen['name']
        except KeyError, reason:
            QtGui.QMessageBox.information( self, "notice", "did not add an device." )
        else:
            nameChosen = self.an24Chosen['name']
            if self.an24Dict[nameChosen].is_connected:
                self.an24Dict[nameChosen].is_checked = DlgCheck.init_check(self.an24Dict[nameChosen])
            
    def start_detecting(self):
        self.timerPaint = QTimer()             
        QtCore.QObject.connect(self.timerPaint, SIGNAL("timeout()"),self.update_paint)
        try:        
            self.an24Chosen['name']
        except KeyError, reason:
            QtGui.QMessageBox.information( self, "notice", "please add device first." )
        else:
            nameChosen = self.an24Chosen['name']
            if self.an24Dict[nameChosen].is_checked:
                self.an24Dict[nameChosen].start_time=time.time()
                self.an24Dict[nameChosen].all_battry_time = self.an24Dict[nameChosen].rawAN24.battry            
                self.an24Dict[nameChosen].rawAN24.data_recv(self.an24Dict[nameChosen].handler.handle)
                self.timerPaint.start(2000)
                self.start_sound()
                self.an24Dict[nameChosen].is_detecting = True
                #print 'detect begin'
            else: 
                if self.an24Dict[nameChosen].is_infoed:
                    QtGui.QMessageBox.information( self, "notice", "pin check not pass." )
    
    def play_sound(self):
        soundfile = "./sound/heartbeat.wav" 
        Cache = []
        try:
            nameChosen =self.an24Chosen['name']            
        except KeyError, reason:
            print 'have not chosen a device'
        else:  
            Cache = self.an24Dict[nameChosen].rawAN24.cache  
            if (len(Cache)!=0) and (self.is_soundOn == True):
                heartRate=Cache[-1][0]
                if heartRate!=0:
                    heartCycle=60000/heartRate
                    winsound.PlaySound(soundfile, winsound.SND_ASYNC) #立即返回，支持异步播放
                    self.timerSound.start(heartCycle)
                    
            
    def sound_on(self):
        self.is_soundOn = True
        
    def sound_off(self):
        self.is_soundOn = False
    
    def start_sound(self):
        self.timerSound=QTimer()
        QtCore.QObject.connect(self.timerSound, SIGNAL("timeout()"),self.play_sound) 
        self.sound_on()
        self.timerSound.start(500)
        
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
    
    def listen_alarm(self):
        try:        
            self.an24Chosen['name']
        except KeyError, reason:
            r = QtGui.QMessageBox.warning( self, "warning", "FHR alarm error.", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No )
        else:
            nameChosen = self.an24Chosen['name']
            i = 0
            try:
                Cache = self.an24Dict[nameChosen].rawAN24.cache[-240:-1]
                for cache in Cache:
                    if cache[0]>self.FHR_limit[2] or cache[0]<self.FHR_limit[1]:
                        i+=1
                    else:
                        pass
            except e, r:
                print 'FHR_alarm error,not enough cache', reason
            else:
                if i>=230:
                    self.is_alarm = True
                if self.is_alarm:
                    self.sound_off()
                    sound = "./sound/beep.wav" 
                    winsound.PlaySound(sound, winsound.SND_ASYNC) #立即返回，支持异步播放
                    self.pushButtonAlarm.setStyleSheet("background-image: url(:/picture/imgs/alarm.png);background-repeat:no-repeat;") 
                    
    @pyqtSignature("bool")    
    def on_pushSoundSwitch_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        try:
            is_soundOn = self.is_soundOn
        except AttributeError, reason:
            print 'can not switch sound', reason
        else:
            if is_soundOn:
                self.sound_off()
            else:
                self.sound_on()
        
    @pyqtSignature("bool")
    def on_visualChange_clicked(self, checked):
        """
        Slot documentation goes here.
        """  
        nameChosen =self.an24Chosen['name']
        an24Dict_chosen = self.an24Dict[nameChosen]
        self.hide()
        DlgPregSim.switch2_simple(an24Dict_chosen)
        self.show()
    
    @pyqtSignature("bool")    
    def on_pinTest_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        for key in self.an24Dict:
            run_chk = self.an24Dict[key].rawAN24.run_chk    
            if run_chk != [0, 0, 0, 0, 0]:
                self.an24Dict[key].rawAN24.run_chk  = [0, 0, 0, 0, 0]
                print self.an24Dict[key].rawAN24.run_chk 
            else:
                self.an24Dict[key].rawAN24.run_chk  = [0, 0, 1, 0, 1]
                print self.an24Dict[key].rawAN24.run_chk 
    
    @pyqtSignature("bool")     
    def on_recvStop_clicked(self, checked): 
        try:
            nameChosen =self.an24Chosen['name']
            self.an24Dict[nameChosen]
        except KeyError, reason:
            QtGui.QMessageBox.information( self, "notice", "please start detection first." )
        else:
            self.an24Dict[nameChosen].rawAN24.stop_recv()       
            self.an24Dict.pop(nameChosen)
            if self.an24Dict:
                for key in self.an24Dict:
                    self.an24Chosen['name'] = key
                    self.an24Chosen['address'] = self.an24Dict[key].address
                    break
                self.update_button_look()
                self.update_patient_info(self.an24Dict[self.an24Chosen['name']])
            else:
                self.an24Chosen = {}
                self.sound_off()
                self.update_button_look()
                self.update_patient_info({})
            
    
    @pyqtSignature("")
    def on_pushButton_fill_information_clicked(self):
        """
        Slot documentation goes here.
        """
        self.fill_info()
    
    @pyqtSignature("")
    def on_pushButtonSettings_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.FHR_limit = DlgSettings.change_settings()
        self.paint_calculation()
    
    @pyqtSignature("")
    def on_pushButtonAlarm_clicked(self):
        """
        Slot documentation goes here.
        """
        self.pushButtonAlarm.setStyleSheet("background-image: url(:/picture/imgs/normal.png);background-repeat:no-repeat;") 
        self.repaint()
        self.is_alarm = False  
        self.sound_on()
    
    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
    
    def showContextMenu(self, pos):
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu = QtGui.QMenu(self)
        self.actionA = self.contextMenu.addAction(u'添加注释')
        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.actionA.triggered.connect(self.add_note)
        
        self.cursor_pos = pos
        self.contextMenu.move(self.pos() +self.cursor_pos)
        self.contextMenu.show()

    def add_note(self):
        '''
        菜单中的具体action调用的函数
        '''
        try:
            nameChosen =self.an24Chosen['name']
        except AttributeError, reason:
            is_detecting = False
            #print 'paintEvent-> you have not add an divice. <reason>', reason
        except KeyError, reason:
            is_detecting = False
            #print 'paintEvent-> you need to choose one divice. <reason>', reason
        else:
            is_detecting = self.an24Dict[nameChosen].is_detecting
        
        if is_detecting:
            draw_current_time = self.an24Dict[nameChosen].draw_current_time
            end_count = len(self.an24Dict[nameChosen].rawAN24.cache)
            real_count = cal_realCount(self.window_rect, self.xstep, self.xyRatio, self.screen_ratio)
            if end_count>real_count:
                start_count=end_count-int(real_count)
            else:
                start_count = 0
            note= self.an24Dict[nameChosen].note
            count = xy2count(self,  self.cursor_pos.x(), start_count, self.unitXY['FHR'])
            note_y = self.cursor_pos.y()/float(self.height())            
            note_text = DlgFillNote.fill_note()
            self.an24Dict[nameChosen].note.append([count, note_y, note_text])
            self.an24Dict[nameChosen].handler.handle([count, note_y, note_text], 2)
            self.repaint()
        
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)    
    qTranslator = PyQt4.QtCore.QTranslator()
    qTranslator.load("./Chinese.qm")
    app.installTranslator(qTranslator)
    ist = Holter()    
    DlgSearch = SeaAN24()
    DlgConnect = CntAN24()
    DlgCheck = ChkAN24()
    DlgCheck_Run_0 = ChkAN24_Run()
    DlgCheck_Run_1 = ChkAN24_Run()
    DlgCheck_Run_2 = ChkAN24_Run()
    DlgCheck_Run_3 = ChkAN24_Run()
    DlgFillPatient = FillPatient()
    DlgFillNote = FillNote()
    DlgPregSim = PregSim()
    DlgSettings = Settings()
    ist.show()
    sys.exit(app.exec_())
    
    
