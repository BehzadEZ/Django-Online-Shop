
---

# Django Online Shop

Welcome to the **Django Online Shop**! This is a simple yet powerful e-commerce platform built with Django. It includes features like product management, user authentication, shopping cart functionality, and order management.

## Features
- **Product Catalog**: Browse and filter products by category.
- **Shopping Cart**: Add, remove, and manage items in the shopping cart.
- **User Authentication**: Sign-up, login, and manage user profiles.
- **Order Management**: Complete purchases and track orders.
- **Admin Panel**: Manage products, categories, and orders.
- **Responsive Design**: Optimized for desktop and mobile devices.

## Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.x
- pip (Python package installer)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-online-shop.git
cd django-online-shop
```

### 2. Create a Virtual Environment

To ensure that your project uses the correct dependencies, it's recommended to create a virtual environment.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

To install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Set Up the Database

Before running migrations, you need to create the migrations. Use the following command to do that:

```bash
python manage.py makemigrations
```

Then, to apply the migrations and set up the database, run:

```bash
python manage.py migrate
```

### 6. Create a Superuser

To access the admin panel, create an admin user:

```bash
python manage.py createsuperuser
```

Follow the instructions to set up your admin user credentials.

### 7. Run the Development Server

To start the server, run:

```bash
python manage.py runserver
```

You can now access the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Important Notes

- **Adding Products and Content**: To add products, sliders, and other content to the site, you will need to go to the Django admin panel and add them manually. Once logged in as an admin user, you can access the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and manage all the content.

- **The project may be incomplete**: Some parts of the project may be incomplete and need further improvement or fixes. We welcome contributions to help improve and complete the project.

---

## Contributing

Feel free to fork this repository, report issues, or submit pull requests to improve features and functionality.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---


---

---

# فروشگاه آنلاین با جنگو

به **فروشگاه آنلاین با جنگو** خوش آمدید! این یک پلتفرم تجارت الکترونیک ساده و قدرتمند است که با جنگو ساخته شده است. این پلتفرم شامل مدیریت محصولات، احراز هویت کاربران، عملکرد سبد خرید و مدیریت سفارشات است.

## ویژگی‌ها
- **کاتالوگ محصولات**: مرور و فیلتر محصولات بر اساس دسته‌بندی.
- **سبد خرید**: افزودن، حذف و مدیریت آیتم‌ها در سبد خرید.
- **احراز هویت کاربران**: ثبت‌نام، ورود و مدیریت پروفایل کاربری.
- **مدیریت سفارشات**: تکمیل خرید و پیگیری سفارشات.
- **پنل ادمین**: مدیریت محصولات، دسته‌بندی‌ها و سفارشات.
- **طراحی ریسپانسیو**: بهینه‌شده برای نمایش در دسکتاپ و دستگاه‌های موبایل.

## پیش‌نیازها

قبل از شروع، مطمئن شوید که موارد زیر را نصب کرده‌اید:
- Python 3.x
- pip (نصب‌کننده بسته‌های پایتون)

## راه‌اندازی

### 1. کلون کردن مخزن

```bash
git clone https://github.com/your-username/django-online-shop.git
cd django-online-shop
```

### 2. ایجاد محیط مجازی

برای اینکه پروژه شما از وابستگی‌های درست استفاده کند، بهتر است یک محیط مجازی بسازید.

```bash
python -m venv venv
```

### 3. فعال‌سازی محیط مجازی

- در **ویندوز**:
  ```bash
  venv\Scripts\activate
  ```

- در **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. نصب وابستگی‌ها

برای نصب پکیج‌های مورد نیاز از فایل `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. راه‌اندازی دیتابیس

قبل از اجرای مهاجرت‌ها، ابتدا باید مهاجرت‌ها را ایجاد کنید. برای این کار از دستور زیر استفاده کنید:

```bash
python manage.py makemigrations
```

سپس برای اعمال مهاجرت‌ها و راه‌اندازی دیتابیس، دستور زیر را اجرا کنید:

```bash
python manage.py migrate
```

### 6. ایجاد سوپرکاربر

برای دسترسی به پنل ادمین، یک کاربر ادمین ایجاد کنید:

```bash
python manage.py createsuperuser
```

دستورالعمل‌ها را دنبال کنید تا اطلاعات کاربری ادمین خود را وارد کنید.

### 7. اجرای سرور توسعه

برای شروع سرور، دستور زیر را اجرا کنید:

```bash
python manage.py runserver
```

حالا می‌توانید به سایت از آدرس [http://127.0.0.1:8000/](http://127.0.0.1:8000/) دسترسی پیدا کنید.

---

## نکات مهم

- **اضافه کردن محصولات و محتوا**: برای اضافه کردن محصولات، اسلایدرها و سایر محتواها به سایت، شما باید به پنل ادمین جنگو بروید و آنها را به صورت دستی اضافه کنید. پس از وارد شدن به عنوان کاربر ادمین، می‌توانید به پنل ادمین از آدرس [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) دسترسی پیدا کنید و تمامی محتواها را مدیریت کنید.

- **پروژه ممکن است برخی جاها ناقص باشد**: این پروژه ممکن است در برخی بخش‌ها ناقص باشد و نیاز به اصلاح یا بهبود داشته باشد. ما به شدت به مشارکت شما برای بهبود و کامل کردن پروژه خوش‌آمد می‌گوییم.

---

## مشارکت در پروژه

شما می‌توانید این مخزن را فورک کرده، مشکلات را گزارش کنید یا برای بهبود ویژگی‌ها و امکانات درخواست‌های کشش ارسال کنید.

## مجوز

این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر به `LICENSE` مراجعه کنید.

---
