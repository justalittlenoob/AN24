#!/user/bin/env python

import socket
import os
from __init__ import WEB_STAT, client_p

HOST = '192.168.155.3'
PATH = 'D:/WorkSpace/Github/AN24_9/history'
FILE_INFO = 'D:/WorkSpace/Github/AN24_9/history/%s.info'
FILE_DATA = 'D:/WorkSpace/Github/AN24_9/history/%s.data' 

class handle():
    def __init__(self,_uuid,sock):
        self.has_history = self.check_local()
        self._uuid = _uuid

#-------------------------------------------
    def check_local(self):
        if not os.listdir(PATH):
            self.has_history = 0        #no history
        else:
            self.has_history = 1        # has history
        return self.has_history    
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
            self.upload_history(_uuid, tag)
            self.delete_history(_uuid, tag)
        else:
            pass

#-------------------------------------------#

##----------------------------------
    def local_info(self, _uuid, content):#write to json
        with open(FILE_INFO % self._uuid,'a+') as f:
            f.write(str(content.__dict__))
    def local_data(self, _uuid, content):
        with open(FILE_DATA % self._uuid,'a+') as f:
            f.write(content)
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
        pass
    def upload_current_data(self, _uuid, content):
        pass
###---------------------
    def upload_history_info(self, _uuid): #parse json file
        pass
    def upload_history_data(self, _uuid):
        pass
###---------------------
    def delete_history_info(self, _uuid):
        if os.path.exists(FILE_INFO % self._uuid):
            os.remove(FILE_INFO % self._uuid)
    def delete_history_data(self, _uuid):
        if os.path.exists(FILE_DATA % self._uuid):
            os.remove(FILE_DATA % self._uuid)
###-------------------###
