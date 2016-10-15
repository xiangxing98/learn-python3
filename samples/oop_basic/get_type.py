#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type()

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

import types

print('type(\'abc\')==str?', type('abc')==str)

#type(123) = <class 'int'>
#type('123') = <class 'str'>
#type(None) = <class 'NoneType'>
#type(abs) = <class 'builtin_function_or_method'>
#type('abc')==str? True

type(123)==type(456)
#True
type(123)==int
#True
type('abc')==type('123')
#True
type('abc')==str
#True
type('abc')==type(123)
#False

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

#import types
def fn():
        pass

type(fn)==types.FunctionType
#True
type(abs)==types.BuiltinFunctionType
#True
type(lambda x: x)==types.LambdaType
#True
type((x for x in range(10)))==types.GeneratorType
#True


#使用isinstance()

#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

#我们回顾上次的例子，如果继承关系是：

#object -> Animal -> Dog -> Husky
#那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')
        
class Husky(Animal):
    def run(self):
        print('Husky is running')
        
a = Animal()
d = Dog()
h = Husky()
#然后，判断：

isinstance(h, Husky)
#True

isinstance(h, Dog)
#True

isinstance(h, Animal)
#True

isinstance(d, Dog) and isinstance(d, Animal)
#True

isinstance(d, Husky)
#False, Not all Dog is Husky

#能用type()判断的基本类型也可以用isinstance()判断：

isinstance('a', str)
#True
isinstance(123, int)
#True
isinstance(b'a', bytes)
#True

#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

isinstance([1, 2, 3], list)
#True
isinstance([1, 2, 3], tuple)
#False
isinstance([1, 2, 3], (list, tuple))
#True
isinstance((1, 2, 3), (list, tuple))
#True


#使用dir()

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir("ABC"))
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
len('ABC')
#3
'ABC'.__len__()
#3

#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
len(dog)
#100

#剩下的都是普通属性或方法，比如lower()返回小写的字符串：
'ABC'.lower()
#'abc'