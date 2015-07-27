import socket
from threading import Thread
class Recieve(Thread):
	def __init__(self,s):
		self.SOCK=s
		self.running=True
		Thread.__init__(self)
	def recieve(self):
		temp=self.SOCK.recv(1024)
		if temp:
			return temp
		else:
			return 0
	def displayMessage(self,message):
		print ">>"+message+"\n"

	def run(self):
		while(self.running):
			message = self.recieve()
			if(message):
				self.displayMessage(message)
			elif(message=="quit"):
				self.running=False