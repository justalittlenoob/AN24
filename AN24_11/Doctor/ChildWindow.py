# -*- coding: utf-8 -*-

"""
Module implementing ChildWindow.
"""
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import (pyqtSignature, Qt)
from PaintRealTime import *
from Ui_ChildWindow import Ui_ChildWindow
from FillNote import  FillNote
from FillPatient import FillPatient

class ChildWindow(QWidget, Ui_ChildWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.is_max = False
        self.DlgFillNote = FillNote()
        self.createContextMenu()
                     
    def update_paint(self,   PCal,  dictChosen):  
        self.dictChosen = dictChosen
        self.PCal = PCal
        try:
            Cache = self.dictChosen.data_handler.data
        except Exception, reason:
            print Exception, reason
        else:
            self.PCal.reatime_cal(Cache)
            self.listen_RunChk(self.dictChosen)
            self.listen_LowBat(self.dictChosen)
        return self.is_max
    
    def paintEvent(self, event):
        try:
            PCal = self.PCal
        except Exception, reason:
            print Exception, reason
        else:
            qp = PyQt4.QtGui.QPainter()       
            qp.begin(self)
            paintBg(self, qp, PCal.window_rect, PCal.bg_rgb, PCal.bg_rect, PCal.bg_scaleY, PCal.FHR_rect, PCal.FHR_rgb, PCal.ytext_info)
            if not self.dictChosen:
                drawXScale(self, qp,  PCal.window_rect, PCal.unitXY['FHR'], PCal.all_count,  PCal.xyRatio)
            else:
                #draw_current_time = self.dictChosen.draw_current_time
                #print 'start time', time.time()
                try:
                    info = self.dictChosen.data_handler.info
                    self.label_info.setText(u'名字：'+info['name']+u'    年龄：'+ str(info['age'])+u'    孕周：'+str(info['weeks']))
                except KeyError, reason:
                    self.label_info.setText(u'no info')
                Cache = self.dictChosen.data_handler.data
                start_time = self.dictChosen.start_time
                note= self.dictChosen.data_handler.note
#                realtime_monitor(self, qp, PCal.window_rect, Cache, PCal.start_count, PCal.end_count, PCal.bg_scaleY,  PCal.unitXY, PCal.pen) 
                realtime_curves( qp,  PCal.unite_x, PCal.FHR_y, PCal.pen['FHR'])
                realtime_curves( qp, PCal.unite_x, PCal.EHG_y, PCal.pen['EHG'])
                realtime_curves(qp,  PCal.unite_x, PCal.MHR_y, PCal.pen['MHR'])
                realtime_MMov(qp,  PCal.unite_x, PCal.MMov_height, PCal.unitXY['MMov'][0], PCal.bg_scaleY['MMov'][0], PCal.pen['MMov'])
                realtime_SNR( qp,  PCal.unite_x, PCal.SNR_height, PCal.unitXY['SNR'][0], PCal.bg_scaleY['SNR'][0], PCal.pen['SNR'])
                realtime_Event( qp, PCal.unite_x, PCal.Event, PCal.window_rect.height(),  PCal.pen['Event'] )
                drawXScale( qp,  PCal.window_rect, PCal.unitXY['FHR'], PCal.all_count, PCal.start_count, PCal.end_count , PCal.xyRatio, start_time)
                drawNote(PCal.window_rect.height(), qp, PCal.unitXY['FHR'], PCal.all_count,  PCal.start_count,  PCal.end_count, PCal.xyRatio, note)
            paintBorder(self,  qp, PCal.window_rect)
            qp.end() 
    
    def mouseDoubleClickEvent(self, event):
        self.is_max = True
    
    def resize_cal(self, PCal,  dictChosen):
        self.dictChosen = dictChosen
        self.PCal = PCal
        try:
            Cache = self.dictChosen.data_handler.data
        except Exception, reason:
            print 'no cache'
        else:
            self.PCal.resize_cal(Cache)
    
    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
    
    def showContextMenu(self, pos):
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu = QtGui.QMenu(self)
        self.action_addnote = self.contextMenu.addAction(u'添加注释')
        self.action_addinfo = self.contextMenu.addAction(u'添加信息')
        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.action_addnote.triggered.connect(self.add_note)
        self.action_addinfo.triggered.connect(self.add_info)
        
        self.cursor_pos = pos
        self.contextMenu.move(self.pos() +self.cursor_pos)
        self.contextMenu.show()
    
    def add_note(self):
        '''
        菜单中的具体action调用的函数
        '''
        note =  self.dictChosen.data_handler.note
        count = xy2count(self,  self.cursor_pos.x(), self.PCal.start_count, self.PCal.unitXY['FHR'])
        note_y = self.cursor_pos.y()      
        DlgFillNote = FillNote()
        note_text = DlgFillNote.fill_note()
        note_y  = float(note_y)/self.height()
        note.append([count, note_y, note_text])
    
    def add_info(self):
        DlgFillPatient = FillPatient()
        if self.dictChosen:
            self.dictChosen.patient = DlgFillPatient.fill_in_information(self.dictChosen.patient)
            if self.dictChosen.patient:
                self.dictChosen.data_handler.syn_info(self.dictChosen.patient,self.dictChosen.uuid)
                self.update_patient_info(self.dictChosen.data_handler.info)   
        
    def update_patient_info(self, info):
        self.label_info.setText(u'名字：'+info['name']+u'    年龄：'+ str(info['age'])+u'    孕周：'+str(info['weeks']))
        self.update()

            
    def resizeEvent(self, event):
        self.label_info.setGeometry(QtCore.QRect(self.width()-200, 10, 200, 20))
    
    def listen_RunChk(self, dictChosen):
        if dictChosen:
            if self.dictChosen.data_handler.run_chk == [0, 0, 0, 0, 0]:
                self.label_RunChk.setText(u'run_chk:ok')
            else:
                self.label_RunChk.setText(u'pin off')
    def listen_LowBat(self, dictChosen):
        if dictChosen:
            if self.dictChosen.data_handler.low_battry == [False]:
                self.label_LowBat.setText(u'low_battry:false')
            else:
                self.label_LowBat.setText(u'low_battry:true')
    
    
    
