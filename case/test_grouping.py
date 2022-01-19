import json
from idlelib.multicall import r

import jmespath
import pytest

from api.api_grouping import Grouping


# 第二层的拆分 业务层
class TestGrouping:
    def setup_class(self):
        self.group = Grouping()

    # 第四层拆分 剥离数据, 进行参数化
    @pytest.mark.smoke
    @pytest.mark.parametrize("a, check", [(1, 200), (2, 200)], ids=["ONE", "WTO"])
    def test_get_list(self, a, check):
        """
        测试点:
        :return:
        :param a:
        :param check:
        :return:
        """
        self.group.test_grouping(a)
        # assert r.status_code == check
        # assert jmespath.search()

    def test_create_group(self):
        self.group.create_group()

    @pytest.mark.parametrize("a", [
        '000001', '000002', '000004'
    ], ids=["平安银行", "万科A", "国华网安"])
    def test_add_comany(self, a):
        self.group.add_comany(a)

    def test_del_comany(self):
        self.group.delete_group()











    # @pytest.mark.smoke
    # def all_group(self):
    #     self.group.create_group()
    #     r = self.group.test_grouping()
    #     id = jmespath.search()
    #     self.group.add_comany(id)
    #     self.group.delete_group(id)
