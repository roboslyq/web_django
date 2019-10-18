from django.shortcuts import render


def index(request):
    return render(request, 'logon.html', {"welcome": "欢迎来到django世界"})
