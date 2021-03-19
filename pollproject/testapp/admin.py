from django.contrib import admin
from testapp.models import Poll

class PollAdmin(admin.ModelAdmin):
    list_display=['question','option_one','option_two','option_three','option_one_count','option_two_count','option_three_count','id']
# Register your models here.
admin.site.register(Poll,PollAdmin)
