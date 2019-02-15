from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('mypage/', views.mypage, name="mypage"),
    path('qna/', views.qna, name="qna"),
    path('', views.index, name='index'),
    path('<str:not_found>/', views.notfound, name="notfound"),
]
