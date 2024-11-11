from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

# models.py

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# models.py

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, phone, first_name, last_name, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not phone:
            raise ValueError("Users must have a phone number")

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, first_name, last_name, password=None):
        """
        Creates and saves a superuser with the given email, phone, first_name, last_name, and password.
        """
        user = self.create_user(
            email=email,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address (require)",
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    phone = models.CharField(max_length=12, unique=True, verbose_name="Phone Number")
    first_name = models.CharField(max_length=30, verbose_name="name", blank=True)
    last_name = models.CharField(max_length=30, verbose_name="family name", blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)


    objects = MyUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


class Otp(models.Model):
    token=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=11)
    code=models.SmallIntegerField()



class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='addresses', 
        verbose_name='کاربر'
    )
    email = models.EmailField(max_length=254, blank=True, null=True)  # null=True اضافه شد
    meli_code = models.CharField(max_length=10, unique=True, blank=True, null=True)  # null=True اضافه شد
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن')
    address = models.TextField(max_length=500, verbose_name='آدرس')
    postal_code = models.CharField(max_length=10, verbose_name='کد پستی', blank=True, null=True)  # max_length کاهش یافت
    description = models.TextField(null=True, blank=True)
    province = models.CharField(max_length=50, verbose_name='استان', blank=True)
    license_plate = models.CharField(max_length=20, verbose_name='پلاک', blank=True)
    city = models.CharField(max_length=100, verbose_name='شهر', blank=True)
    avatar = models.ImageField(upload_to="media", blank=True, null=True)  # آواتار ممکن است خالی باشد
    membership_date = models.DateField(auto_now_add=True, verbose_name='تاریخ عضویت', null=True)

    @property
    def full_name(self):
        return f"{self.user.first_name or ''} {self.user.last_name or ''}".strip()  # بررسی نام‌ها برای None

    def __str__(self):
        return self.full_name