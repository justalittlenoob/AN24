#!/user/bin/env python

import socket
import os
import json
import threading
from __init__ import WEB_STAT

HOST = '192.168.155.3'
PORT = 1

PATH = 'D:/WorkSpace/Github/AN24_9/history'
FILE_INFO = 'D:/WorkSpace/Github/AN24_9/history/%s.info'
FILE_DATA = 'D:/WorkSpace/Github/AN24_9/history/%s.data' 

class Handler():
    def __init__(self,_uuid,sock):
        self._uuid = _uuid
        self._sock = self.creat_link()
    
    @property
    def handshake(self):
        self._sock.send('SYN')
        buf = self._sock.recv(1024)
        if buf == 'SYN+ACK':
            return 1
        else:
            return 0

    @property
    def has_history(self):
        if not os.listdir(PATH):
            return 0        #no history
        else:
            return 1        # has history
            
    def handle(self, _uuid, content, tag):
        if 0 == WEB_STAT:
            self.local(_uuid, content, tag)
        else:
            self.roaming(_uuid, content, tag)
#-------------------------------------------
    def creat_link(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print '[Fail] creat link'
        else:
            print '[ok] creat link'
        try:
            s.connect((HOST, PORT))
        except Exception, msg:
            print msg
            print '[Fail] link to server'
        else:
            print '[ok] link to server'
        return s
#------------------------------------------
    def local(self, _uuid, content, tag):  #tag=0:info;tag=1:data
        if 0 == tag:
            self.local_info(_uuid, content)
        else:
            self.local_data(_uuid, content)
#-----------------------------------------
    def roaming(self, _uuid, content, tag):
        self.upload_current(_uuid, content, tag)

        if 1 == self.has_history:    #has histroy
            #new thread
            #self.upload_history(_uuid, tag)
            #self.delete_history(_uuid, tag)
            threading.Thread(target=self.handle_history,
                    args=(_uuid,tag)
                    ).start()
        else:
            pass
    
#-------------------------------------------#
##----------------------------------
    def handle_history(self, _uuid, tag):
        self.upload_history(_uuid, tag)
        self.delete_history(_uuid, tag)
##----------------------------------
    def local_info(self, _uuid, content):#write to json
        with open(FILE_INFO % self._uuid,'a+') as f:
            f.write(json.dumps(content.__dict__, sort_keys=True, indent=4))

    def local_data(self, _uuid, content):
        with open(FILE_DATA % self._uuid,'a+') as f:
            f.writelines('%s\n' % content)
##----------------------------------
    def upload_current(self, _uuid, content, tag):
        if 0 == tag:
            self.upload_current_info(_uuid, content)
        else:
            self.upload_current_data(_uuid, content)

    def upload_history(self, _uuid, tag):
        if 0 == tag:
            self.upload_history_info(_uuid)
        else:
            self.upload_history_data(_uuid)
##----------------------------------
    def delete_history(self,_uuid, tag):
        if 0 == tag:
            self.delete_history_info(_uuid)
        else:
            self.delete_history_data(_uuid)
##---------------------------------##

###---------------------
    def upload_current_info(self, _uuid, content): 
        self._sock.send(str(content.__dict__))

    def upload_current_data(self, _uuid, content):
        self._sock.send(content)
###---------------------
    def upload_history_info(self, _uuid): #parse json file
        with open(FILE_INFO % self._uuid,'r') as f:
            dic = json.loads(f.read())
            self._sock.send(str(dic))

    def upload_history_data(self, _uuid):
        with open(FILE_INFO % self._uuid,'r') as f:
            lines = f.readlines()
            for line in lines:
                self._sock.send(line)

###---------------------
    def delete_history_info(self, _uuid):
        if os.path.exists(FILE_INFO % self._uuid):
            os.remove(FILE_INFO % self._uuid)

    def delete_history_data(self, _uuid):
        if os.path.exists(FILE_DATA % self._uuid):
            os.remove(FILE_DATA % self._uuid)
###-------------------###
