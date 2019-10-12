from django import views
from django.conf.urls import url
from django.http import HttpResponse


# from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! --roboslyq" + request.GET['q1'] + "--" + request.GET['q'])
