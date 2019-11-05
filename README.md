# web_django
> 本项项目主要是django学习，以**刘江**老师的Python教程项目源码为基础，进行相关整合改造，仅作学习使用。在些感谢刘江老师写的博客，真的很棒！！！

# 项目结构

​	目前项目主要分4个模块：

 	1. django的原生自带admin模块，访问路径为： http://127.0.0.1:8000/admin/ 
 	2. 自己开发的登录模块，默认访问路径为： http://127.0.0.1:8000/login/ 或者 http://127.0.0.1:8000/
 	3. 刘江老师的资产管理系统：在登录模块合建成功之后，自动跳转到此模块
 	4. 资产管理模块的客户端，安装在具体的服务器上，可以收集相关服务器信息上送到资产管理模块。

# 测试用户

**用户名**: roboslyq

**密码**:123456

# 项目启动

```python
python manage.py
```

启动日志如下：

>C:\ProgramData\Anaconda3\envs\web_django\python.exe D:/helloworld/workspace_python/web_django/manage.py runserver
>init 文件作用测试... ...
>init 文件作用测试... ...
>Watching for file changes with StatReloader
>Performing system checks...
>
>System check identified no issues (0 silenced).
>November 05, 2019 - 22:48:45
>Django version 2.2.6, using settings 'web_django.settings'
>Starting development server at http://127.0.0.1:8000/
>Quit the server with CTRL-BREAK.