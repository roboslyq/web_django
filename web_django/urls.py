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
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url
# from django_app.usercenter import views as logonview
# import web_django.views as indexviews

# urlpatterns = [
#     # url(r'^$', indexviews.index),  # 设置首页
#     # path('admin/', admin.site.urls),
#     # url('logon/', logonview.logon),
#
# ]
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from django_app.usercenter.login import views

urlpatterns = [
    # Django默认的后台管理页面
    path('admin/', admin.site.urls),
    # 设置首页
    url(r'^$', views.index),
    path('index/', views.index),
    # 自定义登录请求
    path('login/', views.login),
    # 自定义用户注册请求
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
    # 图形验证码
    path('captcha/', include('captcha.urls')),
    path('assets/', include('django_app.cmdb.assets.urls')),
]