import socket

HOST = '192.168.155.2'
PORT = 11000
PATH = 'D:/WorkSpace/Github/AN24_9/history'
FILE_INFO = 'D:/WorkSpace/Github/AN24_9/history/%s.info'
FILE_DATA = 'D:/WorkSpace/Github/AN24_9/history/%s.data'
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
            print '[ok] buile connection(to server)'
        try:
            s.connect((HOST, PORT))
        except Exception, msg:
            print msg
            print '[Fail] connect to server'
        else:
            print '[ok] connect to server'
        return s
#----------------------------------------------
    def handshake(self):
        global WEB_STAT
        try:

            self._sock.send('SYN\r\n')
            print '[ok] send SYN'
            buf = self._sock.recv(1024)
            print '[ok] recv:', buf
            if buf == 'SYN+ACK=1\r\n':
                WEB_STAT = 1
                self._sock.close()
            else:
                WEB_STAT = 0
        except:
            pass
p = client_p()
p.handshake()
##---------------------------------------------##
if '__main__' == __name__:
    print 'WEB_STAT(init):', WEB_STAT
    p = client_p()
    p.handshake()
    print 'WEB_STAT(handshake):', WEB_STAT
