# -*- coding: utf-8 -*-

"""
Module implementing Holter.
"""
import sys, PyQt4, winsound

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import (pyqtSignature, QTimer,  SIGNAL)
from Ui_Holter import Ui_Holter
from SeaAN24 import SeaAN24
from CntAN24 import CntAN24
from ChkAN24 import ChkAN24
from ChkAN24_Run import ChkAN24_Run
from PregSim import PregSim
from PaintRealTime import *

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
        self.end_count_pre = 0
        
    def paintEvent(self, event):
        qp = PyQt4.QtGui.QPainter()       
        qp.begin(self)
        drawBackground(self, qp)
        try:
            is_checked = self.is_checked
        except Exception, reason:
            is_checked = False
            drawScales(self, qp)
        
        if is_checked:            
            nameChosen =self.an24Chosen['name']
            Cache = self.an24Dict[nameChosen].rawAN24.cache
            start_time = self.an24Dict[nameChosen].start_time
            end_count = len(self.an24Dict[nameChosen].rawAN24.cache)
            realFHR(self, qp, Cache,  end_count, self.xyRatio)
            realEHG(self, qp, Cache, end_count, self.xyRatio)
            realMHR(self, qp, Cache,  end_count, self.xyRatio)
            realMMov(self, qp, Cache,  end_count, self.xyRatio)
            realSNR(self, qp, Cache,  end_count, self.xyRatio)
            realEvent(self, qp, Cache,  end_count, self.xyRatio)           
            drawScales(self, qp, start_time,  end_count, self.xyRatio) 
            Hour, Minute, Second = self.get_rest_time(self.an24Dict[nameChosen].start_time,self.an24Dict[nameChosen].all_battry_time ) 
            self.restTime.setText(u'电量剩余时间： ' + Hour+ ':'+Minute+ ':'+Second)            
        qp.end()
        self.button_position()
    def update_paint(self):
        self.print_second_cache()
        self.run_check()
        self.repaint()
    
    def button_position(self):
        self.visualChange.setGeometry(QtCore.QRect(self.size().width()*0.95-60, 50, 61, 51))
        self.restTime.setGeometry(QtCore.QRect(self.size().width()*0.95-261,10, 301, 31))
        self.xscale1.setGeometry(QtCore.QRect(self.size().width()*0.95-52,120, 41, 41))
        self.xscale2.setGeometry(QtCore.QRect(self.size().width()*0.95-52,180, 41, 41))
        self.xscale3.setGeometry(QtCore.QRect(self.size().width()*0.95-52,240, 41, 41))
        
    def print_second_cache(self):
        try:
            nameChosen =self.an24Chosen['name']
            Cache = self.an24Dict[nameChosen].rawAN24.cache
            end_count = len(self.an24Dict[nameChosen].rawAN24.cache)
            print 'gotdata--start:', self.end_count_pre, Cache[self.end_count_pre:end_count], 'end:', end_count
            self.end_count_pre = end_count
        except Exception, reason:
            print 'can not print cache now.', reason    
    
    def run_check(self):
        try:
            nameChosen =self.an24Chosen['name']
            run_chk = self.an24Dict[nameChosen].rawAN24.run_chk
            an24Dict_chosen = self.an24Dict[nameChosen]
            if run_chk == [0, 0, 0, 0, 0]:
                pass
            else:
                DlgCheck_Run.run_check(an24Dict_chosen)
                print 'checking pin'
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
        self.an24Chosen = DlgSearch.scan_AN24()
        if self.an24Chosen:
            nameChosen = self.an24Chosen['name']
            addrChosen = self.an24Chosen['address']
            self.an24Dict[nameChosen] = UiAN24(nameChosen, addrChosen)
            print self.an24Dict[nameChosen].name, self.an24Dict
        else:
            print 'please choose one device'
            
            
    @pyqtSignature("")
    def on_pushConnect_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            nameChosen = self.an24Chosen['name']
            is_connected = DlgConnect.connect_start(self.an24Dict[nameChosen])
            print 'connected?', is_connected
        except Exception,  reason:
            print 'connect failed', reason

    
    @pyqtSignature("")
    def on_pushCheck_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            nameChosen = self.an24Chosen['name']
            self.is_checked = DlgCheck.init_check(self.an24Dict[nameChosen])
            print 'device pin has been checked?', self.is_checked
        except Exception, reason:
            print reason
    
    
    @pyqtSignature("")
    def on_pushStart_clicked(self):
        """
        Slot documentation goes here.
        """
        self.timerPaint = QTimer()             
        QtCore.QObject.connect(self.timerPaint, SIGNAL("timeout()"),self.update_paint)        
        nameChosen = self.an24Chosen['name']
        if self.is_checked:
            self.an24Dict[nameChosen].start_time=time.time()
            self.an24Dict[nameChosen].all_battry_time = self.an24Dict[nameChosen].rawAN24.battry            
            self.an24Dict[nameChosen].rawAN24.data_recv()
            self.timerPaint.start(1000)
            self.start_sound()
            print 'detect begin'
        else: 
            print 'have not checked yet.'  
            
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
        
    @pyqtSignature("bool")    
    def on_pushSoundSwitch_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        try:
            is_soundOn = self.is_soundOn
            if is_soundOn:
                self.sound_off()
            else:
                self.sound_on()
        except Exception, reason:
            print 'can not switch sound', reason
            
        
        
    @pyqtSignature("bool")
    def on_visualChange_clicked(self, checked):
        """
        Slot documentation goes here.
        """  
        nameChosen =self.an24Chosen['name']
        an24Dict_chosen = self.an24Dict[nameChosen]
        self.hide()
        DlgPregSim.switch2_simple(an24Dict_chosen)
        if DlgPregSim.is_simple_hidden():
            self.show()
        else:
            pass
    
    @pyqtSignature("bool")    
    def on_pinTest_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        nameChosen =self.an24Chosen['name']
        run_chk = self.an24Dict[nameChosen].rawAN24.run_chk
        if run_chk != [0, 0, 0, 0, 0]:
            self.an24Dict[nameChosen].rawAN24.run_chk = [0, 0, 0, 0, 0]
            print self.an24Dict[nameChosen].rawAN24.run_chk
        else:
            self.an24Dict[nameChosen].rawAN24.run_chk = [0, 0, 1, 0, 1]
            print self.an24Dict[nameChosen].rawAN24.run_chk
    
    @pyqtSignature("bool")     
    def on_recvStop_clicked(self, checked): 
        nameChosen =self.an24Chosen['name']
        self.an24Dict[nameChosen].rawAN24.stop_recv()
        self.sound_off()
        
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)          
    ist = Holter()
    DlgSearch = SeaAN24()
    DlgConnect = CntAN24()
    DlgCheck = ChkAN24()
    DlgCheck_Run = ChkAN24_Run()
    DlgPregSim = PregSim()
    ist.show()
    sys.exit(app.exec_())
