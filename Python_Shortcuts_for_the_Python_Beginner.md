Python Shortcuts for the Python Beginner
======

> Translated from blog.92fenxiang.com/articles/1421931112

以下是我在Python中，多年来收集的一些有用的快捷键和工具。希望你能在其中找到对你有帮助的。

## 1. 交换变量
```
x = 6
y = 5

x, y = y, x

print x
>>> 5
print y
>>> 6
```

## 2. if 语句在行内
```
print "Hello" if True else "World"
>>> Hello
```

## 3. 连接
下面的最后一种方式在绑定两个不同类型的对象时显得很酷。
```
nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
print nfc + afc
>>> ['Packers', '49ers', 'Ravens', 'Patriots']

print str(1) + " world"
>>> 1 world

print `1` + " world"
>>> 1 world

print 1, "world"
>>> 1 world
print nfc, 1
>>> ['Packers', '49ers'] 1
```

## 4. 计算技巧
```
#向下取整
print 5.0//2
>>> 2
# 2的5次方
print 2**5
>> 32
```

### 5. 注意浮点数的除法
```
print .3/.1
>>> 2.9999999999999996
print .3//.1
>>> 2.0
```

## 6. 数值比较
```
x = 2
if 3 > x > 1:
   print x
>>> 2
if 1 < x > 0:
   print x
>>> 2
```

## 7. 两个列表同时迭代
```
nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
for teama, teamb in zip(nfc, afc):
     print teama + " vs. " + teamb
>>> Packers vs. Ravens
>>> 49ers vs. Patriots
```

## 8. 带索引的列表迭代
```
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for index, team in enumerate(teams):
    print index, team
>>> 0 Packers
>>> 1 49ers
>>> 2 Ravens
>>> 3 Patriots
```

## 9. 列表推导
```
#已知一个列表，刷选出偶数列表方法：
numbers = [1,2,3,4,5,6]
even = []
for number in numbers:
    if number%2 == 0:
        even.append(number)

#用下面的代替
numbers = [1,2,3,4,5,6]
even = [number for number in numbers if number%2 == 0]
```

## 11. 字典推导
```
teams = ["Packers", "49ers", "Ravens", "Patriots"]
print {key: value for value, key in enumerate(teams)}
>>> {'49ers': 1, 'Ravens': 2, 'Patriots': 3, 'Packers': 0}
```

## 12. 初始化列表的值
```
items = [0]*3
print items
>>> [0,0,0]
```

## 13. 将列表转换成字符串
```
teams = ["Packers", "49ers", "Ravens", "Patriots"]
print ", ".join(teams)
>>> 'Packers, 49ers, Ravens, Patriots'
```

## 14. 从字典中获取元素
```
不要用下列的方式
data = {'user': 1, 'name': 'Max', 'three': 4}
try:
   is_admin = data['admin']
except KeyError:
   is_admin = False
替换为
data = {'user': 1, 'name': 'Max', 'three': 4}
is_admin = data.get('admin', False)
```

## 15. 获取子列表
```
x = [1,2,3,4,5,6]
#前3个
print x[:3]
>>> [1,2,3]
#中间4个
print x[1:5]
>>> [2,3,4,5]
#最后3个
print x[-3:]
>>> [4,5,6]
#奇数项
print x[::2]
>>> [1,3,5]
#偶数项
print x[1::2]
>>> [2,4,6]
```

## 16. 60个字符解决FizzBuzz
```
前段时间Jeff Atwood 推广了一个简单的编程练习叫FizzBuzz，问题引用如下：
写一个程序，打印数字1到100，3的倍数打印“Fizz”来替换这个数，5的倍数打印“Buzz”，对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”。
这里有一个简短的方法解决这个问题：
for x in range(101):print"fizz"[x%3*4::]+"buzz"[x%5*4::]or x
```

## 17. 集合
```
用到Counter库
from collections import Counter
print Counter("hello")
>>> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```

## 18. 迭代工具
```
和collections库一样，还有一个库叫itertools
from itertools import combinations
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for game in combinations(teams, 2):
    print game
>>> ('Packers', '49ers')
>>> ('Packers', 'Ravens')
>>> ('Packers', 'Patriots')
>>> ('49ers', 'Ravens')
>>> ('49ers', 'Patriots')
>>> ('Ravens', 'Patriots')
在python中，True和False是全局变量，因此：
False = True
if False:
   print "Hello"
else:
   print "World"

>>> Hello
```

> 译文源自：blog.92fenxiang.com/articles/1421931112
> 原文：Python Shortcuts for the Python Beginner
