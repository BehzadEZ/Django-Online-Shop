from itertools import product
from math import prod
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Product, ProductFeature, ProductImage, Category
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductFeature, ProductImage
from cart.cart import Cart
from urllib.parse import unquote


def product_detail_view(request, pk):
    # دریافت جزئیات محصول
    product = get_object_or_404(Product, pk=pk)
    product_feature = ProductFeature.objects.filter(product=product)
    gallery = ProductImage.objects.filter(product=product)
    # دریافت جزئیات سبد خرید
    cart = Cart(request)
    cart_session_data = request.session.get("CART_SESSION_ID", {})
    products_with_quantity = []
    total_items = 0

    for key, value in cart_session_data.items():
        if isinstance(value, dict) and "id" in value:
            product_in_cart = Product.objects.get(id=value["id"])
            quantity = value["quantity"]
            products_with_quantity.append(
                {
                    "product": product_in_cart,
                    "color": request.POST.get("color"),
                    "quantity": quantity,
                    "majmoo": int(quantity) * int(product_in_cart.price),
                }
            )
            total_items += int(quantity)

    total = cart.total()

    # ترکیب داده‌ها در کانتکست
    context = {
        "product": product,
        "product_feature": product_feature,
        "galery": gallery,
        "products_with_quantity": products_with_quantity,
        "total": total,
        "total_items": total_items,
    }
    return render(request, "single-product.html", context)






def product_list_view(request, category_title=None):
    # دی‌کد کردن category_title برای پشتیبانی از یونیکد
    if category_title:
        decoded_category_title = unquote(category_title)
        category = get_object_or_404(Category, title=decoded_category_title)
        products = Product.objects.filter(Category=category)
    else:
        products = Product.objects.all()

    # محاسبه قیمت پس از تخفیف در ویو
    for product in products:
        if product.discount:
            product.final_price = product.price - product.discount
        else:
            product.final_price = product.price

    # دریافت جزئیات سبد خرید
    cart = Cart(request)
    cart_session_data = request.session.get('CART_SESSION_ID', {})
    products_with_quantity = []
    total_items = 0

    for key, value in cart_session_data.items():
        if isinstance(value, dict) and 'id' in value:
            product_in_cart = Product.objects.get(id=value['id'])
            quantity = value['quantity']
            products_with_quantity.append({
                'product': product_in_cart,
                'color': request.POST.get("color"),
                'quantity': quantity,
                'majmoo': int(quantity) * int(product_in_cart.price),
            })
            total_items += int(quantity)

    total = cart.total()

    # ترکیب داده‌ها در کانتکست
    context = {
        'products': products,
        'products_with_quantity': products_with_quantity,
        'total': total,
        'total_items': total_items,
    }

    return render(request, "product-list.html", context)
