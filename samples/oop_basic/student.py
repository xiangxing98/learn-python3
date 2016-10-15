#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。 init前后各有两个下划线

#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()
lisa.print_score()

print('Grade of bart:', bart.get_grade())
print('Grade of Lisa:', lisa.get_grade())

print('-----\nScore of %s is %s, Grade of %s is %s.' %(bart.name, bart.score, bart.name, bart.get_grade()))
#Score of Bart Simpson is 59, Grade of Bart Simpson is C.
print('-----\nScore of %s is %s, Grade of %s is %s.' %(lisa.name, lisa.score, lisa.name, lisa.get_grade()))
#Grade of Lisa Simpson is B.

print('%s: %s' % (lisa.name, lisa.score))
#Lisa Simpson: 87

lisa.name
lisa.score
lisa.get_grade()


#python的构造方法灵活到只有你想不到的，没有它做不到的。

class Screen(object):

    def __init__(self, **kw):
        self.width = kw.get('width', 2880)
        self.height = kw.get('height', 1800)
        # 你还可以在下面为任何属性设置初默认值

screen1 = Screen()
screen2 = Screen(width=1080)
screen3 = Screen(width=1400, height=900)
screen4 = Screen(height=2100)

screen1
#<__main__.Screen at 0x10dfbb0>
screen2
#<__main__.Screen at 0x10dfe50>
screen3
# <__main__.Screen at 0x10df250>
screen4
#<__main__.Screen at 0x10df310>


#不同学生获取分数等级
class Student2(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def get_level(self):
        if self.score >= 90:
            return (self.name +"'s score is: " + str(self.score) + "," +self.name + "'s level is: "+"A\n")
        elif self.score<90 and self.score>70:
            return  (self.name +"'s score is: " + str(self.score) + "," +self.name + "'s level is: "+"B\n")
        else:
            return (self.name +"'s score is: " + str(self.score) + "," +self.name + "'s level is: "+"C\n")


lisa = Student2('lisa',18,91)
jerry = Student2('jerry',18,85)
tom = Student2('tom',18,45)
print(lisa.get_level())
print(jerry.get_level())
print(tom.get_level())


class Human_BMI(object):
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    def printBMI(self):
        BMI = self.weight / self.height ** 2
        if BMI < 18.5:
            print('体重过低\n')
        elif 24 > BMI >= 18.5:
            print('正常\n')
        elif 28 > BMI >= 24:
            print('超重\n')
        else:
            print('肥胖\n')

GIN = Human_BMI(1.73,56)
GIN.printBMI()

Stone = Human_BMI(1.73,75)
Stone.printBMI()

#一个实操
class Compare(object):
    def __init__(self):
        self.n1=float(input('输入一个数字：'))
        self.n2=float(input('再输入一个数字：'))

    def compa(self):
        if self.n1>self.n2:
            return str(self.n1)+'大于'+str(self.n2)
        elif self.n1==self.n2:
            return str(self.n1)+'等于'+str(self.n2)
        else:
            return str(self.n1)+'小于'+str(self.n2)

x=Compare()
print('第一个数字:''%s' % (x.n1)+'\n''第二个数字：''%s' % (x.n2))
print(x.compa())