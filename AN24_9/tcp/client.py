#!/user/bin/env python

import socket
import os
HOST = '192.168.155.3'
PATH = 'D:/WorkSpace/Github/AN24_9/history'
FILE_INFO = 'D:/WorkSpace/Github/AN24_9/history/%s.info'
FILE_DATA = 'D:/WorkSpace/Github/AN24_9/history/%s.data' 
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


class toServer():
    
    def __init__(self):
        '''sock1:info sock2:data'''
        self._uuid = ''
        self.web_stat = 0  # 1:True  0:False
        self._sock1, self._sock2 = self.conn_server()
        
    
    def conn_server(self):#ok
        port1, port2 = 1, 2  
        try:
            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print '[Fail] creat socket(to server)'
        else:
            print '[ok] creat socket(to server)'
        try:
            s1.connect((HOST,port1))
            s2.connect((HOST,port2))
        except Exception, msg:
            print '[Fail] connect to server'
            print msg
        else:
            print '[ok] connect to server'
            self.web_stat = 1 
        return (s1, s2)

    def handle_info(self, patient_info):
        if self.web_stat ==1:
            self.upload_patient(patient_info)
        else:
            self.patient_to_local(patient_info)

    def handle_data(self, data):
        if self.web_stat ==1:
            self.upload_data(data)
        else:
            self.data_to_local(data)

    ''' web_stat = 0 (Fail)'''
    def _patient_to_local(self, patient_info):
        '''patient_info is a class'''
        with open(FILE_INFO % self._uuid,'a+') as f:
            f.write(str(patient_info.__dict__))

    def _data_to_local(self,data):
        with open(FILE_DATA % self._uuid,'a+') as f:
            f.write(data)

    ''' web_stat = 1 (ok)'''
    def check_local(self):#ok
        if not os.listdir(PATH):
            self.has_history = 0   # empty florder,no history
        else:
            self.has_history = 1
        return self.has_history
    
    def upload_histroy(self):
        if self.has_history:
            for parent, dirname, filenames in os.walk(PATH):
                file_info = [info[:-5] for info in filenames if info[-4:]=='info'] 
                file_data = [data[:-5] for data in filenames if data[-4:]=='data']
        for file in file_info:
            with open(FILE_INFO % file, 'w+') as f:
                buf1 = f.read()
                self._sock1.send(buf1)
        for file in file_data:
            with open(FILE_DATA % file, 'w+') as f:
                buf2 = f.read()
                self._sock2.send(buf2)

    def del_histroy(self):
        if os.path.exists(FILE_INFO % self._uuid):
            os.remove(FILE_INFO % self._uuid)
        if os.path.exists(FILE_DATA % self._uuid):
            os.remove(FILE_DATA % self._uuid)    
    '''port = 1'''
    def upload_patient(self,patient_info):
        self._sock1.send(str(patient_info.__dict__)) 
    def online(self):
        pass
    '''port = 2 '''
    def upload_data(self, data):
        self._sock2.send(data)
    def close_port1(self):
        self._sock1.close()
    def close_port2(self):
        self._sock2.close()


if __name__ == '__main__':
    pass

'''
def upload_patient(patient):

    port = 2
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print '[Fail] creat socket[2]' 
    print '[ok] creat socket[2]'

    s.connect((HOST, port))
    print '[ok] connected to ' + HOST + str(port) 

    print 'message:', str(patient.__dict__),type(str(patient.__dict__))

    s.send(str(patient.__dict__))
    s.close()

def upload_data(data):
    port = 8888
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print '[Fail] creat socket[1]'
    print '[ok] creat socket[1]'
    s.connect((HOST,port))
    print '[ok] connected to ' + HOST + str(port)
    s.send(data)
    print '[ok] send data'
    s.close()
import time
def upload(patient=None,data=''):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print '[Fail] creat socket[2]' 
    print '[ok] creat socket[2]'

    s.connect((HOST, 2)) 
    if None != patient:
        print 'message:', str(patient.__dict__),type(str(patient.__dict__))
        s.send('P'+str(patient.__dict__))
        if '' != data:
            time.sleep(1)
            s.send('D'+data)
        else:
            pass
        s.close()
    else:
        if '' == data:
            pass
        else:
            s.send('D'+data)
        s.close()
'''
        
    
