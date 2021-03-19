from django.contrib import admin
from testapp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
# Register your models here.


admin.site.register(Post,PostAdmin)
