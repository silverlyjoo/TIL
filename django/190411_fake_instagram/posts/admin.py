from django.contrib import admin
from .models import Post, Hashtag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at', 'updated_at']
    
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['content',]



admin.site.register(Post, PostAdmin)
admin.site.register(Hashtag, HashtagAdmin)