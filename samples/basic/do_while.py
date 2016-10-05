#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 计算1+2+3+...+100:
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

# 计算1+2+3+...+100:--version 2
sum = 0
n = 99 #why 99?
while n > 0:
    sum = sum + n
    n = n -2
print("sum is ", sum)
#2500

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 100:
    acc = acc * n
    n = n + 1
print("1x2x3x...x100 = ", acc)

#practise 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam','Michael', 'Bob', 'Tracy']
for name in L:
    print("Hello",name)

# Break, 在循环中，break语句可以提前退出循环。
# 例如，本来要循环打印1～100的数字：
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        print("n >10 and break now")
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue在循环过程中，也可以通过continue语句，
# 跳过当前的这次循环，直接开始下一次循环。

n = 0
while n < 10:
    n = n + 1
    print(n)
# 上面的程序可以打印出1～10。
# 但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue 
        # continue语句会直接继续下一轮循环，
        # 后续的print()语句不会执行
    print(n)
#执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9。
#可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。

# break语句可以在循环过程中直接退出循环，
# 而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
# 这两个语句通常都必须配合if语句使用

#Dead loop and Ctrl+C to Interrupt
n = 99
sum = 0
while n >= 99:
    sum = sum + n
    n = n + 1
print (sum)
