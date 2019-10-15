from django.shortcuts import render


def logon(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if username != 'roboslyq' or password != '123456':
            return render(request, 'error.html', {'errorcode': '999999', 'errormessage': '用户名或密码错误'})
        else:
            return render(request, 'welcome.html', {'username': username, 'password': password})
