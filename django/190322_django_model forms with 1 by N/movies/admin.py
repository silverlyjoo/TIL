from django.contrib import admin
from .models import Genre, Movie, Score

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'audience', 'poster_url', 'description', 'genre_id',)
    
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'score', 'movie_id',)
    
    

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Score, ScoreAdmin)
