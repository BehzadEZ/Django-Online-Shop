from django.contrib import admin
from django.urls import path
from . import  views


from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path("", views.user_profile_and_cart_detail, name="profile"),
    path("address/", views.user_address, name="address"),
    path("edit_address/", views.edit_address, name="edit_address"),
    path("orders/", views.user_orders, name="orders"), 
    path('save-address/', views.save_address, name='save_address'),
]
