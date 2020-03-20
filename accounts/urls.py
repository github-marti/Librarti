from django.urls import path
from django.contrib.auth import views as auth_views
from books import views as book_views
from . import views

urlpatterns = [
    path('', book_views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name="register"),
]