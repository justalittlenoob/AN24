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
    #baseCount=0
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
        realFHR(self, qp, FHR, Holter.count)
        realBaseline(self, qp, Baseline, Holter.count)       
        Holter.count+=1
        if Holter.count%1000==0:
            print time.strftime('%H:%M:%S',time.localtime(time.time()))        
            print Holter.count
        
    def sound(self):
        winsound.PlaySound(soundfile, winsound.SND_ASYNC) #立即返回，支持异步播放

if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    path="D:/WorkSpace/Github/docs/csv.csv"
    Time, FHR, MHR, EHG= OpenCsv(path)
    Baseline=CalBaseline(FHR)
    print len(Baseline)
    DlgHolter=Holter()
    DlgPregSim=PregSim()
    DlgHolter.show()
    DlgPregSim.show()   
    #dlg.close()
    sys.exit(app.exec_())
