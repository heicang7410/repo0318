from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from status.models import Status


def hello(request):
    x = request.GET.get('x', 0)
    x = int(x)
    data = Status.objects.all()
    return render(request, 'hello.html', {'result': x+1, 'data': data})

def index(request):
    data = Status.objects.order_by('-id')
    return render(request, 'index.html', {'data': data})

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/index/')
    else:
        # Return an 'invalid login' error message.
        pass

def logout_view(request):
    logout(request)
    return redirect('/index/')

def say(request):
    text = request.POST['text']
    user = request.user
    Status.objects.create(text=text, user=user)
    return redirect('/index/')
