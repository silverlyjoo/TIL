from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),# GET(edit) / POST(update)
    path('<int:board_pk>/delete/', views.delete, name='delete'), #POST(delete)
    path('<int:board_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'), # GET(new) / POST(create)
    path('', views.index, name='index'),
]
