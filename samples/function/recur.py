#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))
#最多计算到979就不行了
print('fact(10) =', fact(980))
print('fact(10) =', fact(1000))
#RecursionError: maximum recursion depth exceeded in comparison
#使用递归函数需要注意防止栈溢出。
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，
#每当函数返回，栈就会减一层栈帧。
#由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

#计算fact(5)，可以根据函数定义看到递归计算过程如下
#===> fact(5)
#===> 5 * fact(4)
#===> 5 * (4 * fact(3))
#===> 5 * (4 * (3 * fact(2)))
#===> 5 * (4 * (3 * (2 * fact(1))))
#===> 5 * (4 * (3 * (2 * 1)))
#===> 5 * (4 * (3 * 2))
#===> 5 * (4 * 6)
#===> 5 * 24
#===> 120
#递归函数的优点是定义简单，逻辑清晰。
#理论上，所有的递归函数都可以写成循环的方式，
#但循环的逻辑不如递归清晰。

#解决递归调用栈溢出的方法是通过尾递归优化
#尾递归是指，在函数返回的时候，调用自身本身，
#并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，
#使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，
#所以就不是尾递归了。
#要改成尾递归方式，需要多一点代码，
#主要是要把每一步的乘积传入到递归函数中：

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，
#num - 1和num * product在函数调用前就会被计算，不影响函数调用。
#
#fact(5)对应的fact_iter(5, 1)的调用如下：
#===> fact_iter(5, 1)
#===> fact_iter(4, 5)
#===> fact_iter(3, 20)
#===> fact_iter(2, 60)
#===> fact_iter(1, 120)
#===> 120

#再试试fact(1000)还是不行呢
#fact(1000)
#RecursionError: maximum recursion depth exceeded in comparison
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
#
#遗憾的是，大多数编程语言没有针对尾递归做优化，
#Python解释器也没有做优化，
#所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。


#请编写move(n, a, b, c)函数，A、B、C为三个柱子
#汉诺塔就是利用用中间的柱子把最左边的柱子上的圆盘依次从大到小叠上去，说白了就是c要跟原来的a一样 
#它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
#然后打印出把所有盘子从A借助B(buffer)移动到C的方法
# 利用递归函数移动汉诺塔:
def move(n, a, buffer, c):
    if n == 1:
        print('Move one Plate From', a, 'to -->', c)
        return
    move(n-1, a, c, buffer)
    print('Move one Plate From', a, 'to -->', c)
    move(n-1, buffer, a, c)

move(4, 'A', 'B', 'C')
move(3, 'A', 'B', 'C')
