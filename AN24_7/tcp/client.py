#!/user/bin/env python

import socket
def upload_data(message='hello from win7 client'):

    host = '192.168.155.2'
    port = 8888
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print '[Fail] creat socket' 
    print '[ok] creat socket'

    s.connect((host, port))
    print '[ok] connected to ' + host 

    #message = 'hello from win7 client'
    ''.join(message)
    print 'message:', message
    s.send(message)
    s.close()

if __name__ == '__main__':
    upload_data()
