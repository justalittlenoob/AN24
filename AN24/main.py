# -*- coding: utf-8 -*-

"""
Module implementing Holter.
"""

import sys,random
import time
import winsound
import PyQt4
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_Holter import Ui_Holter
from PyQt4.QtCore import (QObject,QRectF,QRect,QPointF,
                          QTimer,SIGNAL,Qt,pyqtProperty,
                          QPropertyAnimation,QEasingCurve )
from OpenCsv import *
from BasCal import *
from PregSim import *
from Holter import *
from PaintRealTime import *
                         

class Holter(QMainWindow, Ui_Holter):
    """
    Class documentation goes here.
    """
    startCount=0 #用于计数realFHR的绘画次数，即timer的计数次数
    endCount=0
    def __init__(self,parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.timer = QTimer()
        self.timerSound=QTimer()
        global soundfile 
        soundfile = "F:/work in 2015 winter/5-HOLTER/FHR/_eric4project/rawHR.wav" 
        self.timer.start(1000)
        QtCore.QObject.connect(self.timer, SIGNAL("timeout()"),self.update)

    def paintEvent(self, event): 
        qp = QtGui.QPainter()       
        qp.begin(self)
        drawBackground(self, qp)
        drawScales(self, qp)        
        realFHR(self, qp, Cache, Holter.startCount, Holter.endCount)
        #realBaseline(self, qp, Baseline, Holter.endCount) 
        if Holter.endCount<len(Cache):
            Holter.endCount+=4
            if Holter.endCount%1000==0:
                print time.strftime('%H:%M:%S',time.localtime(time.time()))        
                print Holter.endCount
        
    def sound(self):
        winsound.PlaySound(soundfile, winsound.SND_ASYNC) #立即返回，支持异步播放
    @pyqtSignature("bool")
    def on_visualChange_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        
        DlgPregSim.show()
        DlgHolter.hide()
        
        
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
        self.timer = QTimer()
        self.timer.start(250)
        QtCore.QObject.connect(self.timer, SIGNAL("timeout()"),self.ShowHr)
    
    
    @pyqtSignature("bool")
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if DlgHolter.isVisible():
            DlgHolter.setVisible(False)
        else:
            DlgHolter.setVisible(True)
        DlgPregSim.setVisible(False)            
        self.Bulb.setStyleSheet("background-image: url(:/imgs/BulbOn.png);\n"
"background-repeat: no-repeat")
    
    def ShowHr(self):
        """
        display the heatrate of mother and children 
        """
        x = random.randint(60, 120)
        y = random.randint(120, 180)
        self.MoHrNum.setText(str(x))
        self.ChHrNum.setText(str(y))
        
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    #path="E:/5-HOLTER/new/long.csv"
    global Cache
    global Baseline
    Cache = OpenCsv()
    '''
    FHR=[]
    for item in Cache:
        FHR.append(item[0])
    Baseline=CalBaseline(FHR)
    '''
    DlgHolter=Holter()
    DlgPregSim=PregSim()
    DlgHolter.show()
    #dlg.close()
    sys.exit(app.exec_())
