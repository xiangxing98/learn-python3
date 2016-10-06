#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list(range(1, 11)) #List Comprehensions 1 to 10

#生成list [1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#列表生成式
#写列表生成式时，把要生成的元素x * x放到前面，
#后面跟for循环，就可以把list创建出来，十分有用，
#多写几次，很快就可以熟悉这种语法。

L_new = [x * x for x in range(1, 11)]
print(L_new)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x * x for x in range(1, 11)])

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
#[x * x for x in range(1, 11) if x % 2 == 0]
#[4, 16, 36, 64, 100]
print([x * x for x in range(1, 11) if x % 2 == 0])

#还可以使用两层循环，可以生成全排列：
#[m + n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m + n for m in 'ABC' for n in 'XYZ'])

#for循环其实可以同时使用两个甚至多个变量，
#比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
#列表生成式也可以使用两个变量来生成list
print([k + '=' + v for k, v in d.items()])

#最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('E:\Github\learn-python3\samples')] # os.listdir可以列出文件和目录
#['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']

#如果list中既包含字符串，又包含整数，
#由于非字符串类型没有lower()方法，所以列表生成式会报错：
L = ['Hello', 'World', 18, 'Apple', None]
[s.lower() for s in L]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 1, in <listcomp>
#AttributeError: 'int' object has no attribute 'lower'

#modify
[s.lower() for s in L if isinstance(s,str)]
"""
for x in L:
    if isinstance(x,str):
        print(x.lower())
    else:
        continue
"""

#使用内建的isinstance函数可以判断一个变量是不是字符串：
x = 'abc'
y = 123
isinstance(x, str)
#True
isinstance(y, str)
#False


