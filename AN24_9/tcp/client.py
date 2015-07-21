#!/user/bin/env python

import socket
import os
HOST = '192.168.155.3'
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
        self._sock1, self._sock2 = self.conn_server()
        self.web_stat = 1  # 1:True  0:False

    def conn_server(self):
        port1, port2 = 1, 2
        try:
            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            print '[Fail] creat socket(to server)'
        print '[ok] creat socket(to server)'
        try:
            s1.conn((HOST,port1))
            s2.conn((HOST,port2))
        except:
            print '[Fail] connect to server'
        print '[ok] connect to server'
        self.web_stat = 0
        return (s1, s2)

    ''' web_stat = 0 (Fail)'''
    def patient_to_local(self, patient_info,uuid):
        with open('../history/%s.info' % uuid,'a+') as f:
            f.write(patient_info)

    def data_to_local(self,data,uuid):
        with open('../history/%s.data' % uuid,'a+') as f:
            f.write(data)

    ''' web_stat = 1 (ok)'''
    def check_local(self):
        if not os.listdir('../history/'):
            self.has_history = 0   # empty florder,no history
        else:
            self.has_history = 1
    
    def upload_histroy(self):
        pass
    def del_histroy(self):
        pass
    '''port = 1'''
    def upload_patient(self):
        pass
    def online(self):
        pass
    '''port = 2 '''
    def upload_data(self):
        pass

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

if __name__ == '__main__':
        
        p = Patient('N0000','zpf',1,2,'aaa','bbb','ccc','ddd')
        d = '1111112222222233333333333'
        upload(p)
        while 1:
            upload(None,d)
        

