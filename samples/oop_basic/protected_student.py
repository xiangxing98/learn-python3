#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
#因为在方法中，可以对参数做检查，避免传入无效的参数：
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)

#Note
#1.python中竟然可以这样写：1<=score<=100，这在其他很多语言中都是不允许的，Like java
#
#2.双下划线开头并以双下划线结尾的变量是特殊变量，不是private的，可以直接访问
#
#3.单个下划线开头的变量虽然可以直接访问，但是它隐含了“不要随便访问我”的意思
#
#4.____name虽然是private的变量，但是依然可以在外部以_Student_name的形式访问到
#
#5.bart.__name = 'Chen' 在外部也可以正常执行，但是和想相中的不是一回事，这时候其实是又定义了新的变量__name

#dir(bart)



#一点体会
class Person1(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def func(self):
        print(self.__name)


class Student1(Person1):
    def func1(self):
        print(self.__name)
    pass


bart1 = Student1('bart1',100)
bart1.func1()
dir(bart1)

#返回错误：
#Traceback (most recent call last):
#  File "<pyshell#27>", line 1, in <module>
#    bart.func1()
#  File "C:\Users\Administrator\Desktop\xxd.py", line 14, in func1
#    print(self.__name)
#AttributeError: 'Student' object has no attribute '_Student__name'


#类Student继承了Person，但是一旦在父类中定义了私有变量，这个私有变量比如self.__name只能在这个父类里面调用，即便是子类继承了父类，也不可直接调用，你可以试一下dir(bart)发现没有_Student__name，只有_Person__name。但是如果你在父类中定义的是公共的属性，则在子类，还有在外部可以调用。