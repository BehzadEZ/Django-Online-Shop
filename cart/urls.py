from django.contrib import admin
from django.urls import path
from . import  views

app_name="cart"
urlpatterns = [
    path("/add/<int:pk>/", views.CartAddView.as_view(),name="add_to_cart"),
    path("/list", views.cart_detail_view,name="cart_list"),
    path("/order", views.OrderRequestView.as_view(),name="order"),
  #  path("pay/<int:order_id>/", views.PayView.as_view(), name="PayView"),
    path("/delete/<int:product_id>", views.cartdelete.as_view(),name="delete"),
    path('request/<int:order_id>/', views.PayView.as_view(), name='PayView'),
    path('verify/', views.verifyView.as_view(), name='verifyView'),

]