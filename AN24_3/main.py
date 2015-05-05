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
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_Holter import Ui_Holter
from PyQt4.QtCore import (QObject,QRectF,QRect,QPointF,
                          QTimer,SIGNAL,Qt,pyqtProperty,
                          QPropertyAnimation,QEasingCurve )
from OpenCsv import *
from BasCal import *
from Ui_PregSim import *
from Ui_Holter import *
from Ui_SeaAN24 import *
from Ui_CntAN24 import *
from Ui_ChkAN24 import *
from PaintRealTime import *
import init_An24    
import data
class SeaAN24(QDialog, Ui_SeaAN24):
    """
    Class documentation goes here.
    """
    n=0
    """
    此处用真实搜索到的name：address字典来替换AN24Dict的内容，变量名不要换。
    """
    #print '111111111111'
    AN24Dict=init_An24.scan_bluetooth()                                                                     #!!!!!!!!!!!!!!
    #print '22222'
    NameList=[]
    Address=''
    Name=''
    for key in AN24Dict:
        NameList.append(key)
        
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.timerScan = QTimer()
        QtCore.QObject.connect(self.timerScan, SIGNAL("timeout()"),self.addItems)
        self.timerScan.start(1000)        

        
    def addItems(self):
        print 'Scan', SeaAN24.n
        self.listWidget.addItems([SeaAN24.NameList[SeaAN24.n]])
        if SeaAN24.n==len(SeaAN24.AN24Dict)-1:
            self.timerScan.stop()
            print 'stop'
        SeaAN24.n+=1
            
    
    @pyqtSignature("QListWidgetItem*")
    def on_listWidget_itemClicked(self, item):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        foot=self.listWidget.currentRow()
        SeaAN24.Name=SeaAN24.NameList[foot]
        SeaAN24.Address=SeaAN24.AN24Dict[SeaAN24.Name]
        print SeaAN24.Name, SeaAN24.Address
        self.pushButton.setEnabled(True)

    
    @pyqtSignature("bool")
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #print '333'
        DlgCntAN24.show()
        CntAN24.timerConnecting.start(100)
        
        

class CntAN24(QDialog, Ui_CntAN24):
    """
    Class documentation goes here.
    """
    count=0
    timerConnecting=QTimer()
    #init_An24.conn(SeaAN24.Address)                                                       #!!!!!!!!!!!
    def __init__(self, parent = None):
        """
        Constructor
        """
        
        QDialog.__init__(self, parent)
        self.setupUi(self)        
        QtCore.QObject.connect(self.timerConnecting, SIGNAL("timeout()"),self.connectAN24)
    def connectAN24(self):
        
        self.label.setText(SeaAN24.Name+u"正在连接……") 
        self.repaint()
        CntAN24.count+=1
        
        """
        此处连接蓝牙的函数，参数为SeaAN24.Address,return connected,a bool.
        """
        print time.ctime()
        time.sleep(random.randint(2, 4))
#        connected=random.randint(0, 1)
        init_An24.conn(SeaAN24.Address)                                                              #!!!!!!!!!!!!! 
        print time.ctime()
        
        if init_An24.conn_value == 1:                                                                #!!!!!!!!!!!!!!
            self.label.setText(SeaAN24.Name+u"连接失败，请重新选择")           
            self.repaint()
            CntAN24.count=0
            time.sleep(1)
            self.close()
            self.timerConnecting.stop()
        else:
            print 'successful connection!'
            time.sleep(1)
            self.label.setText(SeaAN24.Name+u"连接成功!")           
            self.repaint()
            time.sleep(1)
            self.close()
            DlgSeaAN24.hide()
            DlgChkAN24.show()
            self.timerConnecting.stop()                                                             #!!!!!!!!!!!
            print 'close'                                                                           #!!!!!!!!!!!!!!
                
            
class ChkAN24(QDialog, Ui_ChkAN24):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("bool")
    def on_ButtonCheck_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        """
        此处checkList为返回的电极检查结果
        """
        #checkList=[2, 1, 1, 1, 1]
        checkList = init_An24.checking(init_An24.sock)                                            #!!!!!!!!!!!!!!
        print checkList
        labelList=[self.Check, self.Check_2, self.Check_3,self.Check_4, self.Check_5]
        for i in range(5):            
            if checkList[i]==0:
                labelList[i].setStyleSheet("background-image: url(:/picture/imgs/OK.png);background-repeat:no-repeat;") 
            elif checkList[i]==2:
                labelList[i].setStyleSheet("background-image: url(:/picture/imgs/questionMark.png);background-repeat:no-repeat;")
            else:
                labelList[i].setStyleSheet("background-image: url(:/picture/imgs/No.png);background-repeat:no-repeat;")
                                                                                                                   #!!!!!!!!!!!!!!
    @pyqtSignature("bool")
    def on_ButtonStart_clicked(self, checked):
        global Cache
        global startTime
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet 
        
        self.hide()    
        DlgHolter.show()
        DlgHolter.timerCount.start(1000)
        DlgHolter.timerSound.start(500)     
        
        #Cache = OpenCsv()
        data.start_data_thread(init_An24.sock)                                                                           #!!!!!!!!!!!!!!
        startTime = int(time.time())
        Cache = data.data_cache
        DlgHolter.timerPaint.start(1000)                                                                                   #!!!!!!!!!!!!!!
        DlgPregSim.timer.start(250)
class Holter(QMainWindow, Ui_Holter):
    """
    Class documentation goes here.
    """
    timerCount=QTimer()
    timerPaint = QTimer()
    timerSound=QTimer()
    def __init__(self,parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)      
        QtCore.QObject.connect(self.timerPaint, SIGNAL("timeout()"),self.update)
        QtCore.QObject.connect(self.timerSound, SIGNAL("timeout()"),self.sound)
        QtCore.QObject.connect(self.timerCount, SIGNAL("timeout()"),self.endCountAdd)

    def paintEvent(self, event):
 
        qp = QtGui.QPainter()       
        qp.begin(self)
        drawBackground(self, qp)
        drawScales(self, qp,startTime)        
        realFHR(self, qp, Cache, startCount, endCount)
        realEHG(self, qp, Cache, startCount, endCount)
        realMHR(self, qp, Cache, startCount, endCount)
#        realBaseline(self, qp, Baseline, endCount) 
#        qp.end(self)
    def endCountAdd(self):
        global endCount
        if endCount<len(Cache)-4:
            endCount+=4
            if endCount%100==0:
                print endCount
        
    @pyqtSignature("bool")
    def on_visualChange_clicked(self, checked):
        """
        Slot documentation goes here.
        """        
        DlgPregSim.show()
        DlgHolter.hide()
    
    def sound(self):
        if endCount!=0:
            heartRate=Cache[endCount][0]
            if heartRate!=0:
                heartCycle=60000/heartRate
                self.timerSound.start(heartCycle)
                winsound.PlaySound(soundfile, winsound.SND_ASYNC) #立即返回，支持异步播放
            print heartRate, Cache[endCount][1],  endCount
        
        
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
        #self.timer.start(1000)
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
        self.Bulb.setStyleSheet("background-image: url(:/picture/imgs/BulbOn.png);\n"
"background-repeat: no-repeat")
    
    def ShowHr(self):
        """
        display the heatrate of mother and children 
        """
        x = int(Cache[endCount][0])
        y = int(Cache[endCount][1])
        if 0==x:
            x='--'
        if 0==y:
            y='--'
        self.MoHrNum.setText(str(y))
        self.ChHrNum.setText(str(x))


def endCountAdd():
    global endCount
    if endCount<len(Cache):
        endCount+=4
        if endCount%1000==0:
            '''print time.strftime('%H:%M:%S',time.localtime(time.time()))        
            print endCount, len(Cache)'''
    countStart()
def countStart():
    timerCount=Timer(1,endCountAdd)  
    timerCount.start()

def playSound():
    heartRate=Cache[endCount][0]
    if heartRate!=0:        
        winsound.PlaySound(soundfile, winsound.SND_ASYNC) #立即返回，支持异步播放
    print heartRate, Cache[endCount][1]
    global soundflg
    soundStart()
    
def soundStart():
    heartRate=Cache[endCount][0]
    if heartRate==0:
        heartCycle=0.5
    else:
        heartCycle=float(60/heartRate) 
    global timerSound
    timerSound=Timer(heartCycle, playSound)
    timerSound.start()
    
        
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    path="./long.csv"
    global Cache
    #Cache = data.data_cache
    global startCount
    global endCount
    global soungfile
    global startTime
    startCount=0
    endCount=0 
    
    soundfile = "./sound/heartbeat.wav"
    DlgSeaAN24=SeaAN24()
    DlgCntAN24=CntAN24()
    DlgChkAN24=ChkAN24()
    DlgHolter=Holter()
    DlgPregSim=PregSim()
    DlgSeaAN24.show()
    sys.exit(app.exec_())
"""
此处为计算基线
"""
#    global Baseline
#    FHR=[]
#    for item in Cache:
#        FHR.append(item[0])
#    Baseline=CalBaseline(FHR)
    
