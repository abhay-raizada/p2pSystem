import subprocess
import re
import platform

#returns ip as string value
def return_ip(): 
	if platform.system() == "Windows":
		p=subprocess.check_output("ipconfig")
		ip = re.search('   IPv4 Address. . . . . . . . . . . : (.+?)\n   Subnet', p)
		return ip.group(1).strip()
	else:	  
		p=subprocess.check_output("ifconfig")
		ip = re.search('inet addr:(.+?)  Bcast', p)
		return ip.group(1)
