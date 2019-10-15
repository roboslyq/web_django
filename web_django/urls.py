"""web_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from com.roboslyq.demo.helloworld import helloworld
from com.roboslyq.usercenter.logon import logon
import com.roboslyq.index as index
import com.roboslyq.demo.template_demo1 as template


urlpatterns = [
    url(r'^$', index.index),  # 设置首页
    path('admin/', admin.site.urls),
    url('hello/', helloworld.hello1),
    url('logon/', logon.logon),
    url('template1/', template.template_demo1),
    url('template2/', template.template_demo2)
]
