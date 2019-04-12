from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/update/', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('', views.list, name='list'),
]
