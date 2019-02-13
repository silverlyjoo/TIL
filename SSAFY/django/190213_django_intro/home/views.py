from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.

def index(request):
    return HttpResponse('Welcome to Django !')
    
def dinner(request):
    menus = ['참치회', '방어회', '연어회', '광어회']
    pick = random.choice(menus)
    pick2 = random.choice(menus)
    return render(request, 'dinner.html', {'menus': menus, 'pick': pick, 'pick2': pick2})
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request, num):
    cubenum = num**3
    return render(request, 'cube.html', {'num': num, 'cubenum':cubenum})
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data':data})
    
    
def user_new(request):
    return render(request, 'new.html')
    
def user_create(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    return render(request, 'create.html', {'id':id, 'pwd':pwd})