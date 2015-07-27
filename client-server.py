import socket
import func
from threading import Thread 

choice=raw_input("1.HOST A CHAT\n2.JOIN AN EXISTING CHAT:\n3.HOST A GROUP CHAT\n")
def sendo(s):
	data = raw_input("")
	while True:
		s.sendall(data)
		data = raw_input("")
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
def sendgrp(L):
	data = raw_input("")
	while True:
		for i in L:
			i[0].sendall(data)
		data = raw_input("")
		
def recvgrp(L):
	while True:
		for i in L:
			data=i[0].recv(1024)
			if data:
				for j in L:
					j[0].sendall(data)
				print i[1][0],">>",data
		


if choice == '1':
	s=socket.socket()
	host = func.return_ip()
	raw_input("")
	port = int(raw_input("Enter the port\n"))
	print ("Server IP | Port are %s | %d" %(host,port))
	s.bind((host,port))
	s.listen(1)
	print 'Listening ...'
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
			print "Error\n"
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
	
if choice =='3':
	s=socket.socket()
	L=[]
	host = func.return_ip()
	port = int(raw_input("Enter the port\n"))
	print ("Server IP | Port are %s | %d" %(host,port))
	s.bind((host,port))
	s.listen(5)
	print 'Listening ...'
	while True:
    	# establish a connection
		clientsocket,addr = s.accept()
		if addr not in L:
			L.append([clientsocket,addr]) 
		     
		print("Got a connection from %s" % str(addr))
		try:
			clientsocket.send('Connection Established')
			
			tt1 = Thread(target=sendgrp,args=(L,))
			tt2 = Thread(target=recvgrp, args =(L,))
			tt1.start()
			tt2.start()
    		
		except:
			print "Error\n"
			#clientsocket.close()
	
	#s.close()
