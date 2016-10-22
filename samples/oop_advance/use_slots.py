#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    __slots__ = ('name', 'age','set_age') # 用tuple定义允许绑定的属性名称,只允许对Student实例添加name和age属性

class GraduateStudent(Student):
    pass

s = Student() # 创建新的实例
# 绑定属性'name'
s.name = 'Michael' 
print(s.name)
s.age = 25 # 绑定属性'age'

# ERROR: AttributeError: 'Student' object has no attribute 'score',定义不能添加score属性
#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

#尝试给实例绑定一个方法：
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法 'Student' object has no attribute 'set_age'

s.set_age(25) # 调用实例方法
s.age # 测试结果
#25

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
