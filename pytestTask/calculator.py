# -*- coding:utf-8 -*-
# @Time : 2021/4/8 21:38
"""
待测试的类
"""
class Calculator:
    """两个数相加"""
    def add(self,a,b):
        return a+b

    """两个数相除"""
    def divide(self,a,b):
        if b == 0:
            return "除数不能为零"
        return round(a/b,2)