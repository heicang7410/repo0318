from django.shortcuts import render
from status.models import Status


def hello(request):
    x = request.GET.get('x', 0)
    x = int(x)
    data = Status.objects.all()
    return render(request, 'hello.html', {'result': x+1, 'data': data})

def index(request):
    return render(request, 'index.html', {})

