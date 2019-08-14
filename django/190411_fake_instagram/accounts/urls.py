from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('password/', views.password, name='password'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
