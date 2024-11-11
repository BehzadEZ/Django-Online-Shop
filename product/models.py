from django.db import models

# Create your models here.
class Size(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return  self.title

class Color(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs', blank=True, null=True, verbose_name='include')
    title=models.CharField(max_length=30)
    
    def __str__(self):
        return  self.title

class Product(models.Model):
    title=models.CharField(max_length=150)
    title_en=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=0)
    discount=models.SmallIntegerField()
    image=models.ImageField(upload_to="media")
    size=models.ManyToManyField(Size,blank=True,null=True,related_name="products")
    color=models.ManyToManyField(Color,related_name="products")
    Category=models.ManyToManyField(Category,related_name="products")
    SpecialOffer  = models.BooleanField(default=False, verbose_name="پیشنهاد ویژه")

    def __str__(self):
        return self.title




class ProductFeature(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_feature")
    key=models.CharField(max_length=255,blank=True,null=True)
    value=models.CharField(max_length=255)

    def __str__(self):
        return  f"{self.product.title}-{self.value}"

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(upload_to="media/product_image")

    def __str__(self):
        return f"{self.product.title} Image"