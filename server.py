import socket
from threading import Thread
from send import Send
from recieve import Recieve

class Server(Thread):

	def __init__(self,s,host,port):
		s.bind((host,port)) # Bind Host a
		self.connectedIPs=[] # List Contatining all ip's  which have connected 
		self.SOCK=s # Server Socket
		self.running=True
		self.clientSock=[] # List Containing all client sockets connected to server
		#self.SendObj=[] 
		Thread.__init__(self)

	def SendMsg(self):
		#print "Type Message...\n"
		s=Send(None,server=True,serverList=self.clientSock) # Server Send Object initalized
		s.start() # Server Send Started
		s.join()

	def RecvMsg(self):
		r=Recieve(clientSocket=None,ServerList=self.clientSock,isServer=True) 
		r.start()
		r.join()

	def Listen(self):
		self.SOCK.listen(5)
		while self.running :
			clientsocket,addr = self.SOCK.accept()
			print "Got A connection from: " + addr[0] 
			clientsocket.sendall("Connection Established")
			if addr not in self.connectedIPs:
				self.connectedIPs.append(addr)
			if clientsocket not in self.clientSock :
				self.clientSock.append(clientsocket)
				#self.SendObj.append(Send(clientsocket,True,))

	def run(self):
		t1 = Thread(target= self.Listen) # Listening for Connections 
		t2 = Thread(target = self.SendMsg)
		t3 = Thread(target= self.RecvMsg)
		t1.start()
		t2.start()
		t3.start()
		t1.join() 	#join checks if thread has stopped or not, it doesnot let the control flow 
		t2.join()
		t3.join()	
			
