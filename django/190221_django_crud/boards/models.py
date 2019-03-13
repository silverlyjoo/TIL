from django.db import models

class Board(models.Model): # 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현됩니다.
    title = models.CharField(max_length=10) # max_length는 CharField 의 필수 인자입니다.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True : 장고 모델의 최초저장시 현재 날짜 적용, 필수 인자는 아닙니다.
    updated_at = models.DateTimeField(auto_now=True) # auto_now : 장고 모델이 저장될 때마다 현재 날짜로 갱신.
    
    def __str__(self):
        return f'{self.id}: {self.title}'


class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'