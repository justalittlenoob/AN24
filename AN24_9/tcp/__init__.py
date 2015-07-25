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
    def conn_server(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print '[Fail] creat socket(to server)'
        else:
            print '[ok] creat socket(to server)'
        try:
            s.connect((HOST, PORT))
        except Exception, msg:
            print msg
            print '[Fail] connect to server'
        else:
            print '[ok] connect to server'
            global WEB_STAT
            WEB_STAT = 1
        return s

    def online():
        pass

