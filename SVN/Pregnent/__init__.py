#! /usr/bin/env python
#coding=utf-8
import socket
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('conf.ini')
HOST = config.get('Server', 'HOST')
PORT = config.getint('Server', 'PORT')
#PATH = 'D:/WorkSpace/Github/AN24_10/history'
#FILE_INFO = 'D:/WorkSpace/Github/AN24_10/history/%s.info'
#FILE_DATA = 'D:/WorkSpace/Github/AN24_10/history/%s.data'
WEB_STAT = 0

class client_p():
    def __init__(self):
        self._sock = self.build_connection()
#----------------------------------------------
    def build_connection(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print '[Fail] build connection(to server)'
        else:
            print '[ok] creat socket(to server)'
        try:
            s.settimeout(2)
            s.connect((HOST, PORT))
            s.settimeout(None)
        except Exception, msg:
            print msg
            print '[Fail] connect to server'
        else:
            print '[ok] connect to server'
        return s
#----------------------------------------------
    def handshake(self):
        try:

            self._sock.send('SYN\r\n')
            print '[ok] send SYN'
            buf = self._sock.recv(1024)
            print '[ok] recv:', buf
            if buf == 'SYN+ACK=1\r\n':
                global WEB_STAT
                WEB_STAT = 1
                self._sock.close()
            else:
                pass
        except:
            pass
#p = client_p()
#p.handshake()
##---------------------------------------------##
if '__main__' == __name__:
    print 'WEB_STAT(init):', WEB_STAT
    p = client_p()
    p.handshake()
    print 'WEB_STAT(handshake):', WEB_STAT
