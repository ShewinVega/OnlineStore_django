from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Orders

# Register your models here.

class AdminOrders(admin.ModelAdmin):
    list_display = ('number','date','delivered')
    list_filter = ('date',)
    date_hierarchy = 'date'

admin.site.register(Orders,AdminOrders)