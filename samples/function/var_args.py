#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')


def power2(x):
    return x * x

#Test power2
print(power2(5))
print(power2(15))

#要计算x4、x5……怎么办？我们不可能定义无限多个函数。
#你也许想到了，可以把power(x)修改为power(x, n)，x^n
#把第二个参数n的默认值设定为2
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    
#Test power
print(power(5,2))
print(power(5,3))
print(power(5,103))

power(2)
#TypeError: power() missing 1 required positional argument: 'n'
#Python的错误信息很明确：调用函数power()缺少了一个位置参数n。
#这个时候，默认参数就排上用场了。
#由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Stone', 'F')


#默认参数必须指向不变对象example
#先定义一个函数，传入一个list，添加一个END再返回：
def add_end1(L=[]):
    L.append('END')
    return L
    
add_end1([1, 2, 3]) #ok, [1, 2, 3, 'END']
add_end1(['x', 'y', 'z']) # ok, ['x', 'y', 'z', 'END']
add_end1() #ok, ['END']
add_end1() #NOT OK, ['END', 'END']
add_end1() #NOT OK, ['END', 'END', 'END']
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，
#每次调用该函数，如果改变了L的内容，
#则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

#要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
