from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime

# Create your views here.

def index(request):
    # return HttpResponse('Welcome to Django !')
    return render(request, 'home/index.html')
    
def dinner(request):
    menus = ['참치회', '방어회', '연어회', '광어회']
    pick = random.choice(menus)
    pick2 = random.choice(menus)
    return render(request, 'home/dinner.html', {'menus': menus, 'pick': pick, 'pick2': pick2})
    
def hello(request, name):
    return render(request, 'home/hello.html', {'name': name})
    
def cube(request, num):
    cubenum = num**3
    return render(request, 'home/cube.html', {'num': num, 'cubenum':cubenum})
    
def ping(request):
    return render(request, 'home/ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'home/pong.html', {'data':data})
    
    
def user_new(request):
    return render(request, 'home/new.html')
    
def user_create(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    return render(request, 'home/create.html', {'id':id, 'pwd':pwd})
    
def template_example(request):
    my_list = ['스낵면', '진라면', '짜파게티', '사리곰탕']
    my_sentence = 'life is short, you need python!'
    messages = ['아보카도', '토마토으으싫어', '샐러리', '아스파라거스']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'home/template_example.html', {'my_list': my_list, 'my_sentence': my_sentence, 'messages': messages, 'empty_list': empty_list, 'datetimenow': datetimenow})
    
def static_example(request):
    return render(request, 'home/static_example.html')