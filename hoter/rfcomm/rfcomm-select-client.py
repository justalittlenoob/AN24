from bluetooth import *
from select import *

sock = BluetoothSocket(RFCOMM)
sock_read = BluetoothSocket(RFCOMM)
#sock.setblocking(False)

#try: 
sock.connect(("00:80:98:0E:39:77",1))
sock.send("?I")
#except: pass

while 1:
	print 'waiting for connection'
	readable, writable, excepts = select([sock], [sock], [], 3)
	if sock in readable:
		while 1:
			
			data = sock.recv(65535)
			print '[ok] [recieved hex data %s ]\n' , data
		sock.close()
		break

