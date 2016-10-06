#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python提供了切片（Slice）操作符，R语言出现了
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前3个元素['Michael', 'Sarah', 'Tracy']
#Method 1. old and stupid way
print([L[0], L[1], L[2]])
#Method 2. for loop 
r = []
n = 3
for i in range(n):
    r.append(L[i])
r
#Method 3. slice
L[0:3]

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])
print('L[-2:-1] =', L[-2:-1])

R = list(range(100))
print('R[:10] =', R[:10]) #1st 10 numbeers
print('R[-10:] =', R[-10:]) #last 10 numbers
print('R[10:20] =', R[10:20]) #前11-20个数
print('R[:10:2] =', R[:10:2]) #前10个数，每两个取一个
print('R[::5] =', R[::5]) #所有数，每5个取一个
print(R[:]) #什么都不写，只写[:]原样复制一个list

#tuple也是一种list，唯一区别是tuple不可变。
#因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
(0, 1, 2, 3, 4, 5)[:3]
#(0, 1, 2)

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
#因此，字符串也可以用切片操作，只是操作结果仍是字符串：
'ABCDEFG'[:3]
#'ABC'
'ABCDEFG'[::2] #每两个取一个：
#'ACEG'

#在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。
#Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。

