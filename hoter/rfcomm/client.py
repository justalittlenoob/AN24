from bluetooth import *

# Create the client socket
prot = 1
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("00:22:68:E2:18:6F", 1))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
