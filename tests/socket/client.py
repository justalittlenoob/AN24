#!/user/bin/env python

import socket
host = '10.18.19.46'
port = 2
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print '[Fail] creat socket' 
print '[ok] creat socket'

s.connect((host, port))
print '[ok] connected to ' + host 

message = 'hello from win7 client'
s.send(message)
s.close()
