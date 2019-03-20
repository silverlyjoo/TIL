from django.urls import path
from . import views

app_name = 'choice'


urlpatterns = [
    path('<int:question_pk>/answer_delete/<int:answer_pk>', views.answer_delete, name='answer_delete'),
    path('<int:question_pk>/new_answer/', views.new_answer, name='new_answer'),
    path('<int:question_pk>/delete/', views.delete, name='delete'),
    path('<int:question_pk>/edit/', views.edit, name='edit'),
    path('new/', views.new, name='new'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]