#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
#import math语句表示导入math包，
#并允许后续代码引用math包里的sin、cos等函数。

def my_abs(x):
    # 对参数类型做检查，只允许整数和浮点数类型的参数。
    #数据类型检查可以用内置函数isinstance()实现
    if not isinstance(x, (int, float)): 
        # 添加了参数检查后，如果传入错误的参数类型，
        #函数就可以抛出一个错误：
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

n = my_abs(-20)
print(n)

# TypeError: bad operand type:
my_abs('123')
my_abs('A')

#在游戏中经常需要从一个点移动到另一个点，
#给出坐标、位移和角度，就可以计算出新的新的坐标
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#函数可以返回多个值吗？答案是肯定的
r = move(100, 100, 60, math.pi / 6)
print(r)
# 原来返回值是一个tuple！
# 但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，
# 按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，
# 但写起来更方便。
#(151.96152422706632, 70.0)


# 在Python中，定义一个函数要使用def语句，
# 依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。

# 我们以自定义一个求绝对值的my_abs函数为例：

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
my_abs(-980)
my_abs(980)
#my_abs('uye')   # TypeError: unorderable types: str() >= int()   

# 请注意，函数体内部的语句在执行时，一旦执行到return时，
# 函数就执行完毕，并将结果返回。
# 因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

# return None可以简写为return。

# 在Python交互环境中定义函数时，注意Python会出现...的提示。
# 函数定义结束后需要按两次回车重新回到>>>提示符下：

#如果你已经把my_abs()的函数定义保存为abstest.py文件了，
#那么，可以在该文件的当前目录下启动Python解释器，
#用from abstest import my_abs来导入my_abs()函数，
#注意abstest是文件名（不含.py扩展名）：
#from abstest import my_abs

#空函数

#如果想定义一个什么事也不做的空函数，可以用pass语句：
#def nop():
#    pass

#参数检查

#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：

#my_abs(1, 2)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: my_abs() takes 1 positional argument but 2 were given
#但是如果参数类型不对，Python解释器就无法帮我们检查。
#试试my_abs和内置函数abs的差别：

#my_abs('A')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 2, in my_abs
#TypeError: unorderable types: str() >= int()
#abs('A')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: bad operand type for abs(): 'str'


#练习 请定义一个函数quadratic(a, b, c)，接收3个参数，
#返回一元二次方程：ax2 + bx + c = 0#的两个解。
#提示：计算平方根可以调用math.sqrt()函数：
#import math
#math.sqrt(2)
#1.4142135623730951

import math
def quadratic(a, b, c):
    #参数数据类型检查
    if not isinstance(a,(int,float)):
        raise TypeError('%s 数据类型出错, a只限于整数与浮点数'%a)
    if not isinstance(b,(int,float)):
        raise TypeError('%s 数据类型出错, b只限于整数与浮点数'%b)
    if not isinstance(c,(int,float)):
        raise TypeError('%s 数据类型出错, c只限于整数与浮点数'%c)
    Delta=b**2-4*a*c
    x1=(-b+math.sqrt(Delta))/(2*a)
    x2=(-b-math.sqrt(Delta))/(2*a)
    if Delta < 0:
        return print('Delta<0, 此方程无实数解')
    elif Delta == 0:
        return print('Delta==0, 此方程只有一个解,\n x1 = ', x1)
    else:
        return print('Delta>0,此方程有2个解, \n x1 =',x1,', x2 =',x2)
# 测试:
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 2, 1)) # => (-1.0)
print(quadratic(1, -2, 1)) # => (1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
print(quadratic(1, 'a', -4)) 
# => TypeError: <built-in function abs> 数据类型出错, b只限于整数与浮点数
print(quadratic(1, 3.3, -4)) # => (x1 = 0.943 , x2 = -4.243)