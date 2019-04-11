from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('new/', views.create, name='create'),
    path('', views.list, name='list'),
]
