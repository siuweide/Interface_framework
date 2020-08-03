import os
import json
import requests

class OperaCookie(object):

    def __init__(self, cookies_path=None):
        if cookies_path == None:
            base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            self.cookies_path = base_path + '/Config/cookies.json'
        else:
            self.cookies_path = cookies_path

    def write_cookies(self, res):
        cookies = requests.utils.dict_from_cookiejar(res.cookies)
        with open(self.cookies_path, 'w') as f:
            f.write(json.dumps(cookies))

    def read_cookies(self):
        with open(self.cookies_path) as f:
            cookies = f.read()
            try:
                cookies = json.loads(cookies)
            except Exception:
                raise ValueError('cookies is not json type')
            return cookies

if __name__ == '__main__':
    test = OperaCookie()
    print(type(test.read_cookies()))