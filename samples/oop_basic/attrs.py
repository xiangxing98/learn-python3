#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#仅仅dir()把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()
#测试该对象的属性
print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

#如果试图获取不存在的属性，会抛出AttributeError的错误：
#getattr(obj, 'z') # 获取属性'z'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'MyObject' object has no attribute 'z'

#可以传入一个default参数，如果属性不存在，就返回默认值：
print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

#也可以获得对象的方法：
hasattr(obj, 'power') # 有属性'power'吗？
#True

getattr(obj, 'power') # 获取属性'power'
#<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>

fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn # fn指向obj.power
#<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn() # 调用fn()与调用obj.power()是一样的
#81

f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f())

#小结
#
#通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
#
#sum = obj.x + obj.y
#就不要写：
#
#sum = getattr(obj, 'x') + getattr(obj, 'y')
#一个正确的用法的例子如下：
#
#def readImage(fp):
#    if hasattr(fp, 'read'):
#        return readData(fp)
#    return None
#假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
#
#请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

#1.type()可以判断几乎任何类型，但是用来判断类之间的继承关系就很不方便
#
#2.isinstance（）用来判断类的继承关系就很方便了，type（）可以判断的基本数据类型，isinstance也能判断
#
#3.isinstance（）还可以判断一个变量是否是某些类型的一种
#isinstance([1,2,3],(list, tuple))#True
#4.dir（）获得一个对象的所有属性和方法
#
#5.'ABC'.__len__() 等价于 len('ABC')
#
#6.getattr() 如果对象中没有，可以设置返回默认值：getattr(obj,'z',404) #404

#目的是判断哪些名字是方法，用callable()判断
# 查看属性中为方法的代码
#list(filter(lambda x : hasattr(getattr("ABC",x), '__call__') ,dir("ABC")))
#判断某个属性是否方法的最简单办法就是利用callable：
[f for f in dir('abc') if callable(getattr('',f))]


#类及其实例，方法和函数
class a():
    def b():
        return

 #------------------
 #判断类型

 type(a) 
 type(a())
 type(a.b)
 type(a.b())
 type(a().b)

# 返回结果依次是：
# 〈claaa 'type'〉       #表示一个类
# 〈class '__main__.a'〉 #表示类的实例
# 〈class 'function'〉   #表示类的函数
# 〈class 'NoneType'〉 #表示实例返回的值
# 〈class 'method'〉   #表示实例的方法
