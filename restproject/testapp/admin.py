from django.contrib import admin
from .models import Artical

class ArticalAdmin(admin.ModelAdmin):
    list_display=['title','author','email','date']
# Register your models here.
admin.site.register(Artical,ArticalAdmin)
