import json
import requests

class BaseRequest(object):

    def get_method(self, url, headers, cookies, data):
        res = requests.get(url=url, headers=headers, cookies=cookies, params=data)
        return res

    def post_method(self, url, headers, cookies, data):
        res = requests.post(url=url, headers=headers, cookies=cookies, data=data)
        return res

    def run_method(self, method, url, headers=None, cookies=None, data=None):
        res = None
        if method == 'get':
            res = self.get_method(url=url, headers=headers, cookies=cookies, data=data)
        elif method == 'post':
            res = self.post_method(url=url, headers=headers, cookies=cookies, data=data)
        return res

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/accounts/login/'
    url1 = 'http://www.baidu.com'
    data = {"username":"siuweide", "password":"123456"}
    test = BaseRequest()
    print(test.run_method('post', url, data=data))

