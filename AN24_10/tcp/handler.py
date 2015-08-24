#!/user/bin/env python
#-*- coding: UTF-8 -*-
# coding=utf-8
import select
import socket
import os
import json
import __init__
from __init__ import  HOST, PORT, client_p
import ConfigParser

WEB_STAT = __init__.WEB_STAT
config = ConfigParser.ConfigParser()
config.read('D:/WorkSpace/Github/AN24_10/tcp/conf/conf.ini')
PATH = config.get('History Files', 'PATH')
FILE_INFO = config.get('History Files', 'FILE_INFO')
FILE_DATA = config.get('History Files', 'FILE_DATA') 
FILE_NOTE = config.get('History Files', 'FILE_NOTE')

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
        '''
        if not os.listdir(PATH):
            return 0        #no history
        else:
            return 1        # has history
        '''
        return os.listdir(PATH) and 1 or 0    

    def handle(self, content, tag): #tag=0:info;tag=1:data;tag=2:note
        if 0 == WEB_STAT:
           self.local(content, tag) 
        else:
            rs, ws, es = select.select([self._sock,], [self._sock], [], 5)
            if self._sock in rs:
                buf = self._sock.recv(1024)
                if buf[40:44] == 'SYNI':
                    self.syni == eval(buf[44:]) #if not null,read it then make it null,if null pass
                    print 'self.syni(SYNI):', self.syni
            if self._sock in ws:
                self.roaming(content, tag)

                

#-------------------------------------------
    def creat_link(self):
        global WEB_STAT
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
            s.setblocking(0)
        except Exception, msg:
            print msg
            
            WEB_STAT = 0
            print '[Fail] link to server'
        else:
            WEB_STAT = 1
            print '[ok] link to server'
        return s
#------------------------------------------
    def local(self, content, tag):  #tag=0:info;tag=1:data;tag=2:note
        
        if 0 == tag:
            self.local_info(content)
        elif 1 == tag:
            self.local_data(content)
        else:
            self.local_note(content)
        #self.local_data(content) if tag else self.local_info(content)
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
    def local_info(self, content):#write to json, content is a instance
        self.syni = content.__dict__
        print 'self.syni(Local):', self.syni
        with open(FILE_INFO % self._uuid,'w+') as f:
            f.write(json.dumps(content.__dict__, sort_keys=True, indent=4))
            #f.write(json.dumps(content, sort_keys=True, indent=4))

    def local_data(self, content):
        with open(FILE_DATA % self._uuid,'a+') as f:
            f.writelines('%s\n' % content)

    def local_note(self, content): #content is a list
        with open(FILE_NOTE % self._uuid,'a+') as f:
            f.writelines('%s\n' % str(content))
##----------------------------------

    def upload_current(self, content, tag):
        
        if 0 == tag:
            self.upload_current_info(content)
        elif 1 == tag:
            self.upload_current_data(content)
        else:
            self.upload_current_note(content)
        
        #self.upload_current_data(content) if tag else \
        #        self.upload_current_data(content)

##----------------------------------

    def delete_history(self,filename, tag):
        
        if 0 == tag:
            self.delete_history_info(filename)
        elif 1 == tag:
            self.delete_history_data(filename)
        else:
            self.delete_history_note(filename)
        #self.delete_history_data(filename) if tag else \
        #       self.delete_history_info(filename)

##---------------------------------##

###---------------------
    def upload_current_info(self, content): 
        self.syni = content.__dict__
        print 'self.syni(Current):', self.syni
        self._sock.send('CINFO'+str(content.__dict__)+'\n'+'\r\n')
        #self._sock.send('CINFO'+str(content)+'\n'+'\r\n')

    def upload_current_data(self, content):
        self._sock.send('CDATA'+content+'\r\n')

    def upload_current_note(self, content):   #content is list
        self._sock.send('CNOTE' + str(content) + '\r\n')
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

    def upload_history_note(self):
        files = self.traversal()[2]
        for _file in files:
            self._sock.send('HIST_NOTE'+_file + '\r\n')
            with open(FILE_NOTE % _file,'r') as f:
                lines = f.readlines()
                for line in lines:
                    self._sock.send('HNOTE'+line+'\r\n')
            self.delete_history_data(_file)


###---------------------
    def delete_history_info(self, filename):
        if os.path.exists(FILE_INFO % filename):
            os.remove(FILE_INFO % filename)

    def delete_history_data(self, filename):
        if os.path.exists(FILE_DATA % filename):
            os.remove(FILE_DATA % filename)

    def delete_history_note(self, filename):
        if os.path.exists(FILE_DATA % filename):
            os.remove(FILE_DATA % filename)
###-------------------###

####-----------------------------
    def traversal(self):
        for parent, dirname, filenames in os.walk(PATH):
            files_info = [info[:-5] for info in filenames if info[-4:]=='info'] 
            files_data = [data[:-5] for data in filenames if data[-4:]=='data']
            files_note = [data[:-5] for data in filenames if data[-4:]=='info']
        return files_info, files_data, files_note
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
    

