from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Post, Image, Comment, Hashtag
from .forms import PostForm, ImageForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q
from itertools import chain
# Create your views here.

@login_required
def list(request):
    # followings = request.user.followings.all()
    # posts = Post.objects.filter(Q(post_user__in=followings) | Q(post_user=request.user.id)).order_by('-pk')
    # posts = Post.objects.order_by('-pk')
    
    followings = request.user.followings.all()
    chain_followings = chain(followings, [request.user])
    posts = Post.objects.filter(post_user__in=chain_followings).order_by('-pk')
    
    
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form,
    }
    return render(request, 'posts/list.html', context)
    
    

@login_required
def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.post_user = request.user
            post.save()
            
            # hashtag
            # 1. 게시글을 순회하면서 띄어쓰기를 잘라야함
            # 2. 자를 단어가 #으로 시작하는가?
            # 3. 이 해시태그가 기존 해시태그에 있는 건지?
            
            
            
            
            post_list = post.content.split()
            for word in post_list:
                if word[0] == '#':
                    hashtag = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(hashtag[0])
                    
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {
        'post_form':post_form,
        'image_form':image_form,
    }
    return render(request, 'posts/form.html', context)
    

@login_required
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if post.post_user != request.user:
        return redirect('posts:list')
    
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save()
            post.hashtags.clear()
            
            for word in post.content.split():
                if word.startwith('#'):
                    hashtag, new = Hashtag.objects.get_or_create(word)
                    post.hashtags.add(hashtag)
                
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    context = {
        'post_form':post_form
    }
    return render(request, 'posts/form.html', context)
    
    
@login_required
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if post.post_user != request.user:
        return redirect('posts:list')
    
    if request.method == "POST":
        post.delete()
        return redirect('posts:list')
    return redirect('posts:list')
    



@require_POST
@login_required
def comment_create(request, post_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_pk
        comment.save()
    
    return redirect('posts:list')
    
    
@require_POST
@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user != comment.user:
        return redirect('posts:list')
    
    comment.delete()
    return redirect('posts:list')
    
    

@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    r_user = request.user
    
    # 이미 해당 유저가 like_users에 존재하면 해당 유저를 삭제, 없으면 추가
    
    if r_user in post.like_users.all():
        post.like_users.remove(r_user)
    else:
        post.like_users.add(r_user)
        
    return redirect('posts:list')
    
    # if post.like_users.filter(pk=r_user.pk).exist():
    #     post.like_users.remove(r_user)
    # else:
    #     post.like_users.add(r_user)
        
@login_required
def explore(request):
    # posts = Post.objects.order_by('-pk')
    posts = Post.objects.exclude(post_user=request.user).order_by('-pk')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/explore.html', context)
    
    
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    posts = hashtag.post_set.order_by('-pk')
    context = {
        'hashtag':hashtag,
        'posts':posts
    }
    return render(request,'posts/hashtag.html', context)