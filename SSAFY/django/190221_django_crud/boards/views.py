# 모듈 import 순서
# 1. 파이썬 표준 라이브러리 
# 2. core django : 장고 프레임 워크 내장 모듈
# 3. 3rd party library : pip 로 설치한 모듈들 ex) django-extension
# 4. 장고 프로젝트 app


from django.shortcuts import render, redirect
from .models import Board

# Create your views here.

def index(request):
    # boards = Board.objects.all()
    boards = Board.objects.order_by('-id')
    return render(request, 'boards/index.html', {'boards':boards})
    
def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()
    # Board.objects.create(title=title, content=content)
    return redirect(index)
    # return redirect('/boards/')
    
def detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/detail.html', {'board':board})
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')
    
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/edit.html', {'board':board})
    
def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/{board.pk}/')
    