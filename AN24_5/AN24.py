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
        _sock = init_An24.conn(bt_addr)
        if _sock != False:
            self.sock = _sock 
        else:
            raise AttributeError('conn fail, check bluetooth device')
        self.cache = []
        self.run_chk = [0, 0, 0, 0, 0]
        
        self.low_battry = False
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
        return init_An24.checking(self.sock, 
                self.run_chk) 
         
    
    '''start a thread to recv data'''
    def data_recv(self):
        return data.start_data_thread(self.sock, 
                self.cache, 
                self.run_chk, 
                self.low_battry)

if __name__ == "__main__":
    scan_bt()
    AN24 = AN24("00:80:98:0E:39:77")
    log("connected?", AN24.sock)
    battry = AN24.battry
    init_check_list = AN24.init_chk
    AN24.data_recv()
    
    #if [0, 0, 0, 0, 0] == init_check_list:
         

