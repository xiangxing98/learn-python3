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

s1 = [
		'python', 
		'java', 
		['asp', 'php'], 
		'scheme'
	]
print("lenth of list s1 is",len(s1))
# 4

p = ['asp', 'php']
s2 = ['python', 'java', p, 'scheme']
print("lenth of list s2 is",len(s2))


L = []
print("L is the empty list, Lenth of L is",len(L))
# 0

#List element Append/insert, delete, modify
listExample =['Adam','Lisa','Bart', 'Stone_Hou']
listExample.append('Siqin') ##add Siqin after the List
print(listExample)
listExample.insert(0,'Paul1') #add Paul before the 1st element
print(listExample)
listExample.insert(-1,'Paul2')#add Paul before the last element
print(listExample)
#del(listExample)

listExample.pop(1)
listExample.pop(0)
print(listExample)

#list modify
listExample[0] = 'Liang_Duan'
print(listExample)

