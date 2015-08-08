from socket import *
import retrieveIP
import json
import time
from threading import Thread
def is_json(myjson):
		try:
			json_object = json.loads(myjson)
		except ValueError, e:
			return False
		return True
PORT=5002
host=retrieveIP.return_ip()
s =socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
ip=retrieveIP.return_ip()
data= ip
s.sendto(data, ('<broadcast>', PORT))
#time.sleep(2)
s.close()
s=socket(AF_INET, SOCK_DGRAM)
s.bind(('', PORT))
timeout=5
timout_start=time.time()
while time.time() < timeout_start + timeout:
	m=s.recvfrom(1024)
	s.sendto(data, (m[1][0], PORT))
	#if is_json(m):
	print m[1][0]
