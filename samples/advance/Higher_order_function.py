#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* @Author: Stone_Hou
* Created Date: 2016-10-07 16:32:30
* Version History: 1.0
* runfile('E:/Github/learn-python3/samples/basic/the_dict.py', wdir='E:/Github/learn-python3/samples/basic')
"""
# @author: Administrator

#Higher_order_function

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
#一个最简单的高阶函数：

#abs = abs()
def add(x, y, f):
    return f(x) + f(y)

"""
当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，根据函数定义，我们可以推导计算过程为：

x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
"""

print(add(-5, 6, abs))
#11

#编写高阶函数，就是让函数的参数能够接收别的函数。
#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

#由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。
#abs是python内定义的函数，如果真的要修改的话也就是需要在调用模块中修改

#可变参数
# 引入数学模块中的方法
from math import sqrt
from math import tan

'''
高阶函数应用，返回一个数字不同方法计算结果,可变参数*kw
'''
def same(num, *kw):
    # 参数检查
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')

    # 初始化结果字典
    rel = {}
    # 循环计算可变参数
    for func in kw:
        try:
            rel[str(func)[str(func).find('function ') + 9: -1]] = func(num)
        except ValueError:
            rel[str(func)[str(func).find('function ') + 9: -1]] = 'None'
    # 返回结果字典
    return rel

# 函数调用
result = same(-10.5, sqrt, abs, tan)
# 结果输出
print(result)
#{'sqrt': 'None', 'tan': -1.8498999934219273, 'abs': 10.5}


#来一个可变参数，要几个函数就来几个
from math import sqrt
from math import tan
from math import sin
from math import cos
def same(x,*fs):
    s=[f(x) for f in fs]
    return s
print(same(2,sqrt,abs,sin,cos))


#来一个可变参数，要几个函数就来几个
from math import sqrt

def do_sth(x=[],*func):
    return [f(x_k) for x_k in x for f in func]

print(do_sth([1,2,4,9],abs,sqrt))
