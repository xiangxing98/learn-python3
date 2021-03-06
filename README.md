Python 3 教程
============
<!-- MarkdownTOC -->

- Python3 Free Course From liaoxuefeng
- Git 日常发布流程
- recommand-some-free-stuff

<!-- /MarkdownTOC -->

## Python3 Free Course From liaoxuefeng

1. 2016-10-02 Stone Hou Learning From [liaoxuefeng's Python Free Course](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000 "liaoxuefeng's Python Free Course")

2. 2016-10-07 Add [Crossin的编程教室](http://crossincode.com/home/ "Crossin的编程教室")

3. 2016-10-07 Add [Zhihu Python Topic Top Answers](https://www.zhihu.com/topic/19552832/top-answers "Zhihu Python Topic Top Answers")

> Never too old to learning something new. Stone_Hou 侯祥胡 2016 National Day @ Beijing 

## Git 日常发布流程
```
//本地如果无远程代码，先做这步，不然就忽略 
git clone git@github.com:heiniuhaha/heiniuhaha.github.com.git

//定位到你blog的目录下 
cd .ssh/heiniuhaha.github.com

 //先同步远程文件，后面的参数会自动连接你远程的文件
git pull origin master

//查看本地自己修改了多少文件
git status 

//添加远程不存在的git文件
git add . 

//提交到本地版本库
git commit * -m "what I want told to someone" 

//更新到远程服务器上
git push origin master

//删除已经缓存修改的文件*spyder*,然后重新添加提交
git rm -r -f --cached *spyder*

```

## [recommand-some-free-stuff](http://www.paidepaiper.top/2016/09/29/recommand-some-free-stuff/#more "recommand-some-free-stuff")

### [python3教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000 "python3教程")

这个教程是廖雪峰大神写的，非常适合零基础自学编程的小白，教程最后还给出了一个博客站的源码作为实战训练。我学的时候已经有一点php基础，一点html、css、js基础，所以学的比较快。大概花了一个多月的时间，学得比较偷懒，最后的实战部分也只是做了一遍注释。

### [xx-net](https://github.com/XX-net/XX-Net "wall breaker")

### [菜鸟教程](http://www.runoob.com/ "菜鸟教程")

这个网站的教程非常全面，基本上你能想到的这上面都有。在廖大的网站学python时，我发现自己缺什么就上菜鸟教程补。在实际开发过程中也经常拿这网站当查询手册，是名副其实的菜鸟教程。

### [使用 Express + MongoDB 搭建多人博客](http://wiki.jikexueyuan.com/project/express-mongodb-setup-blog/simple-blog.html)

这可以说是我的nodejs入门教程，手把手教你怎么用express和mongodb写一个多人博客。由于之前有廖大的实战项目做基础，我上手这个教程还是蛮快的。我做完这个教程后把项目部署在heroku上，可以通过这个网址访问https://express-n-blog.herokuapp.com

### [鸟哥的Linux私房菜](http://linux.vbird.org/ "鸟哥的Linux私房菜")

如果只是想用Linux，那可以直接上手Ubuntu，这是一个对新手非常友好的Linux发行版。但如果想比较系统地学下Linux，那还是推荐看鸟哥的Linux私房菜。

### [django-tutorial](http://www.ziqiangxuetang.com/django/django-tutorial.html "django中文教程")

### Python 相关的一些资源
> 2016年十月16的一些

http://www.pythontab.com/

https://github.com/Vamei

http://www.cnblogs.com/vamei

https://www.douban.com/people/Oceannagirl/

### Learn Python the Hard Way-By ZED A. SHAW
[Learn Python the Hard Way-By ZED A. SHAW https://learnpythonthehardway.org/book/](https://learnpythonthehardway.org/book/ "Learn Python the Hard Way-By ZED A. SHAW")