from django.http import HttpResponse

def hello1(request):
    return HttpResponse("user center hello world")
