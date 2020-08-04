import os
import json
import requests

base_path = os.path.abspath(os.path.dirname(__file__))
cookies_path = base_path + '/Config/cookies.json'
print(cookies_path)
url = 'http://127.0.0.1:8000/accounts/login/'
data = {"username":"siuweide", "password":"123456"}
url1 = 'http://127.0.0.1:8000/api/add_event/'
data1 = {"eid":1, "name":"测试发布会", "limit":100, "status":"1", "address":"zs", "start_time":"2020-08-03 10:22:30"}
url2 = 'http://127.0.0.1:8000/api/cancel_event/'
data2 = {"event_id":1}
url3 = 'http://127.0.0.1:8000/api/get_event_list/'
res = requests.post(url, data)
cookies = requests.utils.dict_from_cookiejar(res.cookies)
# with open(cookies_path, 'w') as f:
#     f.write(json.dumps(cookies))

res1 = requests.post(url1, data=data1, cookies=cookies)
print(res1.json())