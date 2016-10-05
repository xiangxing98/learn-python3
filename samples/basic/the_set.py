#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
# {1, 2, 3}
# 注意，传入的参数[1, 2, 3]是一个list，
# 而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，
# 显示的顺序也不表示set是有序的。。
# 重复元素在set中自动被过滤


s2 = set([2, 3, 4])
print(s1 & s2)

print(s1 | s2)

# 通过add(key)方法可以添加元素到set中，
# 可以重复添加，但不会有效果：
s = set([1, 1, 2, 2, 3, 3])
s.add(4)
print(s)
# {1, 2, 3, 4}
s.add(4)
print(s)
# {1, 2, 3, 4}

#通过remove(key)方法可以删除元素：
s.remove(4)
print(s)
#{1, 2, 3}

# set可以看成数学意义上的无序和无重复元素的集合，
# 因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
#{2, 3}
print(s1 | s2)
#{1, 2, 3, 4}

# set和dict的唯一区别仅在于没有存储对应的value，
# 但是，set的原理和dict一样，
# 所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，
# 也就无法保证set内部“不会有重复元素”。
# 试试把list放入set，看看是否会报错。

# 再议不可变对象

# 上面我们讲了，str是不变对象，而list是可变对象。
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

a = ['c', 'b', 'a']
a.sort()
print(a)
# ['a', 'b', 'c']

# 而对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
print(a.replace('a', 'A'))
# 'Abc'

print(a)
# 'abc'

# 虽然字符串有个replace()方法，也确实变出了'Abc'，
# 但变量a最后仍是'abc'，应该怎么理解呢？
# 我们先把代码改成下面这样：

a = 'abc'
b = a.replace('a', 'A')
print(b)
# 'Abc'
print(a)
# 'abc'
# 要始终牢记的是，a是变量，而'abc'才是字符串对象！
# 有些时候，我们经常说，对象a的内容是'abc'，
# 但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：

# 当我们调用a.replace('a', 'A')时，
# 实际上调用方法replace是作用在字符串对象'abc'上的，
# 而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
# 相反，replace方法创建了一个新字符串'Abc'并返回，
# 如果我们用变量b指向该新字符串，就容易理解了，
# 变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：

# 所以，对于不变对象来说，调用对象自身的任意方法，
# 也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，
# 这样，就保证了不可变对象本身永远是不可变的。

# 小结
# 使用key-value存储结构的dict在Python中非常有用，
# 选择不可变对象作为key很重要，最常用的key是字符串。

# tuple虽然是不变对象，
# 但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。

d1 = {1,2,3}
print(d1)
#{1, 2, 3}
d2 = {1, [2, 3]}
#TypeError: unhashable type: 'list'
print(d2)

# set()是一个函数，返回Set类型，而参数要求是iterable
# args = (1, (2, 3))
# s = set(args)
# 合到一起写就是 s = set((1, (2, 3)))
# 注意最外层括号是函数调用，里面的括号是tuple

#以下是错误示范
#s1 = set(1,2,3)
#print(s1)
#TypeError: set expected at most 1 arguments, got 3

#s2 = set(1, [2, 3])
#print(s2)
#TypeError: set expected at most 1 arguments, got 2

#s3 = set(（1,2,3）)
#SyntaxError: invalid character in identifier，中文的括号

s3 = set((1,2,3))
print(s3)
#{1, 2, 3}