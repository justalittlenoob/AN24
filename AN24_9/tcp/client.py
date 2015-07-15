#!/user/bin/env python

import socket
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
        

