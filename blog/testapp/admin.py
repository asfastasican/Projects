from django.contrib import admin
from testapp.models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status','id']
    prepopulated_fields={'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=['post','name','email','body','created','updated','active']
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
