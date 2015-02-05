import subprocess
import re

#returns ip as string value
def return_ip():   
	p=subprocess.check_output("ifconfig")
	ip = re.search('inet addr:(.+?)  Bcast', p)
	return ip.group(1)
