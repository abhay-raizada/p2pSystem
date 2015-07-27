import socket
from threading import Thread
import json

class Recieve(Thread):
	def __init__(self,clientSocket=None,isServer=False,ServerList=[]):
		self.isServer=isServer
		self.CSOCK=clientSocket
		self.ServerList=ServerList
		self.running=True
		Thread.__init__(self)

	def is_json(self,myjson):
		try:
			json_object = json.loads(myjson)
		except ValueError, e:
			return False
		return True

	def recieve(self):
		temp = self.CSOCK.recv(1024)
		message=[]
		if self.is_json(temp):
			message.append(json.loads(temp))   #json decoded
			return message
		else:
			return []

	def displayMessage(self,message):
		for i in message:
			print ">>"+ i['m'] + "\n"

	def RecvServer(self):
		message=[]
		for i in self.ServerList:
			temp = i.recv(1024)
			if(temp):
				message.append(json.loads(temp))  #json decoded
		return message

	def run(self):
		while(self.running):
			if not self.isServer:
				message = self.recieve()
			else :
				#print "Server Gets Message"
				message = self.RecvServer()
			if(message !="quit"):

				self.displayMessage(message)
			else:
				self.running=False