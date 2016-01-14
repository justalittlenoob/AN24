from PaintRealTime import *
class PaintCalculation():
    def __init__(self):
        self.unite_x = []
        self.FHR_y = []
        self.EHG_y = []
        self.MHR_y = []
        self.MMov_height = []
        self.SNR_height = []
        self.Event = []
    def evment_calculation(self,  window_rect,  xyRatio =1,  screen_ratio = 0.1, FHR_limit = [80, 110,140, 180]):  
        self.window_rect = window_rect
        self.xyRatio = xyRatio
        self.screen_ratio = screen_ratio
        self.FHR_limit = FHR_limit
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
                            
        self.all_count = cal_realCount(self.window_rect, self.xstep, self.xyRatio, 1)
        self.pen ={'FHR': QtGui.QPen(QtGui.QColor(35, 78, 220), 1, QtCore.Qt.SolidLine), 
                        'EHG':QtGui.QPen(QtGui.QColor(0, 0, 0), 1, QtCore.Qt.SolidLine), 
                        'MHR':QtGui.QPen(QtGui.QColor(148, 48, 34), 1, QtCore.Qt.SolidLine), 
                        'MMov':QtGui.QPen(QtGui.QColor(116, 186, 106), 1, QtCore.Qt.SolidLine), 
                        'SNR': QtGui.QPen(QtGui.QColor(144, 159, 248, 100), 1, QtCore.Qt.SolidLine), 
                        'Event':QtGui.QPen(QtGui.QColor(204, 138, 138), 1, QtCore.Qt.SolidLine) 
                        }
        self.realCount = cal_realCount(self.window_rect, self.xstep, self.xyRatio, self.screen_ratio)
        #print self.realCount, 'realCount'
    
    def reatime_cal(self, Cache):
        try:
            self.endcount_pre
        except Exception, reason:
            self.endcount_pre = 0
        self.end_count = len(Cache)
        if self.end_count>self.realCount:
            self.start_count=self.end_count-int(self.realCount)
        else:
            self.start_count = 0
        FHR_baseY = self.bg_scaleY['FHR'][0]    
        EHG_baseY = self.bg_scaleY['EHG'][0]
        MHR_baseY = self.bg_scaleY['MHR'][0]
        
        unitX, FHR_unitY = self.unitXY['FHR'] 
        EHG_unitY = self.unitXY['EHG'][1]
        MHR_unitY = self.unitXY['MHR'][1]
        MMov_unitY = self.unitXY['MMov'][1]
        SNR_unitY = self.unitXY['SNR'][1]
        for cache in Cache[self.endcount_pre : self.end_count]: 
            if cache[0]==0:
                self.FHR_y.append(0)
            else:
                self.FHR_y.append(FHR_baseY-FHR_unitY*(cache[0]-50)) 
            
            if cache[2]==0:
                self.EHG_y.append(0)
            else:
                self.EHG_y.append(EHG_baseY-EHG_unitY*(cache[2]/255.0*100))  
            
            if cache[1]==0:
                self.MHR_y.append(0)
            else:
                self.MHR_y.append(MHR_baseY-MHR_unitY*(cache[1]-40))  
            
            if cache[3]==0:
                self.MMov_height.append(0)
            else:
                self.MMov_height.append(-MMov_unitY*cache[3]+2) 
            
            if cache[4]==0:
                self.SNR_height.append(0)
            else:
                self.SNR_height.append(-SNR_unitY*cache[4]) 
            
            if cache[5]==0:  
                self.Event.append(0)
            else:
                self.Event.append(1)
                
            if self.start_count !=0:
                del self.FHR_y[0] 
                del self.EHG_y[0]
                del self.MHR_y[0]
                del self.MMov_height[0]
                del self.SNR_height[0]
                del self.Event[0]
            
            if self.start_count ==0:
                if len(self.unite_x) ==0:
                    self.unite_x.append(0)
                else:
                    self.unite_x.append(self.unite_x[-1]+unitX)
        self.endcount_pre = self.end_count
        
    def resize_cal(self, Cache):
        self.unite_x = []
        self.FHR_y = []
        self.EHG_y = []
        self.MHR_y = []
        self.MMov_height = []
        self.SNR_height = []
        self.Event = []
        
        self.end_count = len(Cache)
        if self.end_count>self.realCount:
            self.start_count=self.end_count-int(self.realCount)
        else:
            self.start_count = 0
        FHR_baseY = self.bg_scaleY['FHR'][0]    
        EHG_baseY = self.bg_scaleY['EHG'][0]
        MHR_baseY = self.bg_scaleY['MHR'][0]
        
        unitX, FHR_unitY = self.unitXY['FHR'] 
        EHG_unitY = self.unitXY['EHG'][1]
        MHR_unitY = self.unitXY['MHR'][1]
        MMov_unitY = self.unitXY['MMov'][1]
        SNR_unitY = self.unitXY['SNR'][1]
        
        
        for cache in Cache[self.start_count:self.end_count]:
            if cache[0]==0:
                self.FHR_y.append(0)
            else:
                self.FHR_y.append(FHR_baseY-FHR_unitY*(cache[0]-50)) 
            
            if cache[2]==0:
                self.EHG_y.append(0)
            else:
                self.EHG_y.append(EHG_baseY-EHG_unitY*(cache[2]/255.0*100))  
            
            if cache[1]==0:
                self.MHR_y.append(0)
            else:
                self.MHR_y.append(MHR_baseY-MHR_unitY*(cache[1]-40)) 
            
            if cache[3]==0:
                self.MMov_height.append(0)
            else:
                self.MMov_height.append(-MMov_unitY*cache[3]+2) 
            
            if cache[4]==0:
                self.SNR_height.append(0)
            else:
                self.SNR_height.append(-SNR_unitY*cache[4]) 
            
            if cache[5]==0:  
                self.Event.append(0)
            else:
                self.Event.append(1)
            
            if len(self.unite_x) ==0:
                self.unite_x.append(0)
            else:
                self.unite_x.append(self.unite_x[-1]+unitX)
        self.endcount_pre = self.end_count

    
