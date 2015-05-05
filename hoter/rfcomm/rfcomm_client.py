#!/usr/b in/env pytho n
#-*- coding: UTF-8 -*-
''' 
AN24    00:80:98:0E:39:77
pc      00:22:68:E2:18:6F
desktop 00:1f:81:00:08:30
 '''

import bluetooth
from bluetooth import *
import sys
from __builtin__ import reload
import types
reload(sys)
#sys.setdefaultencoding('utf-8')
print '[ok] set default coding:', sys.getdefaultencoding()
#apply to connect

bd_addr = "00:80:98:0E:39:77"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print '[OK] connecting '
sock.send("\x10\x02G\x10\x03\x42\xbc")
print '[OK] sending connection request '
print 'waiting reply...'
'''
#waiting receive
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#port2 = 2
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address
'''
print '[ok] ready to accept data '

import chardet

def formatData(data):
    str_Ret = data.replace('\x10','<DLE>')
    str_Ret = str_Ret.replace('\x02','<STX>')
    str_Ret = str_Ret.replace('\x03','<ETX>')
    str_Ret = str_Ret.replace('\x04','<CRC>')
    #CRC=\x04
    return str_Ret
while 1:
    data = sock.recv(65535)
    print '[ok] query data type', chardet.detect(data)
    #str1 = data.decode("ascii")
    
    print '[ok] [recieved hex data %s ]\n' , data
    #print type(data)
   
   
#client_sock.close()
#server_sock.close()
sock.close()
'''
def not_empty(s):
	return s and s.strip()

filter(not_empty,['1 223  234 sas df  '])
'''
#int() can only convert string of number to int
'''
def int16(x, base = 16):
	return int(x, base)
'''

