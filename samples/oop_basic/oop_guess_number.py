#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* @Author: Stone_Hou
* Created Date: 2016-10-15 20:50:46
* Version History: 1.0
* runfile('E:/Github/learn-python3/samples/basic/the_dict.py', wdir='E:/Github/learn-python3/samples/basic')
"""
# @author: Administrator

from random import randint
import functools

shuiji = [s for s in [randint(1,10) for s in range(1)]]

class Guess:
    num = 1

    def __init__(self,num):
        self.num = num

    def print_guess(self):
        if self.num >= 11 or self.num <= 0:
            print("不得大于11 小于0")
        else:
            print("您猜的数字是：%d" % (self.num))


def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("Welcome to Guess!")
        print("please you random writer one number,but can't exceed 10 and less than 0")
        i = func(*args,**kw)
    return wrapper

@log
def data():
    i = Guess(int(input("请输入：")))
    i.print_guess()
    for x in shuiji:
        print("random is %s" % x)
        if i.num == x:
            print("Guess！！")
        else:
            print("No Guess.")


data()