#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# runfile('E:/Github/learn-python3/samples/basic/the_dict.py', wdir='E:/Github/learn-python3/samples/basic')

# dict使用key返回对应的value

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

# 要避免key不存在的错误，有两种办法，
#一是通过in判断key是否存在：
if 'Paul' in d: 
    print(d['Paul'])
#'Thomas' in d
# False
    
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')
d.get('Thomas', -1)
print(d.get('Thomas'))

# 注意：返回None的时候Python的交互式命令行不显示结果。
#-1

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
# 75
print("After pop out Bob, diction d is as follow:\n", d)
# {'Jack': 88, 'Michael': 95, 'Stone_Hou': 100, 'Tracy': 85}

d = {1,2,3}
print(d)

#dict以key:value的形式输出
for key in d:
        print("%s:%s" %(key,d[key]))  #通过key查value: d[key]