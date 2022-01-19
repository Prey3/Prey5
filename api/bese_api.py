import json

import jmespath
import requests
import self as self


class BaseApi:
    def __init__(self):
        self.header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": self.get_token()}

    # 第三层 base 对api做基础支撑 发送请求 获取token
    def send(self, data):
        r = requests.request(**data)
        print(json.dumps(r.json(), indent=1, ensure_ascii=False))
        return r

    def log(self):
        pass

    def get_token(self):
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-user/user/login",
            "headers": {"Content-Type": "application/json;charset=UTF-8"},
            "json": {"name": "lsj1", "password": "123123"}}
        # r = requests.post(
        #     "http://123.56.138.96:3012/api/ainews-user/user/login",
        #     json=data
        # )
        return self.send(data).json().get("access_token")

    def json_parser(self):
        data = {
            "method": 'get',
            "url": 'http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group',
            "headers": {"Content-Type": "application/json;charset=UTF-8", "Authorization": self.get_token()},
            'params': {'page': 1,
                       'per_page': 10,
                       'start_time': '2021-12-28',
                       'end_time': '2022-01-14'}
        }
        return jmespath.search("[?name=='9909'].id", self.send(data).json())

    def compose_data(self):
        pass


if __name__ == '__main__':
    print(BaseApi().get_token())
    print(BaseApi().json_parser())
