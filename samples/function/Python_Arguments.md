Python_Arguments.md
======================================================================

## python的参数 发表于 2016年9月18日
> http://www.qiangtaoli.com/bootstrap/blog/001474192642421efbf41449b2e4a3b99e8202c54d2d8a2000

## python的参数类型 
今天来聊一下python的参数类型，不过我并不是说int/float/bool/list...这些基本数值的类型，而是在python中函数(function)或方法(method)的参数类型有哪些，每种参数类型要怎么传参才能调用，默认参数要怎么设置才算合理。在python有一个标准模块inspect, 主要提供了四种用处：

1. 对是否是模块，框架，函数等进行类型检查。 
2. 获取源码 
3. 获取类或函数的参数的信息 
4. 解析堆栈 

很明显第3点就是我们想要的功能，inspect模块有对python函数的参数类型有详细的定义。

## 有哪几种参数类型？

### POSITIONAL_OR_KEYWORD 
如果没有任何*的声明，那么就是POSITIONAL_OR_KEYWORD类型的，如同语义一样，POSITIONAL_OR_KEYWORD类型的参数可以通过位置POSITIONAL传参调用，也可以过关键字KEYWORD传参。以下是一个最简单的例子：
```
def foo(a): 
    pass

# 位置传参调用
foo(1)
# 关键字传参调用
foo(a=1)
```

### VAR_POSITIONAL 
第二种是可变的位置参数，通过一个*前缀来声明，如果你看到一个*xxx的函数参数声明（不是函数调用！声明和调用是两种不同的含义的），那一定是属于VAR_POSITIONAL类型的，如同语义，这种类型的参数只能通过位置POSITIONAL传参调用，不支持关键字KEYWORD传参，在函数内部，VAR_POSITIONAL类型的参数以一个元祖(tuple)显示，有一点需要注意的，VAR_POSITIONAL类型可以不传任何参数调用也不会报错，而且只允许存在一个。以下是一个简单的例子：

```
def foo(*b):
    print(b)

# 不传参数不会报错，参数值是一个空元祖  
foo() # 结果是 ()
# 可以传入任意个位置参数调用
foo(1, 2.0, '3', True) #结果是 (1, 2.0, '3', True)
```

### KEYWORD_ONLY 
第三种是关键字参数，这种参数只会在VAR_POSITIONAL类型参数的后面而且不带**前缀。如同语义，这类参数只能用关键字KEYWORD来传参，不可以用位置传参，因为位置传的参数全让前面的VAR_POSITIONAL类型参数接收完了，所以KEYWORD_ONLY只能通过关键字才能接收到参数值。以下是一个简单的例子：
```
# VAR_POSITIONAL不需要使用时，可以匿名化
def foo(*, c):
    pass

# 只能关键字传参调用
foo(c=1)
```

### VAR_KEYWORD 
第四种是可变的关键字参数，VAR_KEYWORD类型的参数通过**前缀来声明（不是函数调用！声明和调用是两种不同的含义的）。如同语义，这种类型的参数只能通过关键字KEYWORD调用，但可以接收任意个关键字参数，甚至是0个参数，在函数内部以一个字典(dict)显示。VAR_KEYWORD类型的参数只允许有一个，只允许在函数的最后声名。以下是简单的例子：
```
def foo(**d):
    print(d)

# 不传参数不会报错，参数值是一个空字典
foo() # 结果是 {}
# 可以传入任意个关键字参数调用
foo(a=1, b=2.0, c='3', d=True) # 结果是 {'d': True, 'c': '3', 'b': 2.0, 'a': 1}
```

### POSITIONAL_ONLY 
第五种是位置参数，选择最后说这个，是因为它一点也不重要，属于python的历史产物，你无法在高版本的python中创建一个POSITIONAL_ONLY类型的参数，在某种底层的内置函数也许会使用这类型的参数，但我试用inspect模块也没法正确识别它的命名，但在Ipython的??帮助下，还是能看到Init signature: dict(self, /, *args, **kwargs)这里的self就是位置参数POSITIONAL_ONLY了。相信我，你不会需要用到它的，现在python推荐用VAR_POSITIONAL来代替它。下面是一个综合示例：

```
import inspect

def foo(a, *b, c, **d):
    pass
for name, parame in inspect.signature(foo).parameters.items():
    print(name, ': ', parame.kind)
a :  POSITIONAL_OR_KEYWORD
b :  VAR_POSITIONAL
c :  KEYWORD_ONLY
d :  VAR_KEYWORD
```

## 默认参数

VAR类型不允许设置默认参数
POSITIONAL_OR_KEYWORD和KEYWORD_ONLY可以自定义默认参数，而VAR_POSITIONAL和VAR_KEYWORD不允许自定义默认参数的，因为VAR_POSITIONAL的默认参数是tuple()空元祖，而VAR_KEYWORD的默认参数是dict()空字典。如果自定义了默认参数的话，调用函数的时候可以不必传参，如果默认值是空的话，那就必须传参数才能调用。

### 默认参数的位置 
POSITIONAL_OR_KEYWORD类型的默认参数一定要放在后面，否则会报错，KEYWORD_ONLY虽然没有强制要求，因为都是用关键字传参，谁先谁后都无所谓，但最好还是尽可能地放在后面吧。

### 默认参数不默认？ 
默认参数绝对不能设置为可变类型（比如list, dict, set），如果你在函数内改变了默认参数，下次再调用时它就不再是默认值了。
正确的示例：
```
def foo(p1, p2=2.0, *, k1, k2=None):
    a_list = k2 or list()
    pass

foo(1, k1='3')
```

### 接收参数的优先级

1. 先接收POSITIONAL_OR_KEYWORD
2. 再接收KEYWORD_ONLY
3. 再接收VAR_POSITIONAL和VAR_KEYWORD，这两者没有交集

```
def foo(a, *b, c, **d):
    print(a, b, c, d, sep='\n')

foo(1, 2, '3', c=3, x=1, y=2)

# a: 1
# b: (2, '3')
# c: 3
# d: {'x': 1, 'y': 2}
```

## 关键字参数的适用场景是什么？

个人观点，只要配合上可变长位置参数VAR_POSITIONAL才算是关键字参数KEYWORD_ONLY的适合场景，我们先来看一个函数。

```
def my_print(*args, sep=' ', end='\n'):
    string = sep.join(map(str, args)) + end
    print(string)

my_print(1,2,[12, (12, {4,True})],(12.2,False))
my_print(1,2,[12, (12, {4,True})],(12.2,False), sep=', ')
my_print(1,2,[12, (12, {4,True})],(12.2,False), end='\ndone!\n')
```

你可以像上面这样调用它，如果你只用位置关键字参数POSITIONAL_OR_KEYWORD是很难达到这样的效果的，没错，你可以把sep和end移到前面去，但是你没有为这两个参数设默认值，导致你每次调用函数都不得不填写这两个本来可以不填写的参数，就算你不嫌麻烦，但你很难了解每个参数的语义是什么，你不用关键字传参的话，别人怎么知道，你的第一个参数是sep第二是end？所以最终还得用关键字传参数的。这就是关键字参数的适用场景。