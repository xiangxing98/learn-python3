#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# runfile('E:/Github/learn-python3/samples/basic/the_dict.py', wdir='E:/Github/learn-python3/samples/basic')

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Stone_Hou'] = 100
print('Stone\'s Score is', d['Stone_Hou'])


d['Jack'] = 90
d['Jack']
# 90
d['Jack'] = 88
d['Jack']
# 88

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
'Thomas' in d
# False

d.get('Thomas')
d.get('Thomas', -1)
# 注意：返回None的时候Python的交互式命令行不显示结果。
#-1

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
# 75
print("After pop out Bob, diction d is as follow:\n", d)
# {'Jack': 88, 'Michael': 95, 'Stone_Hou': 100, 'Tracy': 85}

d = {1,2,3}
print(d)