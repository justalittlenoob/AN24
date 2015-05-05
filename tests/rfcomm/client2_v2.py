''' 
AN24    00:80:98:0E:39:77
pc      00:22:68:E2:18:6F
desktop 00:1f:81:00:08:30
 '''

from bluetooth import *
import sys

if sys.version < '3':
    input = raw_input
sys.argv.append('00:80:98:0E:39:77')
addr = None

if len(sys.argv) < 2:
    print("no device specified.  ")
    print("Searching all nearby bluetooth devices ...")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on %s" % addr)

# search for the SampleServer service
uuid = "22222222"
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
    print("couldn't find   service ")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

#print("connected.  type anything to send")
while 1:
    data = sock.recv(65535)
    print "received [%s]" % data
    if data == '': break
sock.close()
