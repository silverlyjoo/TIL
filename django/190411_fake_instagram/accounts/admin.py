from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User


# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'introduction', 'user_id',]
    
admin.site.register(Profile, ProfileAdmin)


admin.site.register(User, UserAdmin)