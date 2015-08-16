#!/user/bin/env python

import socket
import os
import json
from __init__ import WEB_STAT, HOST, PORT, client_p
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('D:/WorkSpace/Github/AN24_10/tcp/conf/conf.ini')
PATH = config.get('History Files', 'PATH')
FILE_INFO = config.get('History Files', 'FILE_INFO')
FILE_DATA = config.get('History Files', 'FILE_DATA') 

p = client_p()
p.handshake()

class Handler():
    def __init__(self,_uuid,_name):
        self._uuid = _uuid
        self._sock = self.creat_link()
        self.syni = {}
        try:
            self._sock.send('UUID'+_uuid + 'NAME'+ _name + '\r\n')
        except:
            print 'UUID is not send'
            pass
        self.handle_history()

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
        if 0 == WEB_STAT:
           self.local(content, tag) 
        else:
            buf = self._sock.recv(65535)
            if not len(buf):
                self.roaming(content, tag)
            elif buf[40:44] == 'SYNI':
                self.syni ==eval(buf[44:]) #if not null,read it then make it null,if null pass
                self.roaming(content, tag)
            else:
                pass
                

#-------------------------------------------
    def creat_link(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print '[Fail] creat link'
        else:
            print '[ok] creat link'
        try:
            s.settimeout(2)
            s.connect((HOST, PORT))
            s.settimeout(None)
        except Exception, msg:
            print msg
            global WEB_STAT
            WEB_STAT = 0
            print '[Fail] link to server'
        else:
            WEB_STAT = 1
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
        try:
            self.upload_current(content, tag)
        except:
            print 'lost the server, part of data will be in local.'
            self.local(content, tag)
        else:
            pass
        #self.local(content, tag)
        
#-------------------------------------------#
##---------------------------------
    def handle_history(self):
        if WEB_STAT and self.has_history:
            self.upload_history_info()
            self.upload_history_data()
        else:
            pass
##----------------------------------
    def local_info(self, content):#write to json
        with open(FILE_INFO % self._uuid,'w+') as f:
            f.write(json.dumps(content.__dict__, sort_keys=True, indent=4))
            #f.write(json.dumps(content, sort_keys=True, indent=4))

    def local_data(self, content):
        with open(FILE_DATA % self._uuid,'a+') as f:
            f.writelines('%s\n' % content)
##----------------------------------
    def upload_current(self, content, tag):
        if 0 == tag:
            self.upload_current_info(content)
        else:
            self.upload_current_data(content)

##----------------------------------
    def delete_history(self,filename, tag):
        if 0 == tag:
            self.delete_history_info(filename)
        else:
            self.delete_history_data(filename)
##---------------------------------##

###---------------------
    def upload_current_info(self, content): 
        self._sock.send('CINFO'+str(content.__dict__)+'\n'+'\r\n')
        #self._sock.send('CINFO'+str(content)+'\n'+'\r\n')
    def upload_current_data(self, content):
        self._sock.send('CDATA'+content+'\r\n')
###---------------------
    def upload_history_info(self): #parse json file
        files = self.traversal()[0]
        for _file in files:
            with open(FILE_INFO % _file,'r') as f:
                self._sock.send('HIST_INFO'+_file + '\r\n')
                dic = json.loads(f.read())
                self._sock.send('HINFO'+str(dic)+'\r\n')
            self.delete_history_info(_file)

    def upload_history_data(self):
        files = self.traversal()[1]
        for _file in files:
            self._sock.send('HIST_DATA'+_file + '\r\n')
            with open(FILE_DATA % _file,'r') as f:
                lines = f.readlines()
                for line in lines:
                    self._sock.send('HDATA'+line+'\r\n')
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
    h = Handler('20e868de-3457-11e5-aa75-1078d2f63bb4')
    p = Patient('S201325016','zzzzpfnew','27','1','2','424243adf','9483','1')
    data1 = '1002newAAAAAAAAAAAA1003'
    data2 = '1002newBBBBBBBB1003'
    data3 = '1002newCCCCCCCCCCCCCCCCCCC1003'
    #print 'handshake:', h.handshake
    print 'WEB_STAT:', WEB_STAT
    print 'hashistory:', h.has_history
    h.handle(data1,1)
    h.handle(data2,1)
    h.handle(data3,1)
    h.handle(p,0)
    

