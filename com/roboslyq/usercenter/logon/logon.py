from django.shortcuts import render
from com.roboslyq.usercenter.logon import models


def logon(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        obj = models.User.objects.get(name=username, password=password)
        if any(obj):
            return render(request, 'welcome.html', {'username': username, 'password': password})
        else:
            return render(request, 'error.html', {'errorcode': '999999', 'errormessage': '用户名或密码错误'})
