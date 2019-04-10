from django.urls import path
from . import views

app_name = 'boards'


urlpatterns = [
    path('<int:board_pk>/comment_delete/<int:comment_pk>/', views.comment_delete, name="comment_delete"),
    path('<int:board_pk>/comment_create/', views.comment_create, name="comment_create"),
    path('<int:board_pk>/edit/', views.update, name="update"),
    path('<int:board_pk>/delete/', views.delete, name="delete"),
    path('<int:board_pk>/', views.detail, name="detail"),
    path('new/', views.create, name="create"),
    path('', views.index, name="index"),
]
