from django.contrib import admin
from django.urls import path
from . import  views
app_name="account"

urlpatterns = [
    path("login", views.login,name="login"),
    path("logout", views.user_logout,name="logout"),
    path("register", views.user_register,name="register"),
    path("verifypass/<str:token>", views.verifycode,name="verifypass"),
]