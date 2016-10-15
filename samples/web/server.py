#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* @Author: Stone_Hou
* Created Date: 2016-10-15 23:02:59
* Version History: 1.0
* runfile('E:/Github/learn-python3/samples/basic/the_dict.py', wdir='E:/Github/learn-python3/samples/basic')
"""
# @author: Administrator

# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()



"""
from wsgiref.simple_server import make_server


# ============================================================================
# ============================================================================
# WSGI接口定义只要求Web开发者实现一个函数，就可以响应HTTP请求

# 有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，
# 然后构造HTML，通过start_response()发送Header，最后返回Body。

# 整个application()函数本身没有涉及到任何解析HTTP的部分，
# 即底层代码不需要自己编写，只负责在更高层次上考虑如何响应请求就可以了。

# application()函数必须由WSGI服务器来调用。

# Python内置了一个WSGI服务器，该模块为wsgiref，是用纯Python编写的WSGI服务器的参考实现。
# 所谓"参考实现"是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

# application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
# environ        -  一个包含所有HTTP请求信息的dict对象
# start_response -  一个发送HTTP响应的函数

def application(environ, start_response):
    # start_response()函数发送HTTP响应的头部Header
    # 注意Header只能发送一次，即只能调用一次start_response()函数
    # start_response()函数接收两个参数：
    # 一个是HTTP响应码，
    # 一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
    status = '200 OK'       # HTTP Status
    response_headers = [('Content-Type', 'text/html; charset=utf-8')]   # HTTP Headers
    start_response(status, response_headers)

    # 函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]           # 网络传输的数据都是bytes类型


# ============================================================================
# ============================================================================
# make_server()负责启动WSGI服务器，加载application()函数
# 在同一个目录下，然后在命令行输入python server.py来启动WSGI服务器
# 按Ctrl+C终止服务器
# 启动成功后，打开浏览器，输入下面的地址，就可以看到结果
# http://localhost:9898/
# http://localhost:9898/Perhaps

# 创建一个服务器，IP地址为空，端口为9898，处理函数为application
# 注意：如果8000(->9898)端口已被其他程序占用，启动将失败，请修改成其他端口。
httpd = make_server('', 9898, application)
print('Serving on port 9898...')

# Respond to requests until process is killed
httpd.serve_forever()


'''
# issue
OSError: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions
solution: 8000 -> 9898
'''


'''
# log result
Serving on port 9898...
127.0.0.1 - - [31/Aug/2016 16:18:06] "GET / HTTP/1.1" 200 20
127.0.0.1 - - [31/Aug/2016 16:18:06] "GET /favicon.ico HTTP/1.1" 200 28
127.0.0.1 - - [31/Aug/2016 16:18:07] "GET /favicon.ico HTTP/1.1" 200 28

"""