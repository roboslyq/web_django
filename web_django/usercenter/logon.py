from django.contrib import auth
from django.shortcuts import render, redirect


def logon(request):
    logon1 = Logon()
    return logon1.logon(request)


class Logon(object):

    @staticmethod
    def get(request):
        return render(request, "logon.html")

    # 登陆模块
    @staticmethod
    def logon(request):
        next_url = request.GET.get("next")
        print(request.POST)
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # django内置的授权模块
        user_obj = auth.authenticate(request, username=username, password=pwd)
        if user_obj:
            # 用户名和密码正确
            auth.login(request, user_obj)  # 给该次请求设置了session数据，并在响应中回写cookie
            if next_url:
                return redirect(next_url)
            else:
                return redirect("/welcome.html")
        else:
            # 用户名或密码错误
            return render(request, "logon.html", {"error_msg": "用户名或密码错误"})