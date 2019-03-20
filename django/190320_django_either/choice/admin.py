from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ['pk', 'title', 'select_1', 'select_2',]

class AnswerAdmin(admin.ModelAdmin):

    list_display = ['pk','pick', 'comment', 'question_id']
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)