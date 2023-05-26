import string, random, requests, json

def generateUser(size=2, chars=string.ascii_lowercase + string.digits):
	return 'np' + ''.join(random.choice(chars) for _ in range(size))

for x in range(100):
	user = generateUser()
	try:
		jsonData = json.loads(
			requests.get(f"https://api.github.com/users/{user}").text
			)
		print (jsonData['login'] + ' exist, created at: ' + jsonData['created_at'][:-10])
	except Exception as e:
		print (f'User: {user}, does not exist\n')
		exit()
