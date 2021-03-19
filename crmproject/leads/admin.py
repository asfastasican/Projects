from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_diaplay=['id']

class AgentAdmin(admin.ModelAdmin):
    list_diaplay=['id','User']

class LeadAdmin(admin.ModelAdmin):
    list_diaplay=['id','first_name','last_name','age']
# Register your models here.

admin.site.register(lead,LeadAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Agent,AgentAdmin)
