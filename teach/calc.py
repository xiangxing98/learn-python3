#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# just for linux add excute privelige
#$ chmod a+x calc.py

print('Hello, world')

# cd /d E:\Github\learn-python3\teach
# python learning.py
# python calc.py

print(100 + 200 + 300)

print('100 + 200 =', 100 + 200)
print("1024 * 768 =",1024 * 768)

print('The quick brown fox', 'jumps over', 'the lazy dog')

print("Pls input somthing: ")
name = input()
print("You Input name is \"",name, "\"")
print('hello, \"', name, "\"")

#name = input()
#print('hello,', name)

name = input('please enter your name: ')
print('hello,', name)

# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

#escape
print('I\'m ok.')
#I'm ok.

print('I\'m learning\nPython.')
#I'm learning
#Python.

print('\\\n\\')
#\
#\


#multi line code
print('''line1
... line2
... line3''')

False == 0
#True
True == 1
#True

age = 30;
if age >= 18:
    print('adult')
else:
    print('teenager')

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

#// a是整数类型变量
a = 123 
# // 错误：不能把字符串赋给整型变量
a = "ABC"

a = 'ABC'
b = a
a = 'XYZ'
print(b)
#ABC

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)

#code
ord('A')
#65

ord('中')
#20013

chr(66)
#'B'

chr(25991)
#'文'

'\u4e2d\u6587'
#'中文'

'ABC'.encode('ascii')
#b'ABC'
'中文'.encode('utf-8')
#b'\xe4\xb8\xad\xe6\x96\x87'
'中文'.encode('ascii')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

b'ABC'.decode('ascii')
#'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#'中文'