import socket
from threading import Thread
class Send(Thread):
	def __init__(self,clientSocket=None,server=False,serverList=[]):
		self.Csock=clientSocket # CSock because this would be the socket of client.
		#self.data=''
		self.running=True
		self.server=server # boolean to check wether server has initialized this class
		self.serverList=serverList # This is the servers client List
		Thread.__init__(self)

	def Send(self,msg):
		self.Csock.sendall(msg)
	def SendServer(self,message,serverList):
		for i in serverList:
			i.sendall(message)
	def getData(self):
		
		return raw_input("\n>>")
		
	
	def run(self):
		while(self.running):
			message = self.getData()
			if(message!='quit'):
				if(self.server):
					self.SendServer(message,self.serverList)
				else:
					self.Send(message)
			else:
				self.running=False 


