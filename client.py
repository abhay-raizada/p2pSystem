import socket
from send import Send
from recieve import Recieve 
class Client():
	def __init__(self,s,host,port):
		s.connect((host,port)) # Connect to the given server host and port
		sendmsg=Send(s)
		recvmsg=Recieve(s)
		sendmsg.start()
		recvmsg.start()
		sendmsg.join()
		recvmsg.join()


    