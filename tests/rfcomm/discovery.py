import socket
import sys
import bluetooth
print "\n\nperforming inquiry..."

address, services = socket.bt_discover()

print "Address: %s" % address

for name, port in services.items():
     print u"%s : %d" % (name, port)