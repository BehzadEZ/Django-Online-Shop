from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home_and_cart_detail, name="home"),  # مسیر صفحه اصلی
    path("remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    path('search/', views.product_search, name='search'),  # مسیر برای جستجو
]
