# -*- coding:utf-8 -*-
# @Time : 2021/4/8 22:06
from calculator import Calculator
import pytest
import yaml

class TestCalculator:
    # 获取yaml中的数据
    params = yaml.load(open("add.yaml",encoding="utf-8"),Loader=yaml.FullLoader)

    def setup_class(self):
        self.cal = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',params["add"],
                              ids=params['ids'])
    def test_add(self,a,b,expect):
        assert expect == self.cal.add(a,b)


    @pytest.mark.parametrize('a,b,expect',[
        [1,1,1],[2.0,3,0.67],[3,-3,-1],[4,0,"除数不能为零"],[0,20,0]
    ],ids=["正整数相除","相除保留两位小数","正整数除以负整数","除数为0","被除数为0"])
    def test_divide(self,a,b,expect):
        assert expect == self.cal.divide(a,b)
