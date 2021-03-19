from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer,Order,OrderItem,ShippingAddress,Product

class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','name','email']

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','product_description','image']

class OrderAdmin(admin.ModelAdmin):
    list_display=['customer','date_ordered','ordered']

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['product','date_added','quantity','order']

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=['customer','order','address','city','state','pincode','date_added']
# Register your models here.

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
