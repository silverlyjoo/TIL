from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def choice_image_path(instance, filename):
    return f'choice/images/{filename}'

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    select_1 = models.CharField(max_length=200)
    img_1 = ProcessedImageField(
        upload_to = choice_image_path,
        processors = [ResizeToFill(300, 200)],
        format = 'JPEG',
        options = {'quality' : 90},
    )
    select_2 = models.CharField(max_length=200)
    img_2 = ProcessedImageField(
        upload_to = choice_image_path,
        processors = [ResizeToFill(300, 200)],
        format = 'JPEG',
        options = {'quality' : 90},
    )
    
    def __str__(self):
        return self.title
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.comment}'