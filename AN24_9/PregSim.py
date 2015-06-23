# -*- coding: utf-8 -*-

"""
Module implementing PregSim.
"""
from PaintRealTime import *
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import (pyqtSignature, QTimer,  SIGNAL)
from Ui_PregSim import Ui_PregSim

class PregSim(QDialog, Ui_PregSim):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    def switch2_simple(self, an24Dict_chosen):
        self.an24 = an24Dict_chosen
        self.timerUpdate = QTimer()
        QtCore.QObject.connect(self.timerUpdate, SIGNAL("timeout()"),self.update_paint)
        self.timerUpdate.start(1000)
        self.exec_()
    
    def update_paint(self):
        self.update_event_bulb()
        self.show_Hr()
        self.show_runtime()
        self.update()
        
    
    @pyqtSignature("bool")
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.accept()
        self.timerUpdate.start(1000)
    def show_Hr(self):
        Cache = self.an24.rawAN24.cache
        if len(Cache)!=0:
            x = int(Cache[-1][0])
            y = int(Cache[-1][1])
        else:
            x = 0
            y = 0
        if 0==x:
            x='--'
        if 0==y:
            y='--'
        print x, y
        self.MoHrNum.setText(str(y))
        self.ChHrNum.setText(str(x))
    
    def show_runtime(self):
        """
        display the curren time 
        """
        runTime=int(self.an24.draw_current_time-self.an24.start_time)
        Hour=runTime/3600
        Minute=(runTime%3600)/60
        Second=(runTime%3600)%60
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
        self.RunTimeNum.setText(Hour+ ':'+Minute+ ':'+Second)
    
    def update_event_bulb(self):    
        """
        update event bulb 
        """
        Cache = self.an24.rawAN24.cache
        if len(Cache)>=4:
            for cache in Cache[-4:-1]:
                if cache[5]!=0:
                    print 'Bulb on'
                    Bulb=True
                    break
                else:
                    Bulb=False
            if Bulb:
                self.Bulb.setStyleSheet("background-image: url(:/picture/imgs/BulbOn.png);background-repeat: no-repeat")
            else:
                self.Bulb.setStyleSheet("background-image: url(:/picture/imgs/BulbOff.png);\n""background-repeat: no-repeat")
    
    def paintEvent(self, event):
        qp = QtGui.QPainter()       
        qp.begin(self)
        Cache = self.an24.rawAN24.cache
        end_count = len(Cache)
        PregSimMMov(self, qp, Cache, end_count)
        qp.end()
