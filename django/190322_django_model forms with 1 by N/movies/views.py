from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Genre, Movie, Score
from . import forms
from django.db.models import Avg

# Create your views here.

def index(request):
    # movies = Movie.objects.order_by('-pk')
    movies = get_list_or_404(Movie.objects.annotate(score_avg=Avg('score__score')))
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)
    
    
def create(request):
    
    if request.method == 'POST':
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:index')
        
    else:
        form = forms.MovieForm()
    context = {
        'form':form
    }
    return render(request, 'movies/form.html', context)
    

def detail(request, movie_pk):
    
    movie = get_object_or_404(Movie, pk=movie_pk)
    scores = movie.score_set.all()
    form_score = forms.ScoreForm()
    context = {
        'movie': movie,
        'form_score':form_score,
        'scores':scores
    }
    
    
    return render(request, 'movies/detail.html', context)
    
    
def delete(request, movie_pk):
    
    if request.method == "POST":
        movie = get_object_or_404(Movie, pk=movie_pk)
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie_pk)
        
def update(request, movie_pk):
    
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == "POST":
        form = forms.MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie_pk)
    else:
        form = forms.MovieForm(instance=movie)
        
    context = {
        'form':form,
        'movie':movie,
    }
    return render(request, 'movies/form.html', context)
    

def scores_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method =="POST":
        score = Score(movie=movie)
        form = forms.ScoreForm(request.POST, instance=score)
        if form.is_valid():
            score = form.save()
            return redirect('movies:detail', movie_pk)
    return redirect('movies:detail', movie_pk)
    
    
def score_delete(request, movie_pk, score_pk):
    
    movie = get_object_or_404(Movie, pk=movie_pk)
    score = get_object_or_404(Score, pk=score_pk)
    
    if request.method =="POST":
        score.delete()
        return redirect('movies:detail', movie_pk)
    return redirect('movies:detail', movie_pk)