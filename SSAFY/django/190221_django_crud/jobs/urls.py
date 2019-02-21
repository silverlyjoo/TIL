from django.urls import path
from . import views

urlpatterns = [
    path('pastlife/', views.pastlife, name='pastlife'),
    path('', views.index, name='index'),
]