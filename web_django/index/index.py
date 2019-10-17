from django.shortcuts import render


# 首页服务定义


def index(request):
    return render(request, 'logon.html')
