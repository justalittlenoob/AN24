#!/user/bin/env python

import socket
import os
import json
import threading
from __init__ import WEB_STAT, HOST, PORT

PATH = 'D:/WorkSpace/Github/AN24_9/history'
FILE_INFO = 'D:/WorkSpace/Github/AN24_9/history/%s.info'
FILE_DATA = 'D:/WorkSpace/Github/AN24_9/history/%s.data' 

class Handler():
    def __init__(self,_uuid):
        self._uuid = _uuid
        self._sock = self.creat_link()
    ''' 
    @property
    def handshake(self):
        try:
            self._sock.send('SYN\r\n')
            buf = self._sock.recv(1024)
        except Exception:
            print '[Fail] Handler handshake'
        else:
            if buf == 'SYN+ACK\r\n':
                return 1
            else:
                return 0
    '''

    @property
    def has_history(self):
        if not os.listdir(PATH):
            return 0        #no history
        else:
            return 1        # has history
            
    def handle(self, content, tag): #tag=0:info;tag=1:data
        self.local(content, tag)
        if 0 == WEB_STAT:
           pass 
        else:
            self.roaming(content, tag)
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
    def local(self, content, tag):  #tag=0:info;tag=1:data
        if 0 == tag:
            self.local_info(content)
        else:
            self.local_data(content)
#-----------------------------------------
    def roaming(self, content, tag):
        self.upload_current(content, tag)
        if 1 == self.has_history:    #has histroy
            #new thread
            #self.upload_history(_uuid, tag)
            #self.delete_history(_uuid, tag)
            threading.Thread(target=self.handle_history,
                    args=(tag,)
                    ).start()
        else:
            pass
    
#-------------------------------------------#
##----------------------------------
    def handle_history(self, tag):
        self.upload_history(tag)
        #self.delete_history(tag)
##----------------------------------
    def local_info(self, content):#write to json
        with open(FILE_INFO % self._uuid,'a+') as f:
            f.write(json.dumps(content.__dict__, sort_keys=True, indent=4))

    def local_data(self, content):
        with open(FILE_DATA % self._uuid,'a+') as f:
            f.writelines('%s\n' % content)
##----------------------------------
    def upload_current(self, content, tag):
        if 0 == tag:
            self.upload_current_info(content)
        else:
            self.upload_current_data(content)

    def upload_history(self, tag):
        if 0 == tag:
            self.upload_history_info()
        else:
            self.upload_history_data()
##----------------------------------
    def delete_history(self,filename, tag):
        if 0 == tag:
            self.delete_history_info(filename)
        else:
            self.delete_history_data(filename)
##---------------------------------##

###---------------------
    def upload_current_info(self, content): 
        self._sock.send(str(content.__dict__)+'\r\n')

    def upload_current_data(self, content):
        self._sock.send(content)
###---------------------
    def upload_history_info(self): #parse json file
        files = self.traversal()[0]
        for _file in files:
            with open(FILE_INFO % _file,'r') as f:
                dic = json.loads(f.read())
                self._sock.send(str(dic)+'\r\n')
            self.delete_history_info(_file)

    def upload_history_data(self):
        files = self.traversal()[1]
        for _file in files:
            with open(FILE_INFO % _file,'r') as f:
                lines = f.readlines()
                for line in lines:
                    self._sock.send(line)
            self.delete_history_data(_file)

###---------------------
    def delete_history_info(self, filename):
        if os.path.exists(FILE_INFO % filename):
            os.remove(FILE_INFO % filename)

    def delete_history_data(self, filename):
        if os.path.exists(FILE_DATA % filename):
            os.remove(FILE_DATA % filename)
###-------------------###

####-----------------------------
    def traversal(self):
        if self.has_history:
            for parent, dirname, filenames in os.walk(PATH):
                files_info = [info[:-5] for info in filenames if info[-4:]=='info'] 
                files_data = [data[:-5] for data in filenames if data[-4:]=='data']
        return files_info, files_data
####-------------------------####    

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

if '__main__' == __name__:
    h = Handler('15e868de-3457-11e5-aa75-1078d2f63bb4')
    p = Patient('S201325016','zpf','27','1','2','424243adf','9483','1')
    #print 'handshake:', h.handshake
    print 'WEB_STAT:', WEB_STAT
    print 'hashistory:', h.has_history
    h.handle(p,0)
    

