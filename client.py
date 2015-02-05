import socket
import func

s= socket.socket()
host = raw_input("Enter Server's IP")
port = 5000
s.connect((host, port))

while tm != 'q':
	tm = s.recv(1024)
	if tm:
		print tm;
s.close()