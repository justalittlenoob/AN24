# -*- coding: utf-8 -*-
import PyQt4
from PyQt4 import QtGui, QtCore
#from Holter import *
import time

def realFHR(self, qp, Cache, endCount, xRatio):
    pen = QtGui.QPen(QtGui.QColor(35, 78, 220), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystepHR=float(HolterHeight)/36
    xstep=2*ystepHR
    ypointHR=ystepHR/10
    cachePre=[]
    xpoint=xstep/(240/xRatio)
    if endCount>HolterWidth*0.83/xstep*240/xRatio:
        startCount=endCount-int(HolterWidth*(0.83)/xstep*240/xRatio)
    else:
        startCount = 0
    for cache in Cache[startCount:endCount]:
        if i!=0 and cache[0]!=0 and cachePre[0]!=0:
            qp.drawLine(xpoint*(i-1), 16*ystepHR-ypointHR*(cachePre[0]-50), xpoint*i, 16*ystepHR-ypointHR*(cache[0]-50))
        cachePre=cache
        i+=1
        
def realEHG(self, qp, Cache, endCount, xRatio):
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
    cachePre=[]
    xpoint=xstep/(240/xRatio)
    if endCount>HolterWidth*0.83/xstep*240/xRatio:
        startCount=endCount-int(HolterWidth*(0.83)/xstep*240/xRatio)
    else:
        startCount = 0
    for cache in Cache[startCount:endCount]:
        if i!=0 and cache[2]!=0 and cachePre[2]!=0:
            qp.drawLine(xpoint*(i-1), 22*ystepHR-ypointEHG*(float(cachePre[2])/255*100), xpoint*i, 22*ystepHR-ypointEHG*(float(cache[2])/255*100))
        cachePre=cache
        i+=1

def realMHR(self, qp, Cache, endCount, xRatio):
    pen = QtGui.QPen(QtGui.QColor(183, 48, 34), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystepHR=float(HolterHeight)/36
    xstep=2*ystepHR
    ypointHR=ystepHR/10
    cachePre=[]
    xpoint=xstep/(240/xRatio)
    if endCount>HolterWidth*0.83/xstep*240/xRatio:
        startCount=endCount-int(HolterWidth*(0.83)/xstep*240/xRatio)
    else:
        startCount = 0
    for cache in Cache[startCount:endCount]:
        if i!=0 and cache[1]!=0 and cachePre[1]!=0:
            qp.drawLine(xpoint*(i-1), 32*ystepHR-ypointHR*(cachePre[1]-40), xpoint*i, 32*ystepHR-ypointHR*(cache[1]-40))
        cachePre=cache
        i+=1

def realMMov(self, qp, Cache, endCount, xRatio):
    pen = QtGui.QPen(QtGui.QColor(116, 186, 106), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    qp.setBrush(QtGui.QColor(116, 186, 106, 100))
    i=0
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystep=float(HolterHeight)/36
    xstep=2*ystep
    ypoint=(ystep-1)*2.5/3
    xpoint=xstep/(240/xRatio)
    if endCount>HolterWidth*0.83/xstep*240/xRatio:
        startCount=endCount-int(HolterWidth*(0.83)/xstep*240/xRatio)
    else:
        startCount = 0
    for cache in Cache[startCount:endCount]:
        if cache[3]!=0:
            qp.drawRect(xpoint*i,34.5*ystep-2, xpoint, -cache[3]*ypoint)
        else:
            qp.drawRect(xpoint*i,34.5*ystep-2, xpoint, -1)
        i+=1
        
def realSNR(self, qp, Cache, endCount, xRatio):
    pen = QtGui.QPen(QtGui.QColor(144, 159, 248), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    qp.setBrush(QtGui.QColor(144, 159, 248, 100))
    i=0
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystep=float(HolterHeight)/36
    xstep=2*ystep
    ypoint=(ystep-1)*1.5/2
    xpoint=xstep/(240/xRatio)
    if endCount>HolterWidth*0.83/xstep*240/xRatio:
        startCount=endCount-int(HolterWidth*(0.83)/xstep*240/xRatio)
    else:
        startCount = 0
    for cache in Cache[startCount:endCount]:
        if cache[4]!=0:
            qp.drawRect(xpoint*i,36*ystep-2, xpoint, -cache[4]*ypoint)
        else:
            qp.drawRect(xpoint*i,36*ystep-2, xpoint, -1)
        i+=1

def realEvent(self, qp, Cache, endCount, xRatio):
    pen = QtGui.QPen(QtGui.QColor(204, 138, 138), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    qp.setBrush(QtGui.QColor(204, 138, 138, 100))
    i=0
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystep=float(HolterHeight)/36
    xstep=2*ystep
    xpoint=xstep/(240/xRatio)
    if endCount>HolterWidth*0.83/xstep*240/xRatio:
        startCount=endCount-int(HolterWidth*(0.83)/xstep*240/xRatio)
    else:
        startCount = 0
    for cache in Cache[startCount:endCount]:
        if cache[5]!=0:
            #qp.drawRect(xpoint*i,0, xpoint, ystep*32)
            qp.drawLine(xpoint*i, 0, xpoint *i,ystep*32)
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
    MMov background below
    '''
    qp.setBrush(QtGui.QColor(220, 248, 146, 100))
    qp.drawRect(0,32*ystepHR, HolterWidth, 2.5*ystepHR)
    
    '''
    MMov and SNR background below
    '''
    qp.setBrush(QtGui.QColor(251, 249, 116, 100))
    qp.drawRect(0,34.5*ystepHR, HolterWidth, 1.5*ystepHR)
    
def drawScales(self, qp, startTime=time.time(), drawTime = time.time(), endCount=0, xRatio=1):
    pen = QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.DotLine)
    qp.setPen(pen)
    qp.setFont(QtGui.QFont('Decorative', 10))
    size=self.size()
    HolterWidth=size.width()
    HolterHeight=size.height()
    ystepHR=float(HolterHeight)/36
    ystepEHG=1.5*ystepHR
    xstep=2*ystepHR    
    
    if endCount>HolterWidth*0.83/xstep*240/xRatio:
        startCount=endCount-HolterWidth*(0.83)/xstep*240/xRatio
        deltaCount = endCount - startCount
        deltaTime = float(deltaCount)/4
        startTime = drawTime - deltaTime
    else:
        startCount = 0
    if xRatio == 1:
        bigScalS = 10*60
        smallScalS = 60
        bigScal = xstep * 10
    elif xRatio == 2:
        bigScalS = 5*60
        smallScalS = 30
        bigScal = xstep * 10
    else:
        bigScalS = 3*60
        smallScalS = 20
        bigScal = xstep * 9
    #rest of second before first 10Min scale
    restTime=bigScalS-startTime%bigScalS
    #rest of second before first 1Min scale   
    restSecond=restTime%smallScalS
    #pix of first column
    halfstep=restSecond*xstep/smallScalS
    #pix of first big scale
    halfBig=restTime*xstep/smallScalS
    #max complete column in whole Holter
    xstepMax=int((HolterWidth-halfstep)/xstep)+1
    #max complete big column in whole Holter
    xBigMax=int((HolterWidth-halfBig)/bigScal)+1
    #time stamp of first 10Min scale
    firstScale = startTime+restTime    
    #print 'restTime:', restTime, 'restSecond:', restSecond, 'halfstep:', halfstep, 'halfBig:', halfBig   
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
    for i in range(xBigMax):
        qp.drawLine(bigScal*i+halfBig, 0, bigScal*i+halfBig, HolterHeight)
        timeScale = time.strftime('%H:%M:%S', time.localtime(firstScale+i*bigScalS))
        qp.drawText(bigScal*i+halfBig,ystepHR*32-10,timeScale )
    
    
def PregSimMMov(self, qp, Cache, endCount):
    pen = QtGui.QPen(QtGui.QColor(183, 48, 34), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    PregSimWidth=size.width()
    PregSimHeight=size.height()
    ystep=40
    xstep=float(PregSimWidth)/15.5
    qp.setBrush(QtGui.QColor(248, 134, 42, 100))
    if endCount>4*10:
        startCount=endCount-4*10
    else:
        startCount = 0
    for cache in Cache[startCount:endCount]:
        if i%4==0:
            if cache[3]!=0:
                qp.drawRect(xstep*(i/4*1.5+0.5),450, xstep, -cache[3]*ystep)
            else:
                qp.drawRect(xstep*(i/4*1.5+0.5),450, xstep, -5)
        i+=1


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
