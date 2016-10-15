#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
#忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排序
print(sorted(students, key=itemgetter(0)))
#按成绩从高到低排序
print(sorted(students, key=lambda t: t[1]))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(students, key=itemgetter(1), reverse=True))


#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
sorted_list = sorted([36, 5, -12, 9, -21], key=abs)
print(sorted_list)
#[5, 9, -12, -21, 36]
#keys排序结果 => [5, 9,  12,  21, 36]
#                |  |    |    |   |
#最终结果     => [5, 9, -12, -21, 36]


#按名字排序,映射函数
def by_name(t):
    return t[0].lower()

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排序
L2 = sorted(L, key=by_name)  # 按小写Ascll码升序对名字排序
L3 = sorted(L, key=by_name, reverse=True)   # 按小写Ascll码升序对名字排序，后反转
print('按名字排序的第一种方式：', L2)
print('按名字排序的第二种方式：', L3)

#按成绩从高到低排序,映射函数
def by_score(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 再按成绩从高到低排序
L2 = sorted(L, key=by_score, reverse=True)
print(L2)
