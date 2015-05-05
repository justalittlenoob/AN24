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
from PaintRealTime import *
                         

class Holter(QMainWindow, Ui_Holter):
    """
    Class documentation goes here.
    """
    count=0 #用于计数realFHR的绘画次数，即timer的计数次数
    FHRR=[]
    Baseline=[]
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
        self.timer.start(1)
        QtCore.QObject.connect(self.timer, SIGNAL("timeout()"),self.update)

    def paintEvent(self, event): 
        qp = QtGui.QPainter()       
        qp.begin(self)
        drawBackground(self, qp)
        drawScales(self, qp)        
        realFHR(self, qp, Holter.FHRR, Holter.count)
        realBaseline(self, qp, Holter.Baseline, Holter.count)       
        Holter.count+=1
        if Holter.count%1000==0:
            print time.strftime('%H:%M:%S',time.localtime(time.time()))        
        
    def sound(self):
        winsound.PlaySound(soundfile, winsound.SND_ASYNC) #立即返回，支持异步播放
    @pyqtSignature("bool")
    def on_visualChange_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        
        DlgPregSim.show()
        DlgHolter.hide()
        
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    path="E:/5-HOLTER/new/long.csv"
    cache= OpenCsv(path)
    FHR=[]
    for item in cache:
        FHR.append(item[0])
    print FHR[1000:1100]
    Holter.FHRR=FHR
    Holter.Baseline=CalBaseline(FHR)
    print len(Holter.Baseline)
    DlgHolter=Holter()
    DlgPregSim=PregSim()
    DlgHolter.show()
    #dlg.close()
    sys.exit(app.exec_())
