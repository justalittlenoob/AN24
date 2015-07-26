import socket

HOST = '192.168.155.3'
PORT = 1
PATH = 'D:/WorkSpace/Github/AN24_9/history'
FILE_INFO = 'D:/WorkSpace/Github/AN24_9/history/%s.info'
FILE_DATA = 'D:/WorkSpace/Github/AN24_9/history/%s.data'
WEB_STAT = 0

class client_p():
    def __init__(self):
        self._sock = self.conn_server()
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
        self._sock.send('SYN')
        buf = self._sock.recv(1024)
        if buf == 'SYN+ACK':
            WEB_STAT = 1
        else:
            WEB_STAT = 0
#---------------------------------------------##
