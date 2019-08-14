from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Board, Comment
from .forms import BoardForm, CommentForm
import hashlib

# Create your views here.


def index(request):
    
    boards = get_list_or_404(Board.objects.order_by('-pk'))
    
    context = {
        'boards':boards,
    }
    
    return render(request, 'boards/index.html', context)


@login_required
def create(request):
    if request.method =="POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {
        'form':form
    }
    return render(request, 'boards/form.html', context)
        
def detail(request, board_pk):
    
    
    
    board = get_object_or_404(Board, pk=board_pk)
    
    comment_form = CommentForm()
    
    context = {
        'board':board,
        'comment_form':comment_form,
    }
    return render(request, 'boards/detail.html', context)
    
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)

@login_required
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                board=form.save()
                return redirect('boards:detail', board.pk)
        else:
            form = BoardForm(instance=board)
    else:
        return redirect('boards:index')
    
    context = {
        'form':form,
        'board':board,
    }
    return render(request, 'boards/form.html', context)
            
        

@require_POST   
@login_required
def comment_create(request, board_pk):
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        
        comment.user = request.user
        comment.board_id = board_pk
        comment.save()
    
    return redirect('boards:detail', board_pk)
        
        
    # board = Board.objects.get(pk=board_pk)
    # user = request.user
    # content = request.POST.get('content')
    # comment = Comment(board=board, content=content, user=user)
    # comment.save()
    # return redirect('boards:detail', board.pk)


@login_required
@require_POST
def comment_delete(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('boards:detail', board_pk)
    
    
    # comment = Comment.objects.get(pk=comment_pk)
    # if request.method =='POST':
    #     comment.delete()
    #     return redirect('boards:detail', board_pk)
    # else:
    #     return redirect('boards:detail', board_pk)
    
