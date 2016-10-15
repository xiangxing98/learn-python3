#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 打印1000以内的素数:
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

#先构造一个从3开始的奇数序列,这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
#定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列
#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。


if __name__ == '__main__':
    main()

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
#源码
def is_palindrome(n):
   return str(n) == str(n)[::-1]
# 测试:   
output = filter(is_palindrome, range(1, 1000))
print(list(output))

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
def is_palindrome2(n):
    s = str(n)
    i = int(len(s)/2)
    if s[:-i] == s[:i-1:-1]:
        return int(s)

# 测试:
output = filter(is_palindrome2, range(1, 1000))
print(list(output))

#基本思路：
#输入数字转成字符串str()，然后反转[::-1]，再变成整数int()与原输入数字比较,返回TRUE/False。两者相等则是回数，反之不是。
def is_palindrome3(n):
    return int(str(n)[::-1]) == n 
# 测试:
output = filter(is_palindrome3, range(1, 1000))
print(list(output))





