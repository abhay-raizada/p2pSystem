import socket
s= socket.socket()
host = '127.0.0.1'
port = 5000
s.connect((host, port))
tm='a' 
while tm != 'q':
	tm = s.recv(1024)
	if tm:
		print tm;
s.close()