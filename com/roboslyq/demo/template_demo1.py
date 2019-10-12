from django.shortcuts import render


def template_demo1(request):
    return render(request, 'template_demo1.html')


def template_demo2(request):
    return render(request, 'index.html')
