# -*- coding: utf-8 -*-

"""
Module implementing Holter.
"""
import random
import sys,random
import time
from threading import Timer 
import winsound
import PyQt4
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QMainWindow, QDialog)
from PyQt4.QtCore import pyqtSignature
from Ui_Holter import Ui_Holter
from PyQt4.QtCore import (QObject,QRectF,QRect,QPointF,
                          QTimer,SIGNAL,Qt,pyqtProperty,
                          QPropertyAnimation,QEasingCurve)
#from OpenCsv import *
#from BasCal import *
from Ui_PregSim import *
from Ui_Holter import *
from Ui_SeaAN24 import *
from Ui_CntAN24 import *
from Ui_ChkAN24 import *
from PaintRealTime import *
from AN24 import scan_bt, AN24
class SeaAN24(QDialog, Ui_SeaAN24):
    """
    Class documentation goes here.
    """   
    
    """
    此处用真实搜索到的name：address字典来替换AN24Dict的内容，变量名不要换。
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.AN24Dict=scan_bt()
        self.NameList=[]
        self.Address=''
        self.Name=''
        self.timerScan = QTimer()
        self.n=0
        self.startTime = 0
        self.allTime = 0
        self.Cache = []
        QtCore.QObject.connect(self.timerScan, SIGNAL("timeout()"),self.addItems)
        for key in self.AN24Dict:
            self.NameList.append(key)
        self.timerScan.start(1000)
        self.DlgCntAN24 = CntAN24(self) 
        
    def addItems(self):
        print 'Scan', self.n
        self.listWidget.addItems([self.NameList[self.n]])
        if self.n==len(self.AN24Dict)-1:
            self.timerScan.stop()
            print 'stop'
        self.n+=1
            
    
    @pyqtSignature("QListWidgetItem*")
    def on_listWidget_itemClicked(self, item):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        foot=self.listWidget.currentRow()
        self.Name=self.NameList[foot]
        self.Address=self.AN24Dict[self.Name]
        print self.Name, self.Address
        self.pushButton.setEnabled(True)

    
    @pyqtSignature("bool")
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented ye
        self.AN24 =  AN24(self.Address)
        print 'init_chk:', self.AN24.init_chk
        self.allTime = self.AN24.battry
        self.DlgCntAN24.show()
        self.close()
        self.DlgCntAN24.timerConnecting.start(100)
        
        

class CntAN24(QDialog, Ui_CntAN24):
    """
    Class documentation goes here.
    """
    
    def __init__(self,  DlgSelect, parent = None ):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.count=0
        self.timerConnecting=QTimer()        
        QtCore.QObject.connect(self.timerConnecting, SIGNAL("timeout()"),self.connectAN24)
        self.DlgSeaAN24 = DlgSelect
        self.DlgChkAN24 = ChkAN24(self.DlgSeaAN24)
        
    def connectAN24(self):
        
        self.label.setText(self.DlgSeaAN24.Name+u"正在连接……") 
        self.repaint()
        self.count+=1
        print self.count, '----------CntAN24.count'
        
        """
        此处连接蓝牙的函数，参数为SeaAN24.Address,return connected,a bool.
        """
        print time.ctime()
        time.sleep(2)
        connected=random.randint(0, 1)
        
        if connected:
            print 'successful connection!'
            self.label.setText(self.DlgSeaAN24.Name+u"连接成功!")           
            self.repaint()
            self.timerConnecting.stop()
            time.sleep(1)
            self.close()
            
            self.DlgChkAN24.show()             
            print 'close'
        else:
            if self.count==2:
                self.label.setText(self.DlgSeaAN24.Name+u"连接失败，请重新选择")           
                self.repaint()
                self.timerConnecting.stop()
                self.count=0
                time.sleep(1)
                self.close()
                self.DlgSeaAN24.show()
                    
            
class ChkAN24(QDialog, Ui_ChkAN24):
    """
    Class documentation goes here.
    """
    def __init__(self,DlgSelect,  parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.labelList=[self.Check, self.Check_2, self.Check_3,self.Check_4, self.Check_5]
        self.DlgSeaAN24 = DlgSelect
        self.DlgPregSim = PregSim(self.DlgSeaAN24)
        self.DlgHolter = Holter(self.DlgSeaAN24)
        self.check_value  = [1, 1, 1, 1, 1]
    def paintEvent(self, event):
        for i in range(5):            
            if self.check_value[i]==0:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/OK.png);background-repeat:no-repeat;") 
            elif self.check_value[i]==1:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/questionMark.png);background-repeat:no-repeat;")
            else:
                self.labelList[i].setStyleSheet("background-image: url(:/picture/imgs/No.png);background-repeat:no-repeat;")
        
    
    @pyqtSignature("bool")
    def on_ButtonCheck_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        """
        此处checkList为返回的电极检查结果
        """         
        #print 'cache:', self.DlgSeaAN24.AN24.cache
        if len(self.DlgSeaAN24.AN24.cache) != 0:
            #self.DlgSeaAN24.AN24.run_chk = [0, 0, 0, 0, 0]
            #print '1111111111'
            #print 'befor:', self.DlgSeaAN24.AN24.run_chk
            #self.DlgSeaAN24.AN24.updata_init_chk()
            #print 'after:', self.DlgSeaAN24.AN24.run_chk
            self.check_value = self.DlgSeaAN24.AN24.run_chk
            self.update()
            if self.check_value == [0, 0, 0, 0, 0]:
                self.timerHold = QTimer()      
                QtCore.QObject.connect(self.timerHold, SIGNAL("timeout()"),self.closehold)
                self.timerHold.start(500)
        else:
            #print '222222222'
            self.check_value = self.DlgSeaAN24.AN24.init_chk
            #print 'before update:', self.check_value
            self.update()
            #print 'after update:', self.check_value
            if self.check_value == [0, 0, 0, 0, 0]:
                self.ButtonStart.setEnabled(True)
    def closehold(self):
        self.timerHold.stop()
        self.close()
            
        
    @pyqtSignature("bool")
    def on_ButtonStart_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet 
        if len(self.DlgSeaAN24.AN24.cache) == 0:
            self.DlgSeaAN24.startTime=time.time()
            self.close()            
            self.DlgSeaAN24.AN24.data_recv()
            self.DlgHolter.timerPaint.start(1000)
            self.DlgHolter.timerSound.start(500)     
            self.DlgPregSim.timer.start(1000)
            self.DlgPregSim.timerPaint.start(1000)
            self.DlgHolter.timerPin.start(1000)
            self.DlgHolter.show()
            self.close()
        else: 
            self.close()
class Holter(QMainWindow, Ui_Holter):
    """
    Class documentation goes here.
    """
    
    def __init__(self,DlgSelect, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.timerCount=QTimer()
        self.timerPaint = QTimer()
        self.timerSound=QTimer()
        self.timerPin = QTimer()      
        QtCore.QObject.connect(self.timerPaint, SIGNAL("timeout()"),self.update)
        QtCore.QObject.connect(self.timerSound, SIGNAL("timeout()"),self.sound)   
        QtCore.QObject.connect(self.timerPin, SIGNAL("timeout()"),self.checkPin)  
        self.DlgSeaAN24 = DlgSelect
    def paintEvent(self, event):
        qp = QtGui.QPainter()       
        qp.begin(self)
        drawBackground(self, qp)
        xyRatio=1
        
        if len(self.DlgSeaAN24.AN24.cache) == 0:
            drawScales(self, qp)       
        else:
            Cache = self.DlgSeaAN24.AN24.cache
            drawScales(self, qp, self.DlgSeaAN24.startTime,  len(self.DlgSeaAN24.AN24.cache), xyRatio)        
            realFHR(self, qp, Cache,  len(self.DlgSeaAN24.AN24.cache), xyRatio)
            realEHG(self, qp, Cache, len(self.DlgSeaAN24.AN24.cache), xyRatio)
            realMHR(self, qp, Cache,  len(self.DlgSeaAN24.AN24.cache), xyRatio)
            realMMov(self, qp, Cache,  len(self.DlgSeaAN24.AN24.cache), xyRatio)
            realSNR(self, qp, Cache,  len(self.DlgSeaAN24.AN24.cache), xyRatio)
            realEvent(self, qp, Cache,  len(self.DlgSeaAN24.AN24.cache), xyRatio)
            
            runTime=int(time.time()-self.DlgSeaAN24.startTime) 
            restTime = int(self.DlgSeaAN24.allTime*3600 - runTime)
            Hour=restTime/3600
            Minute=(restTime%3600)/60
            Second=(restTime%3600)%60
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
            self.restTime.setText(u'电量剩余时间： ' + Hour+ ':'+Minute+ ':'+Second)            
        self.visualChange.setGeometry(QtCore.QRect(self.size().width()*0.95-100, 50, 61, 51))
        self.restTime.setGeometry(QtCore.QRect(self.size().width()*0.95-301,10, 301, 31))
        qp.end()
    def checkPin(self):
        if self.DlgSeaAN24.AN24.run_chk !=[0, 0, 0, 0, 0]:
            self.DlgSeaAN24.DlgCntAN24.DlgChkAN24.check_value = self.DlgSeaAN24.AN24.run_chk
            self.DlgSeaAN24.DlgCntAN24.DlgChkAN24.show()
            self.DlgSeaAN24.DlgCntAN24.DlgChkAN24.update()
            self.DlgSeaAN24.DlgCntAN24.DlgChkAN24.ButtonStart.setVisible(False)
        
    @pyqtSignature("bool")
    def on_visualChange_clicked(self, checked):
        """
        Slot documentation goes here.
        """        
        self.DlgSeaAN24.DlgCntAN24.DlgChkAN24.DlgPregSim.show()
        self.hide()
        
    @pyqtSignature("bool")    
    def on_startButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.DlgSeaAN24.AN24.run_chk = [1, 1, 0, 1, 0]
        
    
    def sound(self):
        Cache =self.DlgSeaAN24.AN24.cache
        if len(Cache)!=0:
            heartRate=Cache[-1][0]
            if heartRate!=0:
                heartCycle=60000/heartRate
                self.timerSound.start(heartCycle)
                winsound.PlaySound(soundfile, winsound.SND_ASYNC) #立即返回，支持异步播放
            print heartRate, Cache[-1][1],  len(Cache)
        
        
class PregSim(QDialog, Ui_PregSim):
    """
    Class documentation goes here.
    """
    def __init__(self, DlgSelect,  parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.timer = QTimer()
        self.timerPaint = QTimer()
        QtCore.QObject.connect(self.timer, SIGNAL("timeout()"),self.ShowHr)
        QtCore.QObject.connect(self.timerPaint, SIGNAL("timeout()"),self.update)
        self.DlgSeaAN24 = DlgSelect
    def paintEvent(self, event):
        qp = QtGui.QPainter()       
        qp.begin(self)
        Cache = self.DlgSeaAN24.AN24.cache
        PregSimMMov(self, qp, Cache, len(self.DlgSeaAN24.AN24.cache))
        
    
    @pyqtSignature("bool")
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.DlgSeaAN24.DlgCntAN24.DlgChkAN24.DlgHolter.isVisible():
            self.DlgSeaAN24.DlgCntAN24.DlgChkAN24.DlgHolter.setVisible(False)
        else:
            self.DlgSeaAN24.DlgCntAN24.DlgChkAN24.DlgHolter.setVisible(True)
        self.setVisible(False)            
        
    
    def ShowHr(self):
        """
        display the heatrate of mother and children 
        """
        Cache = self.DlgSeaAN24.AN24.cache
        if len(Cache)!=0:
            x = int(Cache[-1][0])
            y = int(Cache[-1][1])
            if 0==x:
                x='--'
            if 0==y:
                y='--'
            self.MoHrNum.setText(str(y))
            self.ChHrNum.setText(str(x))
        """
        display the curren time 
        """
        runTime=int(time.time()-self.DlgSeaAN24.startTime)
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
        
        """
        update event bulb 
        """
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
   
        
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    soundfile = "./sound/heartbeat.wav"           
    AN241=SeaAN24()
    AN241.show()
    #AN241.DlgCntAN24.DlgChkAN24.DlgHolter.show() 
    sys.exit(app.exec_())
    
"""
此处为计算基线
"""
#    global Baseline
#    FHR=[]
#    for item in Cache:
#        FHR.append(item[0])
#    Baseline=CalBaseline(FHR)
    
