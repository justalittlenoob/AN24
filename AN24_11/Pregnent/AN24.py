#!/usr/b in/env pytho n
#-*- coding: UTF-8 -*-
# coding=utf-8

import data
import init_An24
from log import log
import uuid   
def scan_bt():
    '''return AN24s dict'''

    AN24_dict = init_An24.scan_bluetooth()
    return AN24_dict
    
class AN24 ():
    def __init__(self, an24):
        bt_addr = an24.items()[0][1]
        self._name = an24.items()[0][0]
        ########################
        self._uuid = str(uuid.uuid1())
        ########################
        '''Fail return False(type=bool)
        sucess return sock(type=socket)'''
        self._addr = bt_addr
        self._count_pos = ['0']   # str
        _sock = init_An24.conn(bt_addr)
        #self._stream = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self._stream=None
        if _sock != False:
            self.sock = _sock 
        else:
            raise AttributeError('conn fail, check bluetooth device')
        
        self.cache = []                #data cache
        self.run_chk = [0, 0, 0, 0, 0]  # checking when running
        self.bt_state = [False]            # bluetooth connection status 
        self.out_of_range = [False]     # whether the person is in range
        self.low_battry = [False]       # the low battry signal
        self.stop = False              # stop recieve data
        
    @property
    #return battry(type=float)
    def battry(self):
        return init_An24.battry(self.sock)
   
    @property
    #return a list
    #sucess:[0,0,0,0,0]
    #fail:some of them is not zero
    def init_chk(self):
        chk = init_An24.checking(self.sock,self.run_chk)
        #self.run_chk = chk
        return  chk
                
                 
    def updata_init_chk(self):
        self.run_chk = [0, 0, 0, 0, 0]    

    '''start a thread to recv data'''
    def data_recv(self,handle):
        data.start_data_thread(self.sock,self.cache,self.run_chk,self.low_battry,self.stop,self._addr,self._count_pos,handle)

    def stop_recv(self,handle):
        data.close_data_thread(self.sock,self.cache,self.run_chk,self.low_battry,self.stop,self._addr,self._count_pos,handle)
        #self._sock.close()
    def _data_recv(self):
        if self._data_recv() != None:
            self.run_chk =self._data_recv() [0]
            self._stream =  self._data_recv() [1]
        print 'self.streams type', type(self._stream)
        return self._stream
        #return data.start_data_thread(self.sock,self.cache,self.run_chk,self.low_battry)

    
class Patient():
    def __init__(self, p='', n='', a=0, w=0, o='', h='', b='', g='' ):
        self.person_num=p
        self.name = n
        self.age = a
        self.weeks = w
        self.outpatient_num = o
        self.hospitalization_num = h
        self.bed_num = b
        self.guardianship_num = g
    

                 
if __name__ == "__main__":
    from tcp.handler import Handler     
    from tcp.__init__ import WEB_STAT
    import time
    #scan_bt()
    AN24 = AN24({'AN24 A001350':'00:80:98:0E:39:77'})
    h = Handler('a88c3ea1-3ffc-11e5-a6fb-1078d2f63bb4', AN24._name)
    #print 'initchk:', AN24.init_chk
    log("connected?", AN24.sock)
    #battry = AN24.battry
    #init_An24.syn_clk(AN24.sock)
    #init_An24.inquire_date(AN24.sock)
    #init_An24.inquire_time(AN24.sock)
    #init_check_list = AN24.init_chk
    p = Patient('lose','zzzzpf','27','1','2','424243adf','9483','1')
    n1 = ['2015:08:08','175',u'这是一个测试']
    n2 = ['2015:09:09','50', '111111']
    print 'sleeping...'
    time.sleep(5)
    print 'begin...'
    h.handle(n1,2)
    h.handle(n2,2)
    h.handle(p,0)
    print 'WEB_STAT:', WEB_STAT
    print 'hashistory:', h.has_history
    AN24.data_recv(h.handle)
    
         

