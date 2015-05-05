# -*- coding: utf-8 -*-
import PyQt4
from PyQt4 import QtGui, QtCore
from Holter import *
import time

def realFHR(self, qp, Cache, startCount, endCount):
    pen = QtGui.QPen(QtGui.QColor(35, 78, 220), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystepHR=float(HolterHeight)/36
    xstep=2*ystepHR
    ypointHR=ystepHR/10
    xpoint=xstep/240
    cachePre=[]
    if endCount>int(HolterWidth*0.83/xstep)*240:
        startCount=endCount-int(HolterWidth*(0.83)/xstep)*240
    for cache in Cache[startCount:endCount]:
        if i!=0 and cache[0]!=0 and cachePre[0]!=0:
            qp.drawLine(xpoint*(i-1), 16*ystepHR-ypointHR*(cachePre[0]-50), xpoint*i, 16*ystepHR-ypointHR*(cache[0]-50))
        cachePre=cache
        i+=1
        
def realEHG(self, qp, Cache, startCount, endCount):
    pen = QtGui.QPen(QtGui.QColor(0, 0, 0), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystepHR=float(HolterHeight)/36
    xstep=2*ystepHR
    ystepEHG=1.5*ystepHR
    ypointEHG=ystepEHG/25
    xpoint=xstep/240
    cachePre=[]
    if endCount>int(HolterWidth*0.83/xstep)*240:
        startCount=endCount-int(HolterWidth*(0.83)/xstep)*240
    for cache in Cache[startCount:endCount]:
        if i!=0 and cache[2]!=0 and cachePre[2]!=0:
            qp.drawLine(xpoint*(i-1), 22*ystepHR-ypointEHG*(float(cachePre[2])/255*100), xpoint*i, 22*ystepHR-ypointEHG*(float(cache[2])/255*100))
        cachePre=cache
        i+=1

def realMHR(self, qp, Cache, startCount, endCount):
    pen = QtGui.QPen(QtGui.QColor(183, 48, 34), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystepHR=float(HolterHeight)/36
    xstep=2*ystepHR
    ypointHR=ystepHR/10
    xpoint=xstep/240
    cachePre=[]
    if endCount>int(HolterWidth*0.83/xstep)*240:
        startCount=endCount-int(HolterWidth*(0.83)/xstep)*240
    for cache in Cache[startCount:endCount]:
        if i!=0 and cache[1]!=0 and cachePre[1]!=0:
            qp.drawLine(xpoint*(i-1), 32*ystepHR-ypointHR*(cachePre[1]-40), xpoint*i, 32*ystepHR-ypointHR*(cache[1]-40))
        cachePre=cache
        i+=1

def realBaseline(self, qp, Baseline, count):
    pen = QtGui.QPen(QtGui.QColor(18, 129, 232), 2, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    baseCount=count/240-10
    size=self.size()
    xstep=float(size.width())/58
    ystep=float(size.height())/150
    if baseCount>0:
        for baseline in Baseline[0:baseCount]:
            if i!=0:
                qp.drawLine(xstep*(i-1+5), size.height()-ystep*(Baseline[i-1]-50), xstep*(i+5), size.height()-ystep*(Baseline[i]-50))
            i+=1
    
def drawBackground(self, qp):
    '''
    FHR background below
    '''
    color = QtGui.QColor()
    color.setNamedColor('#d4d4d4')
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystepHR=float(HolterHeight)/36
    xstep=2*ystepHR
    qp.setPen(color)       
    qp.setBrush(QtGui.QColor(247, 220, 230, 200))
    qp.drawRect(0,13*ystepHR, HolterWidth, 3*ystepHR)
    qp.setBrush(QtGui.QColor(255, 251, 190, 160))
    qp.drawRect(0,10*ystepHR, HolterWidth, 3*ystepHR)
    qp.setBrush(QtGui.QColor(255, 255, 255, 200))
    qp.setPen(QtGui.QColor(255, 255, 255, 200))    
    qp.drawRect(0, 6*ystepHR, HolterWidth, 4*ystepHR)
    qp.setBrush(QtGui.QColor(255, 251, 190, 160))
    qp.setPen(color)    
    qp.drawRect(0, 3*ystepHR, HolterWidth, 3*ystepHR)
    qp.setBrush(QtGui.QColor(247, 220, 230, 200))
    qp.drawRect(0,0, HolterWidth, 3*ystepHR) 
    '''
    EHG background below
    ''' 
    qp.setBrush(QtGui.QColor(255, 255, 255, 200))
    qp.drawRect(0,16*ystepHR, HolterWidth, 6*ystepHR)
    '''
    MHR background below
    ''' 
    qp.setBrush(QtGui.QColor(191, 229, 253, 150))
    qp.drawRect(0,22*ystepHR, HolterWidth, 10*ystepHR)
    '''
    MMov and SNR background below
    '''
    qp.setBrush(QtGui.QColor(255, 255, 255, 200))
    qp.drawRect(0,32*ystepHR, HolterWidth, 4*ystepHR)
def drawScales(self, qp, startTime):
    pen = QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.DotLine)
    qp.setPen(pen)
    qp.setFont(QtGui.QFont('Decorative', 10))
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystepHR=float(HolterHeight)/36
    ystepEHG=1.5*ystepHR
    xstep=2*ystepHR    
    restTime=600-startTime%600
    restSecond=restTime%60
    halfstep=restSecond*xstep/60
    half10Min=restTime*xstep/60
    xstepMax=int((HolterWidth-halfstep)/xstep)+1
    x10Max=int((HolterWidth-half10Min)/xstep/10)+1
    firstScale = startTime+restTime
    print restTime, time.localtime(startTime+restTime)
    
        
    
    '''
    FHR scale below
    '''
    for i in range(17):
        qp.drawLine(0, i*ystepHR,size.width(),i*ystepHR)
        qp.drawText(5,i*ystepHR+5, "%s" %((16-i)*10+50))
        
    '''
    EHG scale and text below
    '''    
    for i in range(5):
        qp.drawLine(0, 16*ystepHR+i*ystepEHG,HolterWidth,16*ystepHR+i*ystepEHG)
        qp.drawText(HolterWidth-30,16*ystepHR+i*ystepEHG+5, "%s" %((4-i)*25))

    '''
    MHR scale and text below
    '''    
    for i in range(11):
        qp.drawLine(0, (i+22)*ystepHR,size.width(),(i+22)*ystepHR)
        qp.drawText(5,(i+22)*ystepHR+5, "%s" %((10-i)*10+40))
    '''
    xstep scale below
    '''    
    for i in range(xstepMax):
        qp.drawLine(xstep*i+halfstep, 0, xstep*i+halfstep, HolterHeight)
        
    '''
    Time scale below
    '''
    pen = QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    qp.setFont(QtGui.QFont('Decorative', 10))
    for i in range(x10Max):
        qp.drawLine(10*xstep*i+half10Min, 0, 10*xstep*i+half10Min, HolterHeight)
        timeScale = time.strftime('%H:%M:%S', time.localtime(firstScale+i*600))
        qp.drawText(10*xstep*i+half10Min,HolterHeight-50,timeScale )
def drawLines(self, qp):
    pen = QtGui.QPen(QtGui.QColor(18, 129, 232), 2, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    xstep=float(size.width())/58
    ystep=float(size.height())/150
    for baseline in Baseline[0:54]:
        if i!=0:
            qp.drawLine(xstep*(i-1+5), size.height()-ystep*(Baseline[i-1]-50), xstep*(i+5), size.height()-ystep*(Baseline[i]-50))
        i+=1
def drawPoints(self, qp):
    qp.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 5, QtCore.Qt.SolidLine))
    size = self.size()
    for i in range(1000):
        x = random.randint(1, size.width()-1)
        y = random.randint(1, size.height()-1)
        qp.drawPoint(x, y)
def drawFHR(self, qp):
    pen = QtGui.QPen(QtGui.QColor(0, 0, 0), 0.5, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    xstep=float(size.width())/(60*240)
    ystep=float(size.height())/150
    for baseline in FHR[0:60*240]:
        if i!=0 and FHR[i-1]!=0 and FHR[i]!=0:
            qp.drawLine(xstep*(i-1), size.height()-ystep*(FHR[i-1]-50), xstep*i, size.height()-ystep*(FHR[i]-50))
        i+=1
