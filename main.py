import socket
from threading import Thread 
import retrieveIP
from client import Client
from server import Server
PORT=5009 #Specifying the port on which this chat client will operate
NAME=raw_input("Enter Your Name\n")
SOCK=socket.socket()
choice=raw_input("1.JOIN AN EXISTING CHAT:\n2.HOST A CHAT\n") 
if(choice=='1'): #User chooses to act as a clitent
	host = raw_input("Enter The IP you wish to connect to\n")
	user = Client(SOCK,host,PORT)# started user as client
if choice=='2' :
	host=retrieveIP.return_ip()
	print "Your IP is: " + host
	user= Server(SOCK,host,PORT)
 	user.start()
	



