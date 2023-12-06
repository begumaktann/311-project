from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('geog/', views.geog, name='geog'),
    path('personal/', views.personal, name='personal'),
    path('financial/', views.financial, name='financial')
    # Add other URL patterns for other views as needed
]
