#!/usr/bin/env python3
# -*- coding: utf-8 -*-

help(abs)
#Help on built-in function abs in module builtins:
#
#abs(x, /)
#    Return the absolute value of the argument.

x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，
# 并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个：

#abs(1, 2)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: abs() takes exactly one argument (2 given)

#如果传入的参数数量是对的，但参数类型不能被函数所接受，
#也会报TypeError的错误，并且给出错误信息：str是错误的参数类型：
#
#abs('a')
#Traceback (most recent call last):
#  File "<ipython-input-59-3b9a69fe3abb>", line 1, in <module>
#    abs('a')
#TypeError: bad operand type for abs(): 'str'

# 数据类型转换

#Python内置的常用函数还包括数据类型转换函数，
#比如int()函数可以把其他数据类型转换为整数：

print(int('123'))
#123
print(int(12.34))
#12
print(float('12.34'))
#12.34
print(str(1.23))
#'1.23'
print(str(100))
#'100'
print(bool(1))
#True
print(bool(''))
#False

#函数名其实就是指向一个函数对象的引用，
#完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

a = abs # 变量a指向abs函数
a(-1) # 所以也可以通过a调用abs函数
#1

stone_ver_abs = abs
print(stone_ver_abs(-3409))
#3409


#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
n2 = 1000
print(hex(n1))
#0xff
print(hex(n2))
#0x3e8

# 调用Python的函数，需要根据函数定义，传入正确的参数。
# 如果函数调用出错，一定要学会看错误信息，所以英文很重要！