from django.contrib import admin

# Register your models here.
from cart.models import OrderItem, Order, DiscountCode


class OrderItemAdmin(admin.StackedInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','total_price','is_paid','created']
    list_filter = ['is_paid','created']
    search_fields = ['user']
    inlines = [OrderItemAdmin]

@admin.register(DiscountCode)
class DicountCodeAdmin(admin.ModelAdmin):

    list_display = ['name','discount','quantity']
    list_filter = ['name']
    search_fields = ['name']


