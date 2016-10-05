#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* @Author: Stone_Hou
* Created Date: Wed Oct  5 17:47:43 2016
* Version History: 1.0
* 
"""
# @author: Administrator

# Python笔记——数字及数学函数
# 一、python中的数字
# 1、  类型及运算符
# Python中有四种类型的数
# Ø  整数：一般意义上的数，包含八进制(0开头)，十六进制(0x开头)    eg.  2
# Ø  长整数：无限大小的数，结尾添加l或L                        eg.   2012121200
# Ø  浮点数：小数或用e/E表示的幂          eg.   3.23      50.2E2
# Ø  复数：复数的虚部以字母J 或 j结尾     eg.    2+3i
# 运算符
# +加法
# -减法
# *乘法
# **幂次
# /除法
# //取整，商的整数部分
# %取余
# &位与
# |位或
# ^位异或
# ~位翻转 x -> -(x+1)
# <<左移
# >>右移
# 运算符优先级，同级从左到右
 
# 2.基本运算及示例
#基本运算开始  
print("3+5 = " + str(3+5)) #不能直接+，转为string  
print("2.0-5 = " + str(2.0-5))  
print("2 * 3 = " + str(2*3))  
print("2 ** 3 = " + str(2**3))  
print("5 / 2 = " + str(5/2))  
print("5 // 2 = " + str(5//2))  
print("5 % 2 = " + str(5%2))  
print("2 >> 2 = " + str(2>>2))  
print("2 << 2 = " + str(2<<2))  
print("2 & 3 = " + str(2&3))# 0010 & 0011 = 0010  
print("2 | 3 = " + str(2|3))  
print("2 ^ 3 = " + str(2^3))  
print("~2 = " + str(~2)) 

# 二、相关数学函数及使用示例
# 使用math模块
import math
# 这句可查看所有函数名列表
print(dir(math))
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

# 查看具体定义及函数原型
help(math)         
 
# 常用的数学函数：
# ceil(x) 取顶
# floor(x) 取底
# fabs(x) 取绝对值
# factorial (x) 阶乘
# hypot(x,y)  sqrt(x*x+y*y)
# pow(x,y) x的y次方
# sqrt(x) 开平方
# log(x)
# log10(x)
# trunc(x)  截断取整数部分
# isnan (x)  判断是否NaN(not a number)
# degree (x) 弧度转角度
# radians(x) 角度转弧度
 
 
# 另外该模块定义了两个常量:
#   DATA
#     e = 2.718281828459045
#     pi = 3.141592653589793

print("-----------math functions-------------")  
#数学函数  
#取顶  
print(math.ceil(2.3))  
#取底  
print(math.floor(2.3))  
#取绝对值  
print(math.fabs(-1))  
#阶乘  
print(math.factorial(3))  
#求直角三角形斜边长  
print(math.hypot(3,4))  
#求x的y次方  
print(math.pow(2,3))  
#求x的开平方  
print(math.sqrt(4))  
#截断，只取整数部分  
print(math.trunc(2.3))  
#判断是否NaN(not a number)  
print(math.isnan(2.3333))     
