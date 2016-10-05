#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：
#
## -*- coding: utf-8 -*-
#
#height = 1.75
#weight = 80.5

name = input('Input your Name: ')
weight = float(input('Input your weight(in kilograms): '))
height = float(input('Input your height(in meters): '))
BMI = weight/math.pow(height, 2)

if BMI < 18.5:
    print("BMI is",BMI,'and you are too light, need eat more')
elif BMI >= 18.5 and BMI <25:
    print("BMI is",BMI,'and you are Nomral, Just keep that good fit')
elif BMI >= 25 and BMI <28:
    print("BMI is",BMI,'and you are Too heavy, you need a little down') 
elif BMI >= 28 and BMI <32:
    print("BMI is",BMI,'and you are Obesity,take action ASAP.')     
else:
    print("BMI is",BMI,'and you are Severe Obesity')
