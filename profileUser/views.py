from django.shortcuts import render
from account.models import Address
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddressUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddressUserForm
from django.contrib import messages
from cart.models import Order
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
from cart.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render




@login_required
def user_profile_and_cart_detail(request):
    address = get_object_or_404(Address, user=request.user)
    avatar_url = address.avatar.url if address.avatar else None

    cart = Cart(request)
    cart_session_data = request.session.get('CART_SESSION_ID', {})
    products_with_quantity = []
    total_items = 0

    for key, value in cart_session_data.items():
        if isinstance(value, dict) and 'id' in value:
            product = Product.objects.filter(id=value['id']).first()
            if product:
                quantity = value['quantity']
                products_with_quantity.append({
                    'product': product,
                    'color': value.get("color"),  # تغییر این خط
                    'quantity': quantity,
                    'majmoo': int(quantity) * int(product.price),
                })
                total_items += int(quantity)

    total = cart.total()

    context = {
        'full_name': address.full_name,
        'phone': address.phone,
        'email': address.email,
        'membership_date': address.membership_date,
        'meli_code': address.meli_code,
        'avatar_url': avatar_url,
        "products_with_quantity": products_with_quantity,
        "total": total,
        "total_items": total_items,
    }

    return render(request, 'profile.html', context)







def user_address(request):
    # دریافت آدرس مربوط به کاربر وارد شده
    address = get_object_or_404(Address, user=request.user)
    avatar_url = address.avatar.url if address.avatar else None
    context = {
        'full_name': address.full_name,
        'phone': address.phone,
        'email': address.email,
        'membership_date': address.membership_date,
        'meli_code': address.meli_code,
        'address': address.address,
        'postal_code': address.postal_code,
        'avatar_url': avatar_url,
    }

    return render(request, 'profile-address.html', context)



@login_required
def edit_address(request):
    address, created = Address.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = AddressUserForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'آدرس شما با موفقیت به‌روزرسانی شد.')
            return redirect('profile:address')
        else:
            # بررسی خطاها در فرم
            print(form.errors)  # خطاهای فرم را در کنسول چاپ کنید

    else:
        form = AddressUserForm(instance=address)

    avatar_url = address.avatar.url if hasattr(address.avatar, 'url') else None

    context = {
        'form': form,
        'full_name': address.full_name,
        'avatar_url': avatar_url,
    }

    return render(request, 'profile-address(edit).html', context)


def user_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user).prefetch_related('items__product')  # پیش‌گیری از نداشته‌باشی
    address = get_object_or_404(Address, user=request.user)
    avatar_url = address.avatar.url if address.avatar else None
    context = {
        'orders': orders,
        'full_name': address.full_name,
        'phone': address.phone,
        'email': address.email,
        'membership_date': address.membership_date,
        'meli_code': address.meli_code,
        'avatar_url': avatar_url,
    }
    return render(request, 'profile-order-view.html', context)





def save_address(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # بررسی وجود آدرس قبلی برای کاربر
            if Address.objects.filter(user=request.user).exists():
                # اگر کاربر قبلاً آدرس وارد کرده باشد، فرم را با آدرس موجود پر کنید
                address = Address.objects.get(user=request.user)
                form = AddressUserForm(request.POST, instance=address)
            else:
                # اگر آدرسی وجود نداشته باشد، یک آدرس جدید ایجاد کنید
                form = AddressUserForm(request.POST)

            if form.is_valid():
                address = form.save(commit=False)
                address.user = request.user  # نسبت دادن کاربر
                address.save()
                return redirect('home:home')  # آدرس مورد نظر بعد از ذخیره
        else:
            # اگر کاربر وارد نشده است، او را به صفحه ورود هدایت کنید
            return redirect('home:home')
    else:
        if request.user.is_authenticated:
            # اگر کاربر وارد شده است و آدرسی وجود دارد، فرم را با مقادیر فعلی پر کنید
            existing_address = Address.objects.filter(user=request.user).first()
            form = AddressUserForm(instance=existing_address)
        else:
            form = AddressUserForm()

    return render(request, 'profile-personal-info.html', {'form': form})