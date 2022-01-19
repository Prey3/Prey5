import pytest
import requests

# 第一层 api层 封装我们接口 为了我们后期的业务调用
from api.bese_api import BaseApi


class Grouping(BaseApi):
    def test_grouping(self, num):
        """
        点击公司分组页
        :param num:
        :return:
        """
        data = {
            "method": 'get',
            "url": 'http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group',
            "headers": self.header,
            "params": {'page': num,
                       'per_page': 10,
                       'start_time': '2021-12-08',
                       'end_time': '2021-12-22'}
        }
        return self.send(data)

    def create_group(self):
        """
        创建分组
        :param num:
        :return:
        """
        data = {
            "method": 'post',
            "url": 'http://123.56.138.96:3012/api/ainews-user/company-group/create',
            "headers": self.header,
            "json": {"name": 9909}
        }
        return self.send(data)


    def add_comany(self, a):
        """
        添加公司
        :param num:
        :return:
        """
        data = {
            "method": 'post',
            "url": 'http://123.56.138.96:3012/api/ainews-user/company-group/company-create',
            "headers": self.header,
            "json": {"company_code": a, "group_id": self.json_parser()}
        }
        return self.send(data)

    def delete_group(self):
        """
        删除分组
        :param num:
        :return:
        """
        data = {
            "method": 'get',
            "url": 'http://123.56.138.96:3012/api/ainews-user/company-group/delete',
            "headers": self.header,
            "params": {'id': self.json_parser()}
        }
        return self.send(data)


# if __name__ == '__main__':
#     case = Grouping()
#     case.test_grouping(num=1)
#     case.create_group()
