from django.urls import path
from . import views

urlpatterns = [
    path('translated/', views.translated, name="translated"),
    path('original/', views.original, name="original"),
    path('ascii_make/', views.ascii_make, name="ascii_make"),
    path('ascii_new/', views.ascii_new, name="ascii_new"),
    path('today/', views.today, name="today"),
    path('imagepick/', views.imagepick, name="imagepick"),
    path('graduation/', views.graduation, name="graduation"),
    path('bye/', views.bye, name="bye"),
    path('', views.index, name='index'),
]