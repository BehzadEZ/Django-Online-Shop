from django.db import models
# Create your models here.
from account.models import MyUser
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='orders', verbose_name='user')
    total_price = models.PositiveBigIntegerField(default=0, verbose_name='total_price')
    address = models.TextField(max_length=500, verbose_name='address')
    is_paid = models.BooleanField(default=False, verbose_name='is_paid')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    payment_method = models.CharField(max_length=100, verbose_name='payment_method', default='انتقال مستقیم بانکی')  # Add payment_method field

    def __str__(self):
        return self.user.phone

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items',verbose_name='order')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='items',verbose_name='product')
    size = models.CharField(max_length=100, verbose_name='size')
    color = models.CharField(max_length=100, verbose_name='color')
    quantity = models.PositiveBigIntegerField(verbose_name='quantity')
    price = models.PositiveBigIntegerField(verbose_name='price')


    def __str__(self):
        return self.order.user.phone


class DiscountCode(models.Model):
    name=models.CharField(max_length=100,unique=True,verbose_name="name")
    discount=models.PositiveSmallIntegerField(default=0,verbose_name="discount")
    quantity=models.PositiveSmallIntegerField(default=1,verbose_name="quantity")


    def __str__(self):
        return self.name







