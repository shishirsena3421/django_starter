from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='app-home'),

    path('physics11/', views.physics11, name='physics11'),

    path('login/', views.login, name='login'),

    path('register/', views.handleSignUp, name='register'),
    
]


