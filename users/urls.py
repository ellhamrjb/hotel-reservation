from django.urls import path
from .views import RegisterUserView, LoginView
from . import views

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
     path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
]
