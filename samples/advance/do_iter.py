#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
#
#在Python中，迭代是通过for ... in来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：
#
#for (i=0; i<list.length; i++) {
#    n = list[i];
#}

#python只要是可迭代对象list,tuple,dict，无论有无下标，都可以迭代，比如dict就可以迭代：

#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以使用isinstance()判断一个对象是否是Iterable对象：

#如何判断一个对象是可迭代对象呢？
#方法是通过collections模块的Iterable类型判断：
from collections import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

isinstance([], Iterable)
#list is iterable? True
isinstance({}, Iterable)
#dict is iterable? True
isinstance('abc', Iterable)
#True
isinstance((x for x in range(10)), Iterable)
#True
isinstance(100, Iterable)
#False

#而生成器不但可以作用于for循环，
#还可以被next()函数不断调用并返回下一个值，
#直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

#使用isinstance()判断一个对象是否是Iterator对象：
print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable)) # list is literable True
print('Iterable? \'abc\':', isinstance('abc', Iterable)) # str is iterable True
print('Iterable? 123:', isinstance(123, Iterable)) # integer non iterable False
print('Iterable? g():', isinstance(g(), Iterable)) # function is iterable True

#生成器都是Iterator对象，
#但list、dict、str虽然是Iterable，却不是Iterator,why?
#这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)
#True
isinstance(iter('abc'), Iterator)
#True

#使用isinstance()判断一个对象是否是Iterator对象
print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator)) # Fasle
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator)) # True
print('Iterator? \'abc\':', isinstance('abc', Iterator)) # Fasle
print('Iterator? 123:', isinstance(123, Iterator)) # False
print('Iterator? g():', isinstance(g(), Iterator)) # True

# iter string/character
for ch in 'ABCDEF':
    print(ch)

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#iter dict also is ok
d = {'a': 1, 'b': 2, 'c': 3}

# iter each key, 默认情况下，dict迭代的是key
print('iter key:', d)
for k in d:
    print('key:', k)

for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index: 下标循环,在for循环中同时迭代索引和元素本身
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


life_experience = {'Zhangbaohua': 'no-comment', 'Erjiyuan': 'excited', 'Wallace': 'talaughed-comfortably'}
for people, elder in life_experience.items():
    print('Elder vs', people, 'as a hath we can say', elder)


days = ['Monday','Tuesday','Wednesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','beer']
desserts = ['tiramisu','ice cream','pie','pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ':drink', drink, '- eat', fruit, '- enjoy', dessert)
print('日子嘛，简单就好')

for i, value in enumerate(['A', 'B', 'C'],1):
    print(i, value)
print(enumerate(['A', 'B', 'C'],1))

"""
小结
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
"""
for x in [1, 2, 3, 4, 5]:
    pass
"""
实际上完全等价于：
"""
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环print('aha, Stop Iteration')
        break