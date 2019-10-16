from django.shortcuts import render
from com.roboslyq.usercenter.logon.models import User


def logon(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user2 = User()
        obj = user2.query(user_id=username, password=password)
        if any(obj):
            return render(request, 'welcome.html', {'username': username, 'password': password})
        else:
            return render(request, 'error.html', {'errorcode': '999999', 'errormessage': '用户名或密码错误'})
