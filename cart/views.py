from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View

from cart.cart import Cart
from cart.models import Order, OrderItem, DiscountCode
from product.models import Product
from account.models import Address
from django.conf import settings
import requests
import json



#? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"


from django.http import JsonResponse
from .models import Order, OrderItem, Product
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 1)
        
        # دریافت یا ایجاد سفارش جدید برای کاربر
        order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
        
        # پیدا کردن محصول و ایجاد یا بروزرسانی OrderItem
        product = Product.objects.get(id=product_id)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        order_item.quantity += int(quantity)
        order_item.price = product.price * order_item.quantity
        order_item.save()
        
        # بروزرسانی قیمت کل سفارش
        order.total_price = sum(item.price for item in order.items.all())
        order.save()

        # آماده کردن داده‌های JSON برای برگرداندن به AJAX
        response_data = {
            'success': True,
            'total_price': order.total_price,
            'item_count': order.items.count(),
            'item_name': product.name,
            'item_price': order_item.price,
            'item_image_url': product.image.url  # فرض بر این است که تصویر محصول موجود است
        }

        return JsonResponse(response_data)

    return JsonResponse({'success': False})



class CartAddView(View):
    def post(self, request, pk):

        price = request.POST.get("price")
        quantity = int(request.POST.get("quantity"))
        color = request.POST.get("color")

        # پیدا کردن محصول با شناسه
        product = Product.objects.get(id=pk)

        # چاپ مقادیر در کنسول (برای تست)
        print(f"Price: {price}, Quantity: {quantity}, Color: {color}")
        print(product)

        cart=Cart(request)
        cart.add(product,quantity,color)

        return redirect("cart:cart_list")





def cart_detail_view(request):
    cart = Cart(request)
    # دریافت مقدار CART_SESSION_ID از session
    cart_session_data = request.session.get('CART_SESSION_ID', {})

    # دریافت آدرس برای کاربر وارد شده
    try:
        address = Address.objects.filter(user=request.user).first()  # Or use `.get()` if only one address is expected
    except Address.DoesNotExist:
        address = None  # یا می‌توانید یک مقدار پیش‌فرض تنظیم کنید

    # لیست برای ذخیره تمامی id ها و محصولات
    product_ids = []
    products_with_quantity = []
    total_items = 0  # شمارنده برای تعداد کل محصولات

    # پیمایش در CART_SESSION_ID و جمع‌آوری id‌ها و مقادیر quantity
    for key, value in cart_session_data.items():
        if isinstance(value, dict) and 'id' in value:
            print("Product color", request.POST.get("color"))
            product_ids.append(value['id'])

            # دریافت محصول و محاسبه مجموع قیمت
            product = Product.objects.get(id=value['id'])
            quantity = value['quantity']
            majmoo = int(quantity) * int(product.price)

            products_with_quantity.append({
                'product': product,
                'color': request.POST.get("color"),
                'quantity': quantity,
                'majmoo': majmoo,
            })

            # به روز رسانی تعداد کل محصولات
            total_items += int(quantity)

    total = cart.total()

    # ایجاد context برای قالب
    context = {
        'products_with_quantity': products_with_quantity,
        'total': total,
        'total_items': total_items,  # تعداد کل محصولات
        "address": address.province if address else "No address available"
    }

    # رندر کردن قالب cart.html
    return render(request, "cart.html", context)





class OrderRequestView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            address = None
            print("Address not found")
        return render(request, "checkout.html", {"address": address})

    def post(self, request):
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone_number')
        address_text = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        description = request.POST.get('description')
        coupon_code = request.POST.get('coupon-code')

        # آپدیت یا ساخت آدرس جدید
        address, created = Address.objects.update_or_create(
            user=request.user,
            defaults={
                'full_name': full_name,
                'phone': phone,
                'address': address_text,
                'postal_code': postal_code,
                'description': description
            }
        )

        cart = Cart(request)

        try:
            discount = DiscountCode.objects.get(name=coupon_code)
            total_price_with_coupon = cart.total() - cart.total() * (discount.discount / 100)
            print(f"Total price with coupon: {total_price_with_coupon}")
        except DiscountCode.DoesNotExist:
            total_price_with_coupon = cart.total()
            print(f"Total price without coupon: {total_price_with_coupon}")

        # بررسی اینکه آیا سفارشی برای کاربر با وضعیت پرداخت نشده وجود دارد
        order, created = Order.objects.update_or_create(
            user=request.user,
            is_paid=False,  # فرض بر این است که فقط سفارشات پرداخت نشده را چک می‌کنیم
            defaults={
                'total_price': total_price_with_coupon,
                'address': address_text
            }
        )

        # اضافه کردن یا آپدیت کردن آیتم‌های سفارش
        for item in cart.cart.values():
            product = Product.objects.get(id=item['id'])

            print(f"Processing item: {product.title} with quantity {item['quantity']}")

            # بررسی اینکه آیا آیتم سفارشی با همین محصول و ویژگی‌ها وجود دارد یا خیر
            order_item, item_created = OrderItem.objects.update_or_create(
                order=order,
                product=product,
                defaults={
                    'size': item.get('size', 'none'),
                    'color': item.get('color', 'none'),
                    'quantity': item['quantity'],
                    'price': float(item['price'])  # استفاده از float به جای int

                }
            )

            if item_created:
                print(f"Order item created for product: {product.title}")
            else:
                print(f"Order item updated for product: {product.title}")

        # پاک کردن سبد خرید
        cart.session['CART_SESSION_ID'] = {}
        cart.session.modified = True

        print("Order and order items created or updated successfully")


        #return HttpResponse("doooooooooooooooooooooooooooooooonnnnnne")
        return redirect('cart:PayView', order.id)





from django.http import JsonResponse, HttpResponse
import requests
import json

class PayView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        CallbackURL = 'http://127.0.0.1:8000/cart/verify'
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": order.total_price,
            "Description": "وب سایت دانش شاپ",
            "Phone": order.user.phone,
            "CallbackURL": CallbackURL,
        }
        request.session['order_id'] = str(order.id)

        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}

        try:
            response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response_data = response.json()
                if response_data['Status'] == 100:
                    return JsonResponse({
                        'status': True,
                        'url': ZP_API_STARTPAY + str(response_data['Authority']),
                        'authority': response_data['Authority']
                    })
                else:
                    return JsonResponse({'status': False, 'code': str(response_data['Status'])})

            return HttpResponse(f"fail pay------> status code: {response.status_code}")

        except requests.exceptions.Timeout:
            return HttpResponse('time out in request')
        except requests.exceptions.ConnectionError:
            return HttpResponse('connection Error')
        except Exception as e:
            return HttpResponse(f"خطا در درگاه پرداخت: {str(e)}")

class verifyView(View):
    def get(self,request,):
        authority = request.GET.get('Authority')
        order_id = request.session.get('order_id')
        order=Order.objects.get(id=order_id)
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": order.total_price,
            "Authority": authority,
        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return HttpResponse (f"{response['RefID']} با تشکر از خرید شما -کد پیگیری شما : " )
            else:
                return  HttpResponse("پرداخت موفقیت آمیز نبود")
        return HttpResponse(response)


class cartdelete(View):
    def get(self, request, product_id):
        # Instantiate the Cart object
        cart = Cart(request)

        # Get the product using the product ID
        product = Product.objects.get(id=product_id)

        # Delete the product from the cart
        cart.delete(product_id, product.title_en)

        # Redirect back to the cart detail page
        return redirect('cart:cart_list')
