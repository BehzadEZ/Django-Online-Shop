from random import randint
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from  django.contrib.auth import  authenticate,login,logout
from django.contrib import auth
from django.urls import reverse

from .forms import  UserLoginForm,UserRegisterForm
from cart.models import Order
from .models import  MyUser
# Create your views here.
#import ghasedakpack
import uuid
from  .models import  Otp
from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import UserRegisterForm
from .models import MyUser
import requests
import json
from django.conf import settings
from django.core.mail import send_mail



def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']

            try:
                # بررسی اینکه آیا کاربر با شماره تلفن وارد شده وجود دارد
                usercheck = MyUser.objects.get(phone=phone)

                if usercheck.is_active:
                    # احراز هویت کاربر
                    user = authenticate(request, username=phone, password=password)
                    
                    if user is not None:
                        # ورود به حساب کاربری
                        auth.login(request, user)
                        return redirect("/")
                    else:
                        # رمز عبور یا اطلاعات نادرست است
                        return render(request, "login.html", {
                            "message": "رمز عبور یا اطلاعات نادرست است", 
                            "form": form
                        })
                else:
                    # کاربر غیر فعال است
                    return render(request, "login.html", {
                        "message": "حساب کاربری شما فعال نمی‌باشد.", 
                        "form": form
                    })

            except MyUser.DoesNotExist:
                # کاربر با این شماره تلفن پیدا نشد
                return render(request, "login.html", {
                    "message": "حساب کاربری با این شماره تلفن یافت نشد.", 
                    "form": form
                })

    else:
        form = UserLoginForm()

    return render(request, "login.html", {"form": form})



def user_logout(request):
    auth.logout(request)
    return  redirect("/")








def user_register(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Extract form data
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("pass1")

            # Create a new user
            user = MyUser.objects.create_user(
                first_name=first_name, 
                last_name=last_name, 
                phone=phone, 
                email=email, 
                password=password
            )
            # user.is_active = False  # Deactivate user until verification
            user.is_active = True  
            user.save()

            # ************* Commented out SMS sending ***************
            # Generate token and random code for verification
            # token = str(uuid.uuid4())
            # rancode = randint(1000, 9999)

            # ************* Send SMS ***************
            # payload = json.dumps({
            #     "lineNumber": "90002930",
            #     "receptor": phone,
            #     "message": "کد فعال سازی شما: " + str(rancode),
            # })
            # url = "https://gateway.ghasedak.me/rest/api/v1/WebService/SendSingleSMS"
            # headers = {
            #     'Content-Type': 'application/json',
            #     'ApiKey': "140a3d5844333ad8773a1cd1c80b8158426b0d73e68834ef4162451380d7cb0a"
            # }
            # response = requests.post(url, headers=headers, data=payload)
            # ************* End SMS ***************

            # Save OTP to the database
            # Otp.objects.create(phone=phone, token=token, code=rancode)
            # print(rancode)
            # print(response.text)

            # Automatically log in the user
            auth.login(request, user)

            # Redirect without verification for now
            return redirect("profile:save_address")  # Change to your desired page
        else:
            print("Form errors:", form.errors)
            print("Form is not valid")
    else:
        form = UserRegisterForm()

    return render(request, "register.html", {'form': form})






def verifycode(request, token):
    if request.method == "POST":
        code = request.POST.get("code")

        try:
            # تلاش برای یافتن رکورد Otp با توکن و کد داده‌شده
            otp = Otp.objects.get(token=token, code=code)

            # یافتن کاربر مربوط به شماره تلفن
            user = MyUser.objects.get(phone=otp.phone)

            # فعال‌سازی حساب کاربری
            user.is_active = True
            user.save()

            # هدایت به صفحه‌ی موفقیت یا ورود
            return redirect("account:login")

        except Otp.DoesNotExist:
            # در صورتی که Otp یافت نشود، پیام خطا چاپ می‌شود
            print("Invalid code or token")
            # شما می‌توانید یک پیام خطا به قالب ارسال کنید
            return render(request, "verifypass.html", {"message": "کد وارد شده اشتباه است"})

    return render(request, "verifypass.html")