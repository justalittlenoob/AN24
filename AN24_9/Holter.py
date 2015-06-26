# -*- coding: utf-8 -*-

"""
Module implementing Holter.
"""
import sys, PyQt4, winsound, time

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import (pyqtSignature, QTimer,  SIGNAL, QPropertyAnimation)
from Ui_Holter import Ui_Holter
from SeaAN24 import SeaAN24
from CntAN24 import CntAN24
from ChkAN24 import ChkAN24
from ChkAN24_Run import ChkAN24_Run
from PregSim import PregSim
from PaintRealTime import *
from FillPatient import  FillPatient

from UiAN24 import UiAN24

        
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
        self.an24Dict = {}
        self.xyRatio = 1
        self.is_soundOn = True
        self.an24Chosen = {}
        
        self.is_frame_shown = True
        #self.frame.hide()
        self.animation_hide = QPropertyAnimation(self.frame, "geometry")
        self.animation_hide.setDuration(500)
        self.animation_hide.setStartValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        self.animation_hide.setEndValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show = QPropertyAnimation(self.frame, "geometry")
        self.animation_show.setDuration(500)
        self.animation_show.setStartValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setEndValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        
    def paintEvent(self, event):        
        qp = PyQt4.QtGui.QPainter()       
        qp.begin(self)
        drawBackground(self, qp)
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
            if round(draw_current_time)%2 ==0 and end_count>=4:
                end_count = len(self.an24Dict[nameChosen].rawAN24.cache) -4
                draw_current_time -= 1
                Cache = Cache[0:-4]
            realFHR(self, qp, Cache,  end_count, self.xyRatio)
            realEHG(self, qp, Cache, end_count, self.xyRatio)
            realMHR(self, qp, Cache,  end_count, self.xyRatio)
            realMMov(self, qp, Cache,  end_count, self.xyRatio)
            realSNR(self, qp, Cache,  end_count, self.xyRatio)
            realEvent(self, qp, Cache,  end_count, self.xyRatio)           
            drawScales(self, qp, start_time,  draw_current_time,  end_count, self.xyRatio) 
            Hour, Minute, Second = self.get_rest_time(self.an24Dict[nameChosen].start_time,self.an24Dict[nameChosen].all_battry_time ) 
            #self.restTime.setText(u'电量剩余时间： ' + Hour+ ':'+Minute+ ':'+Second) 
            self.update_battry_pic(int(Hour))
        else:
            drawScales(self, qp)
        qp.end()
        
    
    def mousePressEvent(self, event):
        if not self.is_frame_shown:
            self.animation_show.start()
        else:
            self.animation_hide.start()
        self.is_frame_shown = not self.is_frame_shown 
    
    def resizeEvent(self, event):
        self.animation_hide.setStartValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        self.animation_hide.setEndValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setStartValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setEndValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        self.button_position()
        self.widget_resize()
        
    def update_paint(self):
        nameChosen =self.an24Chosen['name']
        #print self.an24Dict[nameChosen].name, self.an24Dict[nameChosen].is_checked
        if self.an24Dict[nameChosen].is_detecting ==True:
            self.an24Dict[nameChosen].draw_current_time = time.time()
            if self.an24Dict[nameChosen].rawAN24.low_battry[0]:
                print "low battry"
        else:
            pass
        self.print_second_cache()
        self.run_check()
        self.repaint()
               
        
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
    
    def widget_resize(self):
        self.frame_2.setGeometry(QtCore.QRect(0,0, self.size().width(),61))
        
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
            print '[update_button_look]you did not add the device',  reason
        else:
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
            print 'you did not add the device %s' % nameChosen,  reason
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
            print 'you did not add the device %s' %nameChosen,  reason
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
            print 'you did not add the device %s' %nameChosen,  reason
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
            print 'you did not add the device %s' %nameChosen,  reason
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
            print 'not run_check well', reason    
    
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
        self.repaint()

    
    @pyqtSignature("")
    def on_xscale2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 2
        self.repaint()
    
    @pyqtSignature("")
    def on_xscale3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 3
        self.repaint()
    
    @pyqtSignature("")
    def on_pushSearch_clicked(self):
        """
        Slot documentation goes here.
        """
        self.search_an24()
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
            print 'please choose one device'
        self.update_button_look()
        
    def connect_an24(self):
        try:
            nameChosen = self.an24Chosen['name']
        except KeyError,  reason:
            print 'connect failed', reason
        else:
            self.an24Dict[nameChosen].is_connected = DlgConnect.connect_start(self.an24Dict[nameChosen])
            if self.an24Dict[nameChosen].is_connected:
                self.label_blueTooth.setStyleSheet("background-image: url(:/picture/imgs/blueToothOk.png);background-repeat:no-repeat;") 
            
    def init_check_pin(self):
        try:
            nameChosen = self.an24Chosen['name']
        except KeyError, reason:
            print 'have not add an device', reason
        else:
            self.an24Dict[nameChosen].is_checked = DlgCheck.init_check(self.an24Dict[nameChosen])
            if self.an24Dict[nameChosen].is_checked:
                self.label_pin.setStyleSheet("background-image: url(:/picture/imgs/PinOk.png);background-repeat:no-repeat;") 
    def start_detecting(self):
        self.timerPaint = QTimer()             
        QtCore.QObject.connect(self.timerPaint, SIGNAL("timeout()"),self.update_paint)
        try:        
            nameChosen = self.an24Chosen['name']
        except KeyError, reason:
            print 'please add device first.', reason
        else:
            if self.an24Dict[nameChosen].is_checked:
                self.an24Dict[nameChosen].start_time=time.time()
                self.an24Dict[nameChosen].all_battry_time = self.an24Dict[nameChosen].rawAN24.battry            
                self.an24Dict[nameChosen].rawAN24.data_recv()
                self.timerPaint.start(2000)
                self.start_sound()
                self.an24Dict[nameChosen].is_detecting = True
                #print 'detect begin'
            else: 
                print 'check not past.'
    
    def play_sound(self):
        soundfile = "./sound/heartbeat.wav" 
        Cache = []
        try:
            nameChosen =self.an24Chosen['name']
            Cache = self.an24Dict[nameChosen].rawAN24.cache
        except Exception, reason:
            print 'no sound come'
            
        if (len(Cache)!=0) and (self.is_soundOn == True):
            heartRate=Cache[-1][0]
            if heartRate!=0:
                heartCycle=60000/heartRate
                self.timerSound.start(heartCycle)
                winsound.PlaySound(soundfile, winsound.SND_ASYNC) #立即返回，支持异步播放
            
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
        self.label_name.setText(u'名字：'+dictChosen.patient.name)
        #self.label_age.setText(u'年龄：'+str(patient_info['age']))
        #self.label_weeks.setText(u'孕周：'+str(patient_info['weeks']))
        #self.label_outpatient.setText(u'门诊号：'+patient_info['outpatient_num'])
        self.label_hospitalization.setText(u'住院号：'+dictChosen.patient.hospitalization_num)
        self.label_bed.setText(u'病床号：'+dictChosen.patient.bed_num)
        #self.label_guardianship.setText(u'监护号：'+patient_info['guardianship_num'])
        self.update()
        
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
                #print self.an24Dict[key].rawAN24.run_chk 
            else:
                self.an24Dict[key].rawAN24.run_chk  = [0, 0, 1, 0, 1]
                #print self.an24Dict[key].rawAN24.run_chk 
    
    @pyqtSignature("bool")     
    def on_recvStop_clicked(self, checked): 
        try:
            nameChosen =self.an24Chosen['name']
            self.an24Dict[nameChosen].rawAN24.stop_recv()
            self.sound_off()
            self.an24Dict[nameChosen].is_detecting = False
            self.an24Dict[nameChosen].draw_curruent_time = time.time()
            
            self.an24Dict.pop(nameChosen)
            for key in self.an24Dict:
                self.an24Chosen['name'] = key
                self.an24Chosen['address'] = self.an24Dict[key].address
                break
            self.update_button_look()
            self.update_patient_info(self.an24Dict[self.an24Chosen['name']])
        except AttributeError, reason:
            print 'please start a detection first.', reason
    
    @pyqtSignature("")
    def on_pushButton_fill_information_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            nameChosen =self.an24Chosen['name']
            an24_chosen = self.an24Dict[nameChosen]
        except KeyError, reason:
            print 'start AN24 First', reason
        else:
            patient_info = DlgFillPatient.fill_in_information()
            if patient_info:
                self.an24Dict[nameChosen].patient.name = patient_info['name']
                self.an24Dict[nameChosen].patient.age = patient_info['age']
                self.an24Dict[nameChosen].patient.weeks = patient_info['weeks']
                self.an24Dict[nameChosen].patient.outpatient_num = patient_info['outpatient_num']
                self.an24Dict[nameChosen].patient.hospitalization_num = patient_info['hospitalization_num']
                self.an24Dict[nameChosen].patient.bed_num = patient_info['bed_num']
                self.an24Dict[nameChosen].patient.guardianship_num = patient_info['guardianship_num']
                self.update_patient_info(self.an24Dict[nameChosen])
    

        
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
    DlgPregSim = PregSim()
    ist.show()
    sys.exit(app.exec_())
    

