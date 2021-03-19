from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','pid','description','contents','image','id']

class DoctorAdmin(admin.ModelAdmin):
    list_display=['DoctorName','DLicense','HospitalName','Address','City','State','PinCode','Contactno','Email','id']

class MedicalAdmin(admin.ModelAdmin):
    list_display=['MownerName','MLicense','MedicalName','Address','City','State','PinCode','Contactno','Email','id']

class OrganizationAdmin(admin.ModelAdmin):
    list_display=['OwnerName','OLicense','OrgName','Address','City','State','PinCode','Contactno','Email','id']

class StocksAdmin(admin.ModelAdmin):
    list_display=['product','Maximum_quantity','current_quantity']

class SaleAdmin(admin.ModelAdmin):
    list_display=['product','quater1_sale','quater2_sale','quater3_sale','quater4_sale']

# Register your models here.

admin.site.register(Product,ProductAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Medical,MedicalAdmin)
admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Stocks,StocksAdmin)
admin.site.register(Sale,SaleAdmin)
