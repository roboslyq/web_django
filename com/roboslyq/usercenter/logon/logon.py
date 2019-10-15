from django.shortcuts import render


def logon(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        reshtml = 'welcome.html'
        if username != 'roboslyq' or password != '123456':
            reshtml = 'error.html'

    return render(request, reshtml, {'username': username, 'password': password})
