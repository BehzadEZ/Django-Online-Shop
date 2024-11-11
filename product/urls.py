from django.contrib import admin
from django.urls import path
from . import  views


app_name = "product"

urlpatterns = [
    path("detail/<int:pk>/", views.product_detail_view, name="product_detail"),
    path("list/", views.product_list_view, name="product_list"),
    path("list/category/<str:category_title>/", views.product_list_view, name="category_product_list"),
]
