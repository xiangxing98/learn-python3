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

#如何判断一个对象是可迭代对象呢？
#方法是通过collections模块的Iterable类型判断：
from collections import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable)) # list is literable True
print('Iterable? \'abc\':', isinstance('abc', Iterable)) # str is iterable True
print('Iterable? 123:', isinstance(123, Iterable)) # integer non iterable False
print('Iterable? g():', isinstance(g(), Iterable)) # function is iterable True

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