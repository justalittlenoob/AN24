#!/usr/b in/env pytho n
#-*- coding: UTF-8 -*-


import data
import init_An24
from log import log
   
def scan_bt():
    '''return AN24s dict'''

    AN24_dict = init_An24.scan_bluetooth()
    return AN24_dict

class AN24 (object):
    def __init__(self, bt_addr):
        '''Fail return False(type=bool)
        sucess return sock(type=socket)'''
        self._addr = bt_addr
        _sock = init_An24.conn(bt_addr)
        #self._stream = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self._stream=None
        if _sock != False:
            self.sock = _sock 
        else:
            raise AttributeError('conn fail, check bluetooth device')
        self.cache = []
        self.run_chk = [0, 0, 0, 0, 0]
        
        self.low_battry = [False]
        self.stop = False
        '''
        self.bt_state
        self.web_state
        
        self.id
        '''

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
    def data_recv(self):
        data.start_data_thread(self.sock,self.cache,self.run_chk,self.low_battry,self.stop,self._addr)

    def stop_recv(self):
        self.stop = True

    def _data_recv(self):
        if self._data_recv() != None:
            self.run_chk =self._data_recv() [0]
            self._stream =  self._data_recv() [1]
        print 'self.streams type', type(self._stream)
        return self._stream
        #return data.start_data_thread(self.sock,self.cache,self.run_chk,self.low_battry)

    
                
                 
                
if __name__ == "__main__":
    scan_bt()
    AN24 = AN24("00:80:98:0E:39:77")
    #print 'initchk:', AN24.init_chk
    log("connected?", AN24.sock)
    battry = AN24.battry
    #init_An24.syn_clk(AN24.sock)
    #init_An24.inquire_date(AN24.sock)
    #init_An24.inquire_time(AN24.sock)
    init_check_list = AN24.init_chk
    AN24.data_recv()
    
         

