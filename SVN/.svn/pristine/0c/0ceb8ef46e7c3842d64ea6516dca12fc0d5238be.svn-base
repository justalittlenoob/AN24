# -*- coding: utf-8 -*-
import PyQt4
from PyQt4 import QtGui, QtCore
#from Holter import *
import time

def cal_size(self):
    size = self.size()
    return size.width(), size.height()

def cal_ScaleY(window_rect, type, is_print = False):
    if is_print:
        window_height = window_rect.width()
    else:
        window_height  = window_rect.height()
    ystep=float(window_height)/36
    if type =='FHR':
        baseY = 16*ystep
        height = 16*ystep
        ystep = ystep
    elif type =='EHG':
        baseY = 22*ystep
        height = 6*ystep
        ystep = 1.5*ystep
    elif type =='MHR':
        baseY = 32*ystep
        height = 10*ystep
        ystep = ystep
    elif type =='MMov':
        baseY = 34.5*ystep
        height = 2.5*ystep
        ystep = 2.5*ystep
    elif type =='SNR':
        baseY = 36*ystep
        height = 1.5*ystep
        ystep = 1.5*ystep
    return baseY, height, ystep


def cal_unitXY(type, xstep, scaleY, xRatio):
    baseY, height, ystep = scaleY
    if type =='FHR':
        unitY = ystep/10
    elif type =='EHG':
        unitY = ystep/25
    elif type =='MHR':
        unitY = ystep/10
    elif type =='MMov':
        unitY = ystep/3
    elif type =='SNR':
        unitY  = ystep/2
    unitX = xstep/(4.0*60/xRatio)
    return unitX, unitY


def FHR_blockY(window_rect, FHR_limit, FHR_scaleY):
    bottom_limit,  lower_limit ,upper_limit, top_limit = FHR_limit
    baseY, height, ystep = FHR_scaleY
    bottom_line = baseY-height/(210-50)*(bottom_limit - 50)
    lower_line = baseY -height/(210-50)*(lower_limit - 50)
    upper_line = baseY -height/(210-50)*(upper_limit - 50)
    top_line = baseY- height/(210-50)*(top_limit - 50)
    return bottom_line, lower_line, upper_line, top_line

def paintBlock(self, qp, rgb,  rect):
    pen = QtGui.QPen(QtGui.QColor(165, 173, 181, 0), 1, QtCore.Qt.SolidLine)
    qp.setPen(pen)       
    qp.setBrush(QtGui.QColor(rgb[0], rgb[1], rgb[2], rgb[3]))
    qp.drawRect(rect[0],rect[1], rect[2], rect[3])

def paintCanvas(self, qp):
    window_width, window_height = cal_size(self)
    rgb = (255, 255, 255, 255)
    location = (0, 0, window_width, window_height)
    paintBlock(self, qp, rgb,  location)

def drawDividing(self, qp, y, window_rect, is_print = False):
    if is_print:
        window_height, window_width = window_rect.width(), window_rect.height()
        pen = QtGui.QPen(QtGui.QColor(165, 173, 181), 5, QtCore.Qt.SolidLine)
        qp.setPen(pen)   
        qp.drawLine(0, y-window_height, window_width,y -window_height)
    else:
        window_width, window_height = window_rect.width(), window_rect.height()
        pen = QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)   
        qp.drawLine(0, y, window_width,y)
    

def drawYScale(self, qp, window_rect, scaleY,  ytext_info, is_print = False):
    start_num, step_num, text_xposition = ytext_info
    baseY, height, ystep = scaleY
    amount = int(round(height/ystep))+1
    if is_print:
        width = window_rect.height()
        window_height = window_rect.width()
        pen = QtGui.QPen(QtGui.QColor(165, 173, 181), 3, QtCore.Qt.DotLine)
        qp.setFont(QtGui.QFont('Decorative', 80))  
        qp.setPen(pen)  
        for i in range(amount):
            qp.drawLine(0, baseY-i*ystep -window_height,width,baseY-i*ystep -window_height)
            qp.drawText(text_xposition,baseY-i*ystep -window_height, "%s" %(start_num + i*step_num))
    else:
        width = window_rect.width()
        pen = QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.DotLine)
        qp.setFont(QtGui.QFont('Decorative', 10)) 
        qp.setPen(pen)
        for i in range(amount):
            qp.drawLine(0, baseY-i*ystep,width,baseY-i*ystep)
            qp.drawText(text_xposition,baseY-i*ystep, "%s" %(start_num + i*step_num))
    

def xy2count(self,  x, start_count, FHR_unitXY):
    unitX, unitY = FHR_unitXY
    caled_count = start_count + x/unitX   
    return caled_count
    
def count2time(count, startTime):
    outTime = startTime+count/4
    timeScale = time.strftime('%H:%M:%S', time.localtime(outTime))
    return timeScale

def drawXScale(self, qp,   window_rect, unitXY, all_count, xRatio = 1, is_print = False, start_count = 0, end_count = 0, startTime = time.time()) :
    unitX, unitY = unitXY
    startTime = int(startTime)
    if xRatio ==1:
        min_perscale = 10
    elif xRatio ==2:
        min_perscale = 5
    elif xRatio ==3:
        min_perscale = 5
    
    for count in range(all_count):
        if ((start_count+count)*0.25+startTime)%60 ==0:
            first_scaleCount = count
            break
    scaleCount = range(first_scaleCount, all_count, 4*60)
    
    if is_print:        
        pen_dot = QtGui.QPen(QtGui.QColor(165, 173, 181), 3, QtCore.Qt.DotLine)
        pen_solid= QtGui.QPen(QtGui.QColor(165, 173, 181), 5, QtCore.Qt.SolidLine)
        qp.setFont(QtGui.QFont('Decorative', 80))
        window_height = window_rect.width()        
        for count in scaleCount:
            qp.setPen(pen_dot)
            qp.drawLine(unitX*count, -window_height, unitX*count, 0)
            if ((start_count+count)*0.25+startTime)%(60*min_perscale) ==0:
                qp.setPen(pen_solid)
                qp.drawLine(unitX*count, -window_height, unitX*count, 0)
                timeScale = count2time(start_count+count, startTime)
                for i in range(5):
                    qp.drawText(unitX*count,float(i)/4*window_height - window_height,timeScale)
    else:
        pen_dot = QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.DotLine)
        pen_solid= QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.SolidLine)
        qp.setFont(QtGui.QFont('Decorative', 10))
        window_height = window_rect.height()       
        for count in scaleCount:
            qp.setPen(pen_dot)
            qp.drawLine(unitX*count, 0, unitX*count, window_height)
            if ((start_count+count)*0.25+startTime)%(60*min_perscale) ==0:
                qp.setPen(pen_solid)
                qp.drawLine(unitX*count, 0, unitX*count, window_height)
                timeScale = count2time(start_count+count, startTime)
                for i in range(5):
                    qp.drawText(unitX*count,float(i)/4*window_height,timeScale)
    
def drawNote(self, qp, FHR_unitXY, all_count,  start_count,  end_count, xRatio,  note) :
    pen_solid= QtGui.QPen(QtGui.QColor(165, 173, 181), 1, QtCore.Qt.SolidLine)
    qp.setFont(QtGui.QFont('Decorative', 10))
    unitX, unitY = FHR_unitXY
    for note in note:
        if note[0]>start_count:
            note_x = unitX * (note[0]-start_count)
            note_y = note[1]*self.height()
            note = note[2]
            qp.drawText(note_x, note_y, note)

def cal_rect(window_rect, scaleY, is_print = False):
    baseY, height, ystep = scaleY
    if is_print:
        window_width = window_rect.height()
        window_height = window_rect.width()
        rect = (0,baseY- height+1-window_height, window_width, height)
    else:
        window_width = window_rect.width()
        rect = (0,baseY- height+1, window_width, height)
    return rect

def cal_FHRrect(window_rect, FHR_scaleY, FHR_limit, is_print = False):
    FHR_baseY = FHR_scaleY[0]
    if is_print:
        window_width = window_rect.height()
        window_height = window_rect.width()
        bottom_line, lower_line, upper_line, top_line = FHR_blockY(window_rect, FHR_limit, FHR_scaleY)
        print    FHR_baseY, bottom_line, lower_line, upper_line, top_line
        top_rect = (0,0-window_height, window_width, top_line+1) 
        high_rect = (0, top_line-window_height, window_width, upper_line - top_line+1)
        middle_rect = (0, upper_line-window_height, window_width, lower_line - upper_line+1)
        low_rect = (0,lower_line-window_height, window_width, bottom_line-lower_line+1)
        bottom_rect = (0,bottom_line-window_height, window_width, FHR_baseY-bottom_line+1)
    else:
        window_width = window_rect.width()
        bottom_line, lower_line, upper_line, top_line = FHR_blockY(window_rect, FHR_limit,  FHR_scaleY)      
        top_rect = (0,0, window_width, top_line+1) 
        high_rect = (0, top_line, window_width, upper_line - top_line+1)
        middle_rect = (0, upper_line, window_width, lower_line - upper_line+1)
        low_rect = (0,lower_line, window_width, bottom_line-lower_line+1)
        bottom_rect = (0,bottom_line, window_width, FHR_baseY-bottom_line+1)
    return [top_rect, high_rect,  middle_rect,  low_rect,  bottom_rect]

def paintBg(self, qp, window_rect, bg_rgb, bg_rect, bg_scaleY, FHR_rect, FHR_rgb, ytext_info, is_print = False):
    for key in bg_rgb:
        paintBlock(self, qp,bg_rgb[key], bg_rect[key])
    for i in range(5):
        paintBlock(self, qp, FHR_rgb[i], FHR_rect[i])
    for key in ytext_info:
        drawYScale(self, qp, window_rect, bg_scaleY[key],  ytext_info[key],  is_print)
    for key in bg_rect:
        drawDividing(self, qp, bg_scaleY[key][0], window_rect, is_print)       

def cal_realCount(window_rect, xstep, xyRatio, screen_ratio, is_print = False):
    if is_print:
        window_width = window_rect.height() 
    else:
        window_width = window_rect.width() 
    realCount = window_width*screen_ratio/xstep*(240/xyRatio)
    return int(realCount)

def realtime_monitor(self, qp, Cache, start_count, end_count, scaleY,  unitXY, pen, window_rect = '', is_print = False):
    cachePre=[]
    i=0
    if is_print:
        window_height = window_rect.width()
    for cache in Cache[start_count:end_count]:
        if i!=0 and cache[0]!=0 and cachePre[0]!=0:
            baseY, height, ystep = scaleY['FHR']    
            unitX, unitY = unitXY['FHR']
            qp.setPen(pen['FHR']) 
            if is_print:                
                qp.drawLine(unitX*(i-1), baseY-unitY*(cachePre[0]-50) - window_height, unitX*i, baseY-unitY*(cache[0]-50)- window_height)
            else:
                qp.drawLine(unitX*(i-1), baseY-unitY*(cachePre[0]-50), unitX*i, baseY-unitY*(cache[0]-50))
        
        if i!=0 and cache[2]!=0 and cachePre[2]!=0:
            baseY, height, ystep = scaleY['EHG']    
            unitX, unitY = unitXY['EHG']
            qp.setPen(pen['EHG']) 
            if is_print:
                qp.drawLine(unitX*(i-1), baseY-unitY*(float(cachePre[2])/255*100)- window_height, unitX*i, baseY-unitY*(float(cache[2])/255*100)- window_height)
            else:
                qp.drawLine(unitX*(i-1), baseY-unitY*(float(cachePre[2])/255*100), unitX*i, baseY-unitY*(float(cache[2])/255*100))
        
        if i!=0 and cache[1]!=0 and cachePre[1]!=0:
            baseY, height, ystep = scaleY['MHR']    
            unitX, unitY = unitXY['MHR']
            qp.setPen(pen['MHR']) 
            if is_print:
                qp.drawLine(unitX*(i-1), baseY-unitY*(cachePre[1]-40)- window_height, unitX*i, baseY-unitY*(cache[1]-40)- window_height)
            else:
                qp.drawLine(unitX*(i-1), baseY-unitY*(cachePre[1]-40), unitX*i, baseY-unitY*(cache[1]-40))
        
        baseY, height, ystep = scaleY['MMov']    
        unitX, unitY = unitXY['MMov']
        qp.setPen(pen['MMov']) 
        if cache[3]!=0:
            if is_print:
                qp.drawRect(unitX*i,baseY- window_height , unitX, -cache[3]*unitY+2)
            else:
                qp.drawRect(unitX*i,baseY, unitX, -cache[3]*unitY+2)
        else:
            if is_print:
                qp.drawRect(unitX*i,baseY- window_height, unitX,-1)
            else:
                qp.drawRect(unitX*i,baseY, unitX,-1)
        
        baseY, height, ystep = scaleY['SNR']    
        unitX, unitY = unitXY['SNR']
        qp.setPen(pen['SNR'])
        #qp.setBrush(QtGui.QColor(255, 155, 248, 100))
        if cache[4]!=0:
            if is_print:
                qp.drawRect(unitX*i,baseY- window_height, unitX, -cache[4]*unitY)
            else:
                qp.drawRect(unitX*i,baseY, unitX, -cache[4]*unitY)
        else:
            if is_print:
                qp.drawRect(unitX*i,baseY- window_height, unitX, 0)
            else:
                qp.drawRect(unitX*i,baseY, unitX, 0)
        
        if cache[5]!=0:  
            unitX, unitY = unitXY['FHR']
            qp.setPen(pen['Event']) 
            if is_print:
                qp.drawLine(unitX*i, 0 - window_height, unitX *i,0)
            else:
                qp.drawLine(unitX*i, 0, unitX *i,self.size().height())
        cachePre=cache
        i+=1
        
#def realFHR(self, qp, Cache, start_count, end_count, scaleY,  unitXY, rgb):
#    pen = QtGui.QPen(QtGui.QColor(rgb[0], rgb[1], rgb[2]), 1, QtCore.Qt.SolidLine)
#    qp.setPen(pen)    
#    baseY, height, ystep = scaleY    
#    unitX, unitY = unitXY
#    cachePre=[]
#    i=0
#    for cache in Cache[start_count:end_count]:
#        if i!=0 and cache[0]!=0 and cachePre[0]!=0:
#            qp.drawLine(unitX*(i-1), baseY-unitY*(cachePre[0]-50), unitX*i, baseY-unitY*(cache[0]-50))
#        
#        cachePre=cache
#        i+=1
#
#def realEHG(self, qp, Cache, start_count, end_count, scaleY,  unitXY, rgb):
#    pen = QtGui.QPen(QtGui.QColor(rgb[0], rgb[1], rgb[2]), 1, QtCore.Qt.SolidLine)
#    qp.setPen(pen)
#    baseY, height, ystep = scaleY    
#    unitX, unitY = unitXY
#    cachePre=[]
#    i=0
#    for cache in Cache[start_count: end_count]:
#        if i!=0 and cache[2]!=0 and cachePre[2]!=0:
#            qp.drawLine(unitX*(i-1), baseY-unitY*(float(cachePre[2])/255*100), unitX*i, baseY-unitY*(float(cache[2])/255*100))
#        cachePre=cache
#        i+=1
#
#def realMHR(self, qp, Cache, start_count, end_count, scaleY,  unitXY, rgb):
#    pen = QtGui.QPen(QtGui.QColor(rgb[0], rgb[1], rgb[2]), 1, QtCore.Qt.SolidLine)
#    qp.setPen(pen)
#    baseY, height, ystep = scaleY    
#    unitX, unitY = unitXY
#    cachePre=[]
#    i=0
#    for cache in Cache[start_count: end_count]:
#        if i!=0 and cache[1]!=0 and cachePre[1]!=0:
#            qp.drawLine(unitX*(i-1), baseY-unitY*(cachePre[1]-40), unitX*i, baseY-unitY*(cache[1]-40))
#        cachePre=cache
#        i+=1
#
#def realMMov(self, qp, Cache, start_count, end_count, scaleY,  unitXY, rgb):
#    pen = QtGui.QPen(QtGui.QColor(rgb[0], rgb[1], rgb[2]), 1, QtCore.Qt.SolidLine)
#    qp.setPen(pen)
#    baseY, height, ystep = scaleY    
#    unitX, unitY = unitXY
#    cachePre=[]
#    i=0
#    for cache in Cache[start_count: end_count]:
#        if cache[3]!=0:
#            qp.drawRect(unitX*i,baseY, unitX, -cache[3]*unitY)
#        else:
#            qp.drawRect(unitX*i,baseY, unitX,0)
#        i+=1
#
#def realSNR(self, qp, Cache, start_count, end_count, scaleY,  unitXY, rgb):
#    pen = QtGui.QPen(QtGui.QColor(144, 159, 248), 1, QtCore.Qt.SolidLine)
#    qp.setPen(pen)
#    qp.setBrush(QtGui.QColor(rgb[0], rgb[1], rgb[2], rgb[3]))
#    baseY, height, ystep = scaleY    
#    unitX, unitY = unitXY
#    cachePre=[]
#    i=0
#    for cache in Cache[start_count: end_count]:
#        if cache[4]!=0:
#            qp.drawRect(unitX*i,baseY, unitX, -cache[4]*unitY)
#        else:
#            qp.drawRect(unitX*i,baseY, unitX, 0)
#        i+=1
#
#def realEvent(self, qp, Cache, start_count, end_count, unitXY, rgb):
#    pen = QtGui.QPen(QtGui.QColor(rgb[0], rgb[1], rgb[2]), 1, QtCore.Qt.SolidLine)
#    qp.setPen(pen) 
#    unitX, unitY = unitXY
#    cachePre=[]
#    i=0
#    for cache in Cache[start_count: end_count]:
#        if cache[5]!=0:
#            #qp.drawRect(xpoint*i,0, xpoint, ystep*32)
#            qp.drawLine(unitX*i, 0, unitX *i,self.size().height())
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
        
        
def realtime_printer(self, qp, Cache, start_count, split_count, scaleY,  unitXY, pen, window_rect = ''):
    cachePre=[]
    i=0
    window_height = window_rect.width()
    for cache in Cache[start_count:split_count]:
        if i!=0 and cache[0]!=0 and cachePre[0]!=0:
            baseY, height, ystep = scaleY['FHR']    
            unitX, unitY = unitXY['FHR']
            qp.setPen(pen['FHR'])                 
            qp.drawLine(unitX*(i-1), baseY-unitY*(cachePre[0]-50) - window_height, unitX*i, baseY-unitY*(cache[0]-50)- window_height)
        
        if i!=0 and cache[2]!=0 and cachePre[2]!=0:
            baseY, height, ystep = scaleY['EHG']    
            unitX, unitY = unitXY['EHG']
            qp.setPen(pen['EHG']) 
            qp.drawLine(unitX*(i-1), baseY-unitY*(float(cachePre[2])/255*100)- window_height, unitX*i, baseY-unitY*(float(cache[2])/255*100)- window_height)
        
        if i!=0 and cache[1]!=0 and cachePre[1]!=0:
            baseY, height, ystep = scaleY['MHR']    
            unitX, unitY = unitXY['MHR']
            qp.setPen(pen['MHR']) 
            qp.drawLine(unitX*(i-1), baseY-unitY*(cachePre[1]-40)- window_height, unitX*i, baseY-unitY*(cache[1]-40)- window_height)
        
        baseY, height, ystep = scaleY['MMov']    
        unitX, unitY = unitXY['MMov']
        qp.setPen(pen['MMov']) 
        if cache[3]!=0:
            qp.drawRect(unitX*i,baseY- window_height , unitX, -cache[3]*unitY+2)
        else:
            qp.drawRect(unitX*i,baseY- window_height, unitX,-1)
        
        baseY, height, ystep = scaleY['SNR']    
        unitX, unitY = unitXY['SNR']
        qp.setPen(pen['SNR'])
        #qp.setBrush(QtGui.QColor(255, 155, 248, 100))
        if cache[4]!=0:
            qp.drawRect(unitX*i,baseY- window_height, unitX, -cache[4]*unitY)
        else:
            qp.drawRect(unitX*i,baseY- window_height, unitX, 0)
        
        if cache[5]!=0:  
            unitX, unitY = unitXY['FHR']
            qp.setPen(pen['Event']) 
            qp.drawLine(unitX*i, 0 - window_height, unitX *i,0)
        cachePre=cache
        i+=1

def print_drawXScale(self, qp,   window_rect, unitXY, all_count, xRatio = 1,  start_count = 0, split_count = 0, startTime = time.time()) :
    unitX, unitY = unitXY
    startTime = int(startTime)
    if xRatio ==1:
        min_perscale = 10
    elif xRatio ==2:
        min_perscale = 5
    elif xRatio ==3:
        min_perscale = 5
    
    for count in range(all_count):
        if ((start_count+count)*0.25+startTime)%60 ==0:
            first_scaleCount = count
            break
    scaleCount = range(first_scaleCount, all_count, 4*60)
    
    pen_dot = QtGui.QPen(QtGui.QColor(165, 173, 181), 3, QtCore.Qt.DotLine)
    pen_solid= QtGui.QPen(QtGui.QColor(165, 173, 181), 5, QtCore.Qt.SolidLine)
    qp.setFont(QtGui.QFont('Decorative', 80))
    window_height = window_rect.width()        
    for count in scaleCount:
        qp.setPen(pen_dot)
        qp.drawLine(unitX*count, -window_height, unitX*count, 0)
        if ((start_count+count)*0.25+startTime)%(60*min_perscale) ==0:
            qp.setPen(pen_solid)
            qp.drawLine(unitX*count, -window_height, unitX*count, 0)
            timeScale = count2time(start_count+count, startTime)
            for i in range(5):
                qp.drawText(unitX*count,float(i)/4*window_height - window_height,timeScale)
