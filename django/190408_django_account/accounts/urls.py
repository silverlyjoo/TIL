from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('<int:user_pk>/', views.profile, name="profile"),
    path('password/', views.change_password, name="change_password"),
    path('edit/', views.edit, name="edit"),
    path('delete/', views.delete, name="delete"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
]
