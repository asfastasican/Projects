from django.contrib import admin
from testapp.models import City

class CityAdmin(admin.ModelAdmin):
    list_display=['name']
# Register your models here.

admin.site.register(City,CityAdmin)
