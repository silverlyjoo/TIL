"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home/create/', views.user_create, name='create'),
    path('home/new/', views.user_new, name='new'),
    path('home/pong/', views.pong, name='pong'),
    path('home/ping/', views.ping, name='ping'),
    path('home/cube/<int:num>/', views.cube, name='cube'),
    path('home/hello/<str:name>/', views.hello, name='hello'),
    path('home/dinner/', views.dinner, name='dinner'),
    path('home/index/', views.index, name='index'),
    path('admin/', admin.site.urls),
]
