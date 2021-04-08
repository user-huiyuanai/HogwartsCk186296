# -*- coding:utf-8 -*-
# @Time : 2021/4/8 22:06
from calculator import Calculator
import pytest

class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',[
        [1,1,2],[1.5,0.5,2.0],[1,0.5,1.5]
    ],ids=["正整数相加","浮点数相加","整数浮点数相加"])
    def test_add(self,a,b,expect):
        assert expect == self.cal.add(a,b)
