#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#在Python中，这种一边循环一边计算的机制，称为生成器：generator。

#如何判断一个对象是可迭代对象呢？
#方法是通过collections模块的Iterable类型判断：
from collections import Iterable, Iterator

s = (x * x for x in range(5))
print(s)
print('Iterable? s:', isinstance(s, Iterable)) # generator is literable True
for x in s:
    print(x)

#著名的斐波拉契数列（Fibonacci），
#除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#斐波拉契数列用列表生成式写不出来，
#但是，用函数把它打印出来却很容易：
def fib_fun(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b) #是print
        a, b = b, a + b
        n = n + 1
    return 'done'

fib_fun(6) #输出斐波那契数列的前6个数

#定义generator的另一种方法。
#如果一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator：
#上面的函数和generator仅一步之遥。
#要把fib函数变成generator，只需把print(b)改为yield b就可以了：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b #是yield
        a, b = b, a + b
        n = n + 1
    return 'done'

#注意，赋值语句：
#a, b = b, a + b
#相当于：
#t = (b, a + b) # t是一个tuple
#a = t[0] = b
#b = t[1] = a + b
#但不必显式写出临时变量t就可以赋值


f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#要创建一个generator，有很多种方法。
#第一种方法很简单，只要把一个列表生成式的[]改成()，
#就创建了一个generator：

L = [x *x for x in range(10)]
print(L) 
#L is a ist: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

generator_1 = (x *x for x in range(10))
print(generator_1)
#<generator object <genexpr> at 0x0A86DEA0>

#请注意区分普通函数和generator函数，普通函数调用直接返回结果：
r = abs(6)
print(r)
#6
#generator函数的“调用”实际返回一个generator对象：
g = fib(6)
print(g)
#<generator object fib at 0x1022ef948>




#杨辉三角定义如下：
#
#          1
#        1   1
#      1   2   1
#    1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1
#把每一行看做一个list，试写一个generator，不断输出下一行的list：
#
## -*- coding: utf-8 -*-
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

#n = 0
#for t in triangles():
#    print(t)
#    n = n + 1
#    if n == 10:
#        break


def triangel(n):
    L=[1]    #定义一个list[1]
    while True:
        yield L    #打印出该list
        L=[L[x]+L[x+1] for x in range(len(L)-1)]    #计算下一行中间的值（除去两边的1）
        L.insert(0,1)  #在开头插入1
        L.append(1)  #在结尾添加1
        if len(L)>10:  #仅输出10行
            break

a=triangel(10)
for i in a:
    print(i)



