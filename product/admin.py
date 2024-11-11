from django.contrib import admin

# Register your models here.


from .models import Category,Product,Color,Size,ProductFeature,ProductImage




admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductFeature)
admin.site.register(ProductImage)

