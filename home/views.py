from django.db.models import Q
from django.shortcuts import render,HttpResponse
from product.models import Product, ProductFeature, ProductImage, Category
from cart.cart import Cart
from django.views import View
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product.models import Product
from .models import slider,advimgage
from cart.models import Order, OrderItem




def home_and_cart_detail(request):
    cart = Cart(request)
    # دریافت مقدار CART_SESSION_ID از session
    cart_session_data = request.session.get('CART_SESSION_ID', {})

    # لیست برای ذخیره تمامی id ها و محصولات
    products_with_quantity = []

    # متغیر برای شمارش تعداد کل محصولات در سبد خرید
    total_items = 0

    # پیمایش در CART_SESSION_ID و جمع‌آوری id‌ها و مقادیر quantity
    for key, value in cart_session_data.items():
        if isinstance(value, dict) and 'id' in value:
            product = Product.objects.get(id=value['id'])
            quantity = value['quantity']
            products_with_quantity.append({
                'product': product,
                'color': request.POST.get("color"),  # از داده‌های POST ارسال شده استفاده می‌کند
                'quantity': quantity,
                'majmoo': int(quantity) * int(product.price),
            })
            # اضافه کردن تعداد محصولات به شمارشگر
            total_items += int(quantity)

    # محاسبه مجموع قیمت‌ها
    total = cart.total()

    # ساختن context برای ارسال به تمپلیت
    context = {
        "slider": slider.objects.all(),
        "advimage": advimgage.objects.first(),
        "product": Product.objects.all(),
        "products_with_quantity": products_with_quantity,
        "total": total,
        "total_items": total_items,  # تعداد کل محصولات در سبد خرید
    }

    # بازگشت به همراه رندر تمپلیت و ارسال context
    return render(request, "index.html", context)








def remove_from_cart(request, product_id):
    cart = Cart(request)
    try:
        product = Product.objects.get(id=product_id)
        # حذف محصول از سبد خرید
        cart.delete(product_id=product.id, product_name=product.title_en)
    except Product.DoesNotExist:
        pass

    # پس از حذف محصول، کاربر را به صفحه اصلی یا صفحه سبد خرید هدایت می‌کنیم
    return redirect('home:home')


def product_search(request):
    query = request.GET.get('search-input')  # گرفتن عبارت جستجو از فرم
    products = Product.objects.all()  # همه محصولات
    
    if query:
        products = products.filter(
            Q(title__icontains=query) |  # جستجو در عنوان محصول
            Q(title_en__icontains=query) |  # جستجو در عنوان انگلیسی
            Q(description__icontains=query) |  # جستجو در توضیحات
            Q(Category__title__icontains=query) |  # جستجو در عنوان دسته‌بندی‌ها
            Q(color__title__icontains=query)  # جستجو در عنوان رنگ‌ها
        ).distinct()

    return render(request, 'search.html', {'products': products})



