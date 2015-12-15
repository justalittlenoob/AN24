# -*- coding: utf-8 -*-

"""
Module implementing Holter.
"""
import sys, PyQt4, winsound, time

from PyQt4.QtGui import (QMainWindow, QPainter, QPrinter,QPrintDialog,  QImage, QPicture)  
from PyQt4.QtCore import (pyqtSignature, QTimer,  SIGNAL, QPropertyAnimation, Qt)
from Ui_Holter import Ui_Holter
from PaintRealTime import *
from Search import Search
from Settings import  *
from review import  ReviewClient
        
class Holter(QMainWindow, Ui_Holter):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)   
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.createContextMenu()
        self.create_animation()   
        self.init_var()
        self.init_settings() 
        self.paint_calculation()
    
    def init_var(self):
        self.end_count = 0
        self.start_count = 0
        self.cache_count = 0
        self.is_firstShow = True 
        self.start_time = 0               
        self.is_detecting = False      
    
    def init_settings(self):
        self.xyRatio = 1
        self.screen_ratio = 0.8
        self.is_soundOn = True
        self.FHR_limit = [80, 110,140, 180]
        self.is_frame_shown = True
        self.print_minutes = 20
        self.print_lines = 3
    
    def paint_calculation(self):
        self.window_rect = self.size()
        self.bg_scaleY = {'FHR':cal_ScaleY(self.window_rect,'FHR'), 
                            'EHG':cal_ScaleY(self.window_rect,'EHG'), 
                            'MHR':cal_ScaleY( self.window_rect,'MHR'), 
                            'MMov':cal_ScaleY(self.window_rect,'MMov'), 
                            'SNR':cal_ScaleY(self.window_rect,'SNR')
                            }
        self.bg_rgb = {'EHG':(255, 255, 255, 200), 
                            'MHR':(191, 229, 253, 150), 
                            'MMov':(220, 248, 146, 100), 
                            'SNR':(251, 249, 116, 100)
                            }
        self.bg_rect = {'FHR':cal_rect(self.window_rect, self.bg_scaleY['FHR']) , 
                            'EHG':cal_rect(self.window_rect, self.bg_scaleY['EHG']) , 
                            'MHR':cal_rect(self.window_rect, self.bg_scaleY['MHR']) , 
                            'MMov':cal_rect(self.window_rect, self.bg_scaleY['MMov']) , 
                            'SNR':cal_rect(self.window_rect, self.bg_scaleY['SNR']) 
                            }
        self.FHR_rect = cal_FHRrect(self.window_rect, self.bg_scaleY['FHR'], self.FHR_limit)
        self.FHR_rgb = [(247, 220, 230, 200), 
                            (255, 251, 190, 160), 
                            (255, 255, 255, 200), 
                            (255, 251, 190, 160), 
                            (247, 220, 230, 200)
                            ]
        width = self.window_rect.width()
        self.ytext_info = {'FHR':[50, 10, 5], 
                                'EHG':[0, 25,width-30], 
                                'MHR':[40, 10, 5]
                                }    
        self.xstep = self.bg_scaleY['FHR'][2]*2                            
        self.unitXY = {'FHR': cal_unitXY('FHR',self.xstep, self.bg_scaleY['FHR'], self.xyRatio), 
                        'EHG': cal_unitXY('EHG',self.xstep, self.bg_scaleY['EHG'], self.xyRatio), 
                        'MHR': cal_unitXY('MHR',self.xstep, self.bg_scaleY['MHR'], self.xyRatio), 
                        'MMov': cal_unitXY('MMov',self.xstep, self.bg_scaleY['MMov'], self.xyRatio), 
                        'SNR': cal_unitXY('SNR',self.xstep, self.bg_scaleY['SNR'], self.xyRatio) 
                        }
        self.line_rgb = {'FHR':(35, 78, 220), 
                            'EHG':(0, 0, 0), 
                            'MHR':(148, 48, 34), 
                            'MMov':(116, 186, 106), 
                            'SNR':(144, 159, 248, 100), 
                            'Event': (204, 138, 138)
                            }
        self.all_count = cal_realCount(self.window_rect, self.xstep, self.xyRatio, 1)
        self.pen ={'FHR': QtGui.QPen(QtGui.QColor(35, 78, 220), 1, QtCore.Qt.SolidLine), 
                        'EHG':QtGui.QPen(QtGui.QColor(0, 0, 0), 1, QtCore.Qt.SolidLine), 
                        'MHR':QtGui.QPen(QtGui.QColor(148, 48, 34), 1, QtCore.Qt.SolidLine), 
                        'MMov':QtGui.QPen(QtGui.QColor(116, 186, 106), 1, QtCore.Qt.SolidLine), 
                        'SNR': QtGui.QPen(QtGui.QColor(144, 159, 248, 100), 1, QtCore.Qt.SolidLine), 
                        'Event':QtGui.QPen(QtGui.QColor(204, 138, 138), 1, QtCore.Qt.SolidLine) 
                        }
        
    def create_animation(self):
        self.animation_hide = QPropertyAnimation(self.frame, "geometry")
        self.animation_hide.setDuration(500)
#        self.animation_hide.setStartValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
#        self.animation_hide.setEndValue(PyQt4.QtCore.QRect(self.size().width()-100, 70, 171, 671))
        self.animation_show = QPropertyAnimation(self.frame, "geometry")
        self.animation_show.setDuration(500)
#        self.animation_show.setStartValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
#        self.animation_show.setEndValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        
    def paintEvent(self, event):        
        qp = PyQt4.QtGui.QPainter()       
        qp.begin(self)
        paintBg(self, qp, self.window_rect, self.bg_rgb, self.bg_rect, self.bg_scaleY, self.FHR_rect, self.FHR_rgb, self.ytext_info)
        try:
            self.review_cl
        except AttributeError, reason:
            is_detecting = False
            #print 'paintEvent-> you have not add an divice. <reason>', reason
        except KeyError, reason:
            is_detecting = False
            #print 'paintEvent-> you need to choose one divice. <reason>', reason
        else:
            is_detecting = self.is_detecting
        
        if is_detecting:
            Cache = self.review_cl.his_data
            start_time = self.start_time
            realCount = self.all_count
            if self.is_firstShow == True:
                self.end_count = realCount   
                self.is_firstShow = False
            end_count = self.end_count 
            start_count = self.start_count
            if end_count>realCount:
                end_count=start_count+int(realCount)
            else:
                start_count = 0
            note = self.review_cl.his_note
            realtime_monitor(self, qp, Cache, start_count, end_count, self.bg_scaleY,  self.unitXY, self.pen)    
            drawXScale(self, qp,  self.window_rect, self.unitXY['FHR'], self.all_count, self.xyRatio, False, start_count, end_count ,  start_time)
            drawNote(self, qp, self.unitXY['FHR'], self.all_count,  start_count,  end_count, self.xyRatio, note)
        else:
            drawXScale(self, qp,  self.window_rect, self.unitXY['FHR'], self.all_count,  self.xyRatio)
        qp.end()
        
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if not self.is_frame_shown:
                self.animation_show.start()
            else:
                self.animation_hide.start()
            self.is_frame_shown = not self.is_frame_shown 
    
    def resizeEvent(self, event):
        self.paint_calculation()
        self.animation_hide.setStartValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        self.animation_hide.setEndValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setStartValue(PyQt4.QtCore.QRect(self.size().width(), 70, 171, 671))
        self.animation_show.setEndValue(PyQt4.QtCore.QRect(self.size().width()-188,70, 171, 671))
        self.button_position()
        print 'resize'
        
    def update_paint(self):
        try:
            self.review_cl
        except KeyError, reason:
            self.repaint()
        else:
            #print self.an24Dict[nameChosen].name, self.an24Dict[nameChosen].is_checked
            if self.is_detecting ==True:
                self.repaint()
               

    def button_position(self):
        if self.is_frame_shown:
            self.frame.setGeometry(QtCore.QRect(self.size().width()-188,70, 171,671))
        else:
            self.frame.setGeometry(QtCore.QRect(self.size().width(),70, 171,671))
            
        self.frame_2.setGeometry(QtCore.QRect(0,0, self.size().width(),51))
        
    @pyqtSignature("")
    def on_xscale1_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 1
        self.paint_calculation()
        self.repaint()

    
    @pyqtSignature("")
    def on_xscale2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 2
        self.paint_calculation()
        self.repaint()
    
    @pyqtSignature("")
    def on_xscale3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.xyRatio = 3
        self.paint_calculation()
        self.repaint()
    
    def start_detecting(self, info_uuid):
        try:        
            self.review_cl
        except KeyError, reason:
            QtGui.QMessageBox.information( self, "notice", "the class ReviewClient not established" )
        else:
            self.info_uuid = info_uuid
            if info_uuid[1]:
                str_ST=info_uuid[0][8]  
                struct_ST = time.strptime(str_ST,'%Y-%m-%d %H:%M:%S')
                self.start_time  =  time.mktime(struct_ST)
                self.review_cl.review(info_uuid[1])
                pre_len = 0
                while 1:
                    #print len(self.an24Dict[nameChosen].rawAN24.cache)
                    time.sleep(1)
                    if len(self.review_cl.his_data)!=0:
                        break
                self.cache_count = len(self.review_cl.his_data)
                self.is_detecting = True
                self.update_patient_info()
                self.update_paint()                    
        
    def update_patient_info(self):
        print self.info_uuid
        self.label_name.setText(u'名字：'+self.info_uuid[0][0])
        #self.label_age.setText(u'年龄：'+str(patient_info['age']))
        #self.label_weeks.setText(u'孕周：'+str(patient_info['weeks']))
        #self.label_outpatient.setText(u'门诊号：'+patient_info['outpatient_num'])
        self.label_hospitalization.setText(u'住院号：'+self.info_uuid[0][1])
        self.label_bed.setText(u'病床号：'+self.info_uuid[0][7])
        #self.label_guardianship.setText(u'监护号：'+patient_info['guardianship_num'])
        self.update()
       
    @pyqtSignature("bool")    
    def on_pinTest_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        pass 
        
    @pyqtSignature("")
    def on_pushButtonSettings_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        settings = DlgSettings.change_settings()
        self.FHR_limit = settings[0]
        self.paint_calculation()
        self.print_minutes = settings[1]
        
    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
    
    def showContextMenu(self, pos):
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu = QtGui.QMenu(self)
        self.actionA = self.contextMenu.addAction(u'添加注释')
        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.actionA.triggered.connect(self.add_note)
        
        self.cursor_pos = pos
        self.contextMenu.move(self.pos() +self.cursor_pos)
        self.contextMenu.show()

    def print_calculation(self, print_window_rect,  print_pic_rect, line_no):
        self.print_window_rect = print_window_rect
        self.print_pic_rect = print_pic_rect
        self.print_bg_scaleY = {'FHR':cal_ScaleY(self.print_window_rect,'FHR', True, self.print_lines,  line_no), 
                            'EHG':cal_ScaleY(self.print_window_rect,'EHG', True, self.print_lines,  line_no), 
                            'MHR':cal_ScaleY( self.print_window_rect,'MHR', True,  self.print_lines,  line_no), 
                            'MMov':cal_ScaleY(self.print_window_rect,'MMov', True, self.print_lines,  line_no), 
                            'SNR':cal_ScaleY(self.print_window_rect,'SNR', True,  self.print_lines,  line_no)
                            }
        self.print_bg_rgb = {'EHG':(255, 255, 255, 200), 
                            'MHR':(191, 229, 253, 150), 
                            'MMov':(220, 248, 146, 100), 
                            'SNR':(251, 249, 116, 100)
                            }
        self.print_bg_rect = {'FHR':cal_rect(self.print_window_rect , self.print_bg_scaleY['FHR'], True) , 
                            'EHG':cal_rect(self.print_window_rect , self.print_bg_scaleY['EHG'], True) , 
                            'MHR':cal_rect(self.print_window_rect, self.print_bg_scaleY['MHR'], True) , 
                            'MMov':cal_rect(self.print_window_rect, self.print_bg_scaleY['MMov'], True) , 
                            'SNR':cal_rect(self.print_window_rect, self.print_bg_scaleY['SNR'], True) 
                            }
        self.print_FHR_rect = cal_FHRrect(self.print_window_rect, self.print_bg_scaleY['FHR'], self.FHR_limit, True, self.print_pic_rect)
        self.print_FHR_rgb = [(247, 220, 230, 200), 
                            (255, 251, 190, 160), 
                            (255, 255, 255, 200), 
                            (255, 251, 190, 160), 
                            (247, 220, 230, 200)
                            ]
        width = self.print_window_rect.height()
        self.print_ytext_info = {'FHR':[50, 10, 100], 
                                'EHG':[0, 25,width-300], 
                                'MHR':[40, 10, 100]
                                }    
        self.print_xstep = self.print_bg_scaleY['FHR'][2]*2                            
        self.print_unitXY = {'FHR': cal_unitXY('FHR',self.print_xstep, self.print_bg_scaleY['FHR'], self.xyRatio), 
                        'EHG': cal_unitXY('EHG',self.print_xstep, self.print_bg_scaleY['EHG'], self.xyRatio), 
                        'MHR': cal_unitXY('MHR',self.print_xstep, self.print_bg_scaleY['MHR'], self.xyRatio), 
                        'MMov': cal_unitXY('MMov',self.print_xstep, self.print_bg_scaleY['MMov'], self.xyRatio), 
                        'SNR': cal_unitXY('SNR',self.print_xstep, self.print_bg_scaleY['SNR'], self.xyRatio) 
                        }
        self.print_line_rgb = {'FHR':(35, 78, 220), 
                            'EHG':(0, 0, 0), 
                            'MHR':(148, 48, 34), 
                            'MMov':(116, 186, 106), 
                            'SNR':(144, 159, 248, 100), 
                            'Event': (204, 138, 138)
                            }
        self.print_all_count = cal_realCount(self.print_window_rect, self.print_xstep, self.xyRatio, 1, True)
        self.print_pen ={'FHR': QtGui.QPen(QtGui.QColor(35, 78, 220), 5, QtCore.Qt.SolidLine), 
                        'EHG':QtGui.QPen(QtGui.QColor(0, 0, 0),5, QtCore.Qt.SolidLine), 
                        'MHR':QtGui.QPen(QtGui.QColor(148, 48, 34), 5, QtCore.Qt.SolidLine), 
                        'MMov':QtGui.QPen(QtGui.QColor(116, 186, 106), 5, QtCore.Qt.SolidLine), 
                        'SNR': QtGui.QPen(QtGui.QColor(144, 159, 248, 100), 5, QtCore.Qt.SolidLine), 
                        'Event':QtGui.QPen(QtGui.QColor(204, 138, 138), 5, QtCore.Qt.SolidLine) 
                        }
    
    @pyqtSignature("")
    def on_pushStepForward_clicked(self):
        if self.end_count + 240 <= self.cache_count:
            self.start_count+=240
            self.end_count+=240
            self.update_paint()
    
    @pyqtSignature("")
    def on_pushStepBack_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.start_count - 240 >= 0:
            self.start_count-= 240
            self.end_count-=240
            self.update_paint()
    
    @pyqtSignature("")
    def on_pushForward_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.end_count + self.all_count <= self.cache_count:
            self.start_count+=self.all_count
            self.end_count+=self.all_count
            self.update_paint()
    
    @pyqtSignature("")
    def on_pushBack_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.start_count - self.all_count >= 0:
            self.start_count-=self.all_count
            self.end_count-=self.all_count
            self.update_paint()
    
    @pyqtSignature("")
    def on_pushButtonDownload_clicked(self):
        """
        Slot documentation goes here.
        """
        info_uuid = DlgSearch.show_self()
        self.start_detecting(info_uuid)
    
    @pyqtSignature("")
    def on_pushPrint_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Print(self.print_minutes)
    
    def Print(self, print_minutes):  
        time_scale = 40
        time_count = print_minutes*240
        is_lastPage = True
        is_printOver = False
        
        self.printer=QPrinter()
        printDialog=QPrintDialog(self.printer,self)  
        qp = QPainter() 
        i = 0
        
        try:
            self.review_cl
        except AttributeError, reason:
            is_detecting = False
            #print 'paintEvent-> you have not add an divice. <reason>', reason
        except KeyError, reason:
            is_detecting = False
            #print 'paintEvent-> you need to choose one divice. <reason>', reason
        else:
            is_detecting =self.is_detecting
            end_count = len(self.review_cl.his_data)   
        
        if printDialog.exec_(): 
            if self.print_lines ==1:
                while time_count >0:
                    self.image=QImage()  
                    self.image.load("D:/aaa.png")
                    size=self.image.size()
                    self.print_calculation(size, size, 1)
                    print_window_rect = self.print_window_rect
                    
                    self.painter=QPainter(self.printer)  
                    viewport=self.painter.viewport()  
                    self.pic = QPicture()
                    self.pic.width = 6300
                    self.pic.height = 8910
                    qp.begin(self.pic)  
                    qp.rotate(90)
                    print print_window_rect
                    paintBg(self, qp, print_window_rect , self.print_bg_rgb, self.print_bg_rect, self.print_bg_scaleY, self.print_FHR_rect, self.print_FHR_rgb, self.print_ytext_info, True)
                    realCount = cal_realCount(print_window_rect, self.print_xstep, self.xyRatio, self.screen_ratio, True)
                    
                    if is_detecting:
                        Cache = self.review_cl.his_data
                        start_time = self.start_time                    
                        if is_lastPage:
                            if end_count>realCount:                            
                                start_count = end_count-int(realCount)
                            elif time_count > end_count:
                                start_count = 0
                            else:
                                start_count = end_count - time_count
                        else:
                            if end_count>self.print_all_count:
                                start_count = end_count - int(self.print_all_count)
                            else:
                                start_count = 0
                        note = self.review_cl.his_note
                        realtime_monitor(self, qp, Cache, start_count, end_count, self.print_bg_scaleY,  self.print_unitXY, self.print_pen, self.print_window_rect, True)    
                        drawXScale(self, qp,  print_window_rect, self.print_unitXY['FHR'], self.print_all_count, self.xyRatio, True, start_count, end_count , start_time)
                        if is_lastPage:
                            if end_count < realCount:
                                is_printOver = True
                            else:                            
                                time_count -= realCount
                                print 'lastPage',time_count 
                        else:
                            if end_count < self.print_all_count:
                                is_printOver = True
                            else:                            
                                time_count -= self.print_all_count
                                print 'not lastPage', time_count
                        is_lastPage = False
                        print 'endCount', end_count
                        end_count = start_count
                        print 'new endCount', end_count
        #                drawNote(self, qp, self.print_unitXY['FHR'], self.print_all_count,  start_count,  end_count, self.xyRatio, note)
        #                Hour, Minute, Second = self.get_rest_time(self.an24Dict[nameChosen].start_time,self.an24Dict[nameChosen].all_battry_time ) 
        
                    else:
                        drawXScale(self, qp,  print_window_rect, self.print_unitXY['FHR'], self.print_all_count,  self.xyRatio, True)
                        is_printOver = True
                    qp.end() 
                    print '1', size.width()   
                    size.scale(viewport.size(),Qt.KeepAspectRatio)  
                    print '2', size.width(), viewport.size()
                    self.painter.setViewport(viewport.x()+10,viewport.y()+10,size.width()-20,size.height()-20)   
                    print '3', size.width(), self.painter.viewport()
                    self.painter.setWindow(self.image.rect())
                    print '4', self.image.rect()
                    #self.painter.setWindow(0, 0, 6300, 8910)
                    self.painter.drawPicture(0,0,self.pic) 
                    self.painter.end()  
                    if is_printOver:
                        break
          
            elif self.print_lines !=1: 
                line_no = 2  
                while time_count >0:
                    self.image=QImage()  
                    self.image.load("D:/aaa.png")
                    size=self.image.size()
                    self.print_calculation(QtCore.QRect(0, 0, self.image.width()/self.print_lines, 8910), QtCore.QRect(0, 0, self.image.width()/self.print_lines, 8910), line_no)
                    print 'self.print_lines', self.print_lines, 'line_no', line_no
                    print_window_rect = self.print_window_rect
                    
                    self.painter=QPainter(self.printer)  
                    viewport=self.painter.viewport()  
                    self.pic = QPicture()
                    self.pic.width = 6300
                    self.pic.height = 8910
                    qp.begin(self.pic)  
                    qp.rotate(90)
                    print print_window_rect
                    paintBg(self, qp, print_window_rect , self.print_bg_rgb, self.print_bg_rect, self.print_bg_scaleY, self.print_FHR_rect, self.print_FHR_rgb, self.print_ytext_info, True)
                    realCount = cal_realCount(print_window_rect, self.print_xstep, self.xyRatio, self.screen_ratio, True)
                    
                    if is_detecting:
                        Cache = self.review_cl.his_data
                        start_time = self.start_time                    
                        if is_lastPage:
                            if end_count>realCount:                            
                                start_count = end_count-int(realCount)
                            elif time_count > end_count:
                                start_count = 0
                            else:
                                start_count = end_count - time_count
                        else:
                            if end_count>self.print_all_count:
                                start_count = end_count - int(self.print_all_count)
                            else:
                                start_count = 0
                        note = self.review_cl.his_note
                        realtime_monitor(self, qp, Cache, start_count, end_count, self.print_bg_scaleY,  self.print_unitXY, self.print_pen, self.print_window_rect, True)    
                        drawXScale(self, qp,  print_window_rect, self.print_unitXY['FHR'], self.print_all_count, self.xyRatio, True, start_count, end_count , start_time)
                        if is_lastPage:
                            if end_count < realCount:
                                is_printOver = True
                            else:                            
                                time_count -= realCount
                                print 'lastPage',time_count 
                        else:
                            if end_count < self.print_all_count:
                                is_printOver = True
                            else:                            
                                time_count -= self.print_all_count
                                print 'not lastPage', time_count
                        is_lastPage = False
                        print 'endCount', end_count
                        end_count = start_count
                        print 'new endCount', end_count
        #                drawNote(self, qp, self.print_unitXY['FHR'], self.print_all_count,  start_count,  end_count, self.xyRatio, note)
        #                Hour, Minute, Second = self.get_rest_time(self.an24Dict[nameChosen].start_time,self.an24Dict[nameChosen].all_battry_time ) 
        
                    else:
                        drawXScale(self, qp,  print_window_rect, self.print_unitXY['FHR'], self.print_all_count,  self.xyRatio, True)
                        is_printOver = True
                    qp.end() 
                    print '1', size.width()   
                    size.scale(viewport.size(),Qt.KeepAspectRatio)  
                    print '2', size.width(), viewport.size()
                    self.painter.setViewport(viewport.x()+10,viewport.y()+10,size.width()-20,size.height()-20)   
                    print '3', size.width(), self.painter.viewport()
                    self.painter.setWindow(self.image.rect())
                    print '4', self.image.rect()
                    #self.painter.setWindow(0, 0, 6300, 8910)
                    self.painter.drawPicture(0,0,self.pic) 
                    self.painter.end()  
                    if is_printOver:
                        break              

if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)    
    qTranslator = PyQt4.QtCore.QTranslator()
    qTranslator.load("./Chinese.qm")
    app.installTranslator(qTranslator)
    ist = Holter()    
    ist.review_cl = ReviewClient()
    DlgSearch = Search(ist.review_cl)
    DlgSettings = Settings()
    ist.show()
    info_uuid = DlgSearch.show_self()
    ist.start_detecting(info_uuid)
    sys.exit(app.exec_())
    

