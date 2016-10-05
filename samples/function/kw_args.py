#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
# 参数作为一个list或tuple传进来

#a^2 + b^2 + c^2 + ……
def calc1(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#但是调用的时候，需要先组装出一个list或tuple：
calc1([1, 2, 3])
#14
calc1((1, 3, 5, 7))
#84

#如果利用可变参数，调用函数的方式可以简化成这样
#calc1(1, 2, 3)
#14，TypeError: calc1() takes 1 positional argument but 3 were given
#calc1(1, 3, 5, 7)
#84，TypeError: calc1() takes 1 positional argument but 4 were given

#把函数的参数改为可变参数，C语言的指针出现了，仅在参数前加一个*号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#在函数内部，参数numbers接收到的是一个tuple，
#因此，函数代码完全不变。但是，调用该函数时，
#可以传入任意个参数，包括0个参数：
calc(1, 2, 3) #14
calc() #0


#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
#14
#这种写法当然是可行的，问题是太繁琐，
#所以Python允许你在list或tuple前面加一个*号，
#把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
calc(*nums) #14
#*nums表示把nums这个list的所有元素作为可变参数传进去。
#这种写法相当有用，而且很常见。


#关键字参数
#可变参数允许你传入0个或任意个参数，
#这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，
#这些关键字参数在函数内部自动组装为一个dict。请看示例：
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

#dictionary
data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(AdamLee = data['Adam Lee'], Lisa_S = data['Lisa S'], F_Bart = data['F.Bart'])
#上面复杂的调用可以用简化的写法
print_scores(**data)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
# 对kw的改动不会影响到函数外的extra。


#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。    

f1(1, 2)
#a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
#a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
#a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

#最神奇的是通过一个tuple和dict，你也可以调用上述函数：

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，
#无论它的参数是如何定义的。


#summary
#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
#要注意定义可变参数和关键字参数的语法：
#
#*args是可变参数，args接收的是一个tuple；
#
#**kw是关键字参数，kw接收的是一个dict。
#
#以及调用函数时如何传入可变参数和关键字参数的语法：
#
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

# 计算某个数组的平方和或n次方之和
def quadratic_sum(nums,x = 2):
    n = x
    sum = 0
    for i in nums:
        x = n
        s = 1
        while x > 0:
            x = x - 1
            s = s * i
        sum = sum + s
    print('数组',nums,'的',n,'次方之和为：',sum)
    return sum 

quadratic_sum([1,2,3,4,5,6,7,8,9])

#这章有点繁琐，看着头疼。拉到最下面看总结更清晰。。。
#
#下面是我的理解。前面三个基本是没问题的。
#第一种情况：print(n)
#一个函数需要传入最少一个参数，如果这个参数没有设定默认值，那么而这个就是必选参数。n
#
#第二种情况：print(a,b) =》 print(a,b=0)
#左边，因为传入的参数没有设定默认值，那么这两个也是必选参数
#右边，因为b设定了默认值，所以只有a是必选参数，此时b就是默认参数。
#只要记得，有设置默认值的就是默认参数。
#
#位置参数：print(who,"call",name)//英语渣，随便打的
#函数处理传进来的参数默认是从左到右处理的，位置位置，就是让你注意参数的位置顺序。如我写的，你肯定要注意，who这个位置应该传进you或者I,而name的位置应该传进peter或者其他的人名。所以I call Hank是对的，而Hank call I是错的。
#
#下面三个有点烦。
#可变参数*args
#举个栗子，pring("你和",*args,"是朋友")，因为*args不确定啊。
#有可能是args=('张三','李四'),也有可能是args=('张三','李四','王五')。
#所以...能不能Get到点？？？Get不到再回复我吧。
#
#*args是可变参数，args接收的是一个tuple；
#
#关键字参数：**kw
#再举个栗子，我朋友要去相亲，他的条件比较奇葩，必须有好名字，和适合的年龄，其他的再看看。那么就可以这样print(name,ages,**kw)。名字和年龄必须知道。
#第一个菇凉的信息是>>>如花 18。朋友看到名字，立马说下一个。
#第二个菇凉的信息是>>>似玉 19 车：有 房：有。先不理我朋友了。我们来看看，怎么突然就有房有车呢？因为似玉家有钱，把**kw都用上了。kw={"房":"有","车":"有"}，所以似玉的print是这样的name,ages,house,car
#
#然后。。。。。好吧。我编不下去了。自己get一下吧。不懂再讨论一下。
#
#**kw是关键字参数，kw接收的是一个dict。
#
#最后一个，命名关键字参数 T_T什么鬼。
#按照我的理解，就是把参数封装进一个dict里面。然后调用就必须是key="value"这样。而且也可以设置默认值。调用时没有默认值的时候会出现错误。
#
#    def person(name,ages,*,house,car)
#        print(name,ages,house,car)
#
#    person("似玉",18,house="有",car) #这样会出现错误
#    person("似玉",18,house="有",car="有”) #这样就不会。
#我们再改一下。
#
#    def person(name,ages,*,house,car="有")
#        print(name,ages,house,car)
#
#    person("似玉",18,house="有",car) #这样会出现错误,因为car已经设置默认值了，是默认参数
#    person("似玉",18,house="有") #这样就不会。
#总而言之，命名关键字参数就是将一般参数封装进dict的参数。
#不同在于
#
#书写参数时需要确定有没有前置*，或者可变参数。
#调用参数是需要写参数名，即格式为key='value',而一般的是直接书写value即可
#参数有默认值时，一般参数写不写都一样，但是关键参数一定不能写，举例：
#
#  #这是一般参数的，命名关键字参数的例子在上面
#  def person(name,ages=18,*,house,car="有")
#      print(name,ages,house,car)
#
#  person("似玉",18,house="有") #正常，似玉 18 有 有
#  person("似玉",house="有") #正常，似玉 18 有 有
#相同的就是
#
#没有默认值的都是必选参数
#还有一个点，就是命名关键词参数应该是不存在位置参数的。因为调用时已经注明了参数名。而一般参数不需要注明参数名，所以会按照位置来处理。