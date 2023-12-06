from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('login/', views.user_login, name='login'),  # Changed the view function name
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
