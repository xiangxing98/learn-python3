#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# cannot modify tuple:
classmates[0] = 'Adam'
#TypeError: 'tuple' object does not support item assignment

t = (1)
print(t) 
# 1 ，输出的是一个整数1 而不是元组，因为()既可以表示tuple，又可以作为括号表示运算时的优先级，结果 (1) 被Python解释器计算出结果 1，导致我们得到的不是tuple，而是整数 1

t=(1,) 
print(t) 
#(1,) 正是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“,”，这样就避免了歧义.

#tuple是不可改变，但tuple里面的list是可改变的
#list通过索引返回对应元素；
