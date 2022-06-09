from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # print(dir(request))
    return HttpResponse('<h1>Главная страница</h1>')

def test(request):
    return HttpResponse('<h2>Тестовая страница</h2>')

























