import os
import json
import requests

base_path = os.path.abspath(os.path.dirname(__file__))
cookies_path = base_path + '/Config/cookies.json'
print(cookies_path)
url = 'http://127.0.0.1:8000/accounts/login/'
data = {"username":"siuweide", "password":"123456"}
url1 = 'http://127.0.0.1:8000/api/get_event_list/'

res = requests.post(url, data)
cookies = requests.utils.dict_from_cookiejar(res.cookies)
with open(cookies_path, 'w') as f:
    f.write(json.dumps(cookies))

res1 = requests.get(url1, cookies=cookies)
print(res1.text)