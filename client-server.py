import socket
import func
from threading import Thread 

choice=raw_input("Connect to a person or start a server 1|2 :\n")
def sendo(s):
	data = raw_input("\nYou>>")
	while True:
		s.sendall(data)
		data = raw_input("\nYou>>")
		if(data == 'q'):
			s.close()
			exit()
			break
def recvo(s):
	while True:
		data=s.recv(1024)
		if data:
			print host + ">>"+data
		if data == 'q':
			s.close()
			exit()

			break


if choice == '1':
	s=socket.socket()
	host = func.return_ip()
	port = int(raw_input("Enter the port\n"))
	print ("Server IP | Port are %s | %d" %(host,port))
	s.bind((host,port))
	s.listen(1)
	print 'Connecting ...'
	while True:
    	# establish a connection
		clientsocket,addr = s.accept()      
		print("Got a connection from %s" % str(addr))
		try:
			clientsocket.send('Connection Established')
			
			t1 = Thread(target=sendo,args=(clientsocket,))
			t2 = Thread(target=recvo, args =(clientsocket,))
			t1.start()
			t2.start()
    		
		except:
			print "FUCK\n"
			#clientsocket.close()
if choice == '2':
	s= socket.socket()
	host = raw_input("Enter the IP to connect to : ")
	port = int(raw_input("Enter the port: "))
	s.connect((host, port))
	sendCT = Thread(target=sendo,args=(s,))
	recvCT = Thread(target=recvo, args =(s,))
	sendCT.start()
	recvCT.start()
	
	#s.close()