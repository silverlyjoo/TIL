from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings



class Hashtag(models.Model):
    content = models.TextField(unique=True)
    
    def __str__(self):
        return self.content



class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    
    def __str__(self):
        return self.content
    
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    file = ProcessedImageField(
        upload_to = '',
        processors=[ResizeToFill(100,100)],
        format = 'JPEG',
        options = {'quality':100},
        )
        

class Comment(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content