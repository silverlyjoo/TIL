from django.contrib import admin
from .models import Board, Student

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at',)
    
class StudentAdmin(admin.ModelAdmin):
    L = ('name', 'email', 'birthday', 'age',)


admin.site.register(Board, BoardAdmin)
admin.site.register(Student, StudentAdmin)