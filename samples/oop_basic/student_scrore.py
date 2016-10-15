#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* @Author: Stone_Hou
* Created Date: 2016-10-15 20:52:25
* Version History: 1.0
* runfile('E:/Github/learn-python3/samples/basic/the_dict.py', wdir='E:/Github/learn-python3/samples/basic')
"""
# @author: Administrator

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('----------\nName: %s, \nScroe: %d, \nLevel: %s\n----------\n' % (self.name,self.score,self.get_grade()))
    def get_grade(self):
        if self.score >= 99:
            return '大神'
        elif self.score >= 90:
            return '优良'
        elif self.score >= 60:
            return '及格'
        else:
            return '差'

n0 = Student('Stone',100)
n1 = Student('xiaoling',95)
n2 = Student('xiaoyang',63)
n3 = Student('vforbox',50)

n0.print_score()
n1.print_score()
n2.print_score()
n3.print_score()