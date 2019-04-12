from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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