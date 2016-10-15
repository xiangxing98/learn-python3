#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* @Author: Stone_Hou
* Created Date: 2016-10-15 21:59:34
* Version History: 1.0
* runfile('E:/Github/learn-python3/samples/basic/the_dict.py', wdir='E:/Github/learn-python3/samples/basic')
"""
# @author: Administrator

#使用通用工具类来调用一类对象的方法
# 父类
class Animal(object):
    def run(self):
        print('Animal is running...')


# 子类Dog直接从Animal继承
class Dog(Animal):
    def run(self):
        print('Dog is running...')


# 子类Cat直接从Animal继承
class Cat(Animal):
    def run(self):
        print('Cat is running...')


animal = Animal()
animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(animal, object))
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
print(isinstance(dog, Dog))
print(isinstance(cat, Cat))
print(isinstance(animal, Dog))
print(isinstance(animal, Cat))


# 通用工具类
class Runner(object):
    def __init__(self, animal):
        self.__animal = animal

    def run(self):
        self.__animal.run()

runner = Runner(Animal())
runner.run()
runner = Runner(Dog())
runner.run()
runner = Runner(Cat())
runner.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

runner = Runner(Tortoise())
runner.run()

'''
Animal is running...
Dog is running...
Cat is running...
True
True
True
True
True
False
False
Animal is running...
Dog is running...
Cat is running...
Tortoise is running slowly...
'''