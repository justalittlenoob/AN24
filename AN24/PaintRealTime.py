# -*- coding: utf-8 -*-
import PyQt4
from PyQt4 import QtGui, QtCore
from Holter import *


def realFHR(self, qp, Cache, startCount, endCount):
    pen = QtGui.QPen(QtGui.QColor(0, 0, 0), 0.5, QtCore.Qt.SolidLine)
    qp.setPen(pen)
    i=0
    size=self.size()
    xstep=float(size.width())/(60*240)
    ystep=float(size.height())/150
    cachePre=[]
    if endCount>3000*4:
        startCount=endCount-3000*4
    for cache in Cache[startCount:endCount]:
        if i!=0 and cache[0]!=0 and cachePre[0]!=0:
            qp.drawLine(xstep*(i-1), size.height()-ystep*(cachePre[0]-50), xstep*i, size.height()-ystep*(cache[0]-50))
        cachePre=cache
        i+=1
    
#    for cache in Cache[startCount:endCount]:
#        if i!=0 and Cache[i-1][0]!=0 and Cache[i][0]!=0:
#            qp.drawLine(xstep*(i-1), size.height()-ystep*(Cache[i-1][0]-50), xstep*i, size.height()-ystep*(Cache[i][0]-50))
#        i+=1

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
    color = QtGui.QColor()
    color.setNamedColor('#d4d4d4')
    size=self.size()
    xstep=float(size.width())/59
    ystep=float(size.height())/150
    qp.setPen(color)       
    qp.setBrush(QtGui.QColor(247, 220, 230, 200))
    qp.drawRect(0,size.height()-30*ystep, size.width(), 30*ystep)
    qp.setBrush(QtGui.QColor(255, 251, 190, 160))
    qp.drawRect(0, size.height()-60*ystep, size.width(), 30*ystep)
    qp.setBrush(QtGui.QColor(255, 255, 255, 200))
    qp.setPen(QtGui.QColor(255, 255, 255, 200))    
    qp.drawRect(0, size.height()-100*ystep, size.width(), 40*ystep)
    qp.setBrush(QtGui.QColor(255, 251, 190, 160))
    qp.setPen(color)    
    qp.drawRect(0, size.height()-130*ystep, size.width(), 30*ystep)
    qp.setBrush(QtGui.QColor(247, 220, 230, 200))
    qp.drawRect(0,0, size.width(), 20*ystep)  
def drawScales(self, qp):
    pen = QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.DotLine)
    qp.setPen(pen)
    qp.setFont(QtGui.QFont('Decorative', 10))
    size=self.size()
    xstep=float(size.width())/58
    ystep=float(size.height())/150
    for i in range(59):
        if i!=0:
            qp.drawLine(xstep*i, 0, xstep*i, size.height())
    for yscale in range(201)[0:151:10]:
#            print yscale
        qp.drawLine(0, size.height()-yscale*ystep,size.width(),size.height()-yscale*ystep)
        qp.drawText(5,size.height()-yscale*ystep, "%s" %(yscale+50))

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
