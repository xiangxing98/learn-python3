#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

classmates.pop()
print('After POP out one element, classmates =', classmates)

classmates.pop()
print('After POP out 2 element, classmates =', classmates)

classmates.pop()
print('After POP out 3 one element, classmates =', classmates)

List_examp = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(List_examp[0][0])
# 打印Python:
print(List_examp[1][1])
# 打印Lisa:
print(List_examp[2][2])

s = [
		'python', 
		'java', 
		['asp', 'php'], 
		'scheme'
	]
len(s)
# 4

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']

L = []
len(L)
# 0