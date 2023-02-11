from django.contrib import admin
from .models import Customer,Account,Customer_Account_Details

# Register your models here.
admin.site.register(Customer),
admin.site.register(Account),
admin.site.register(Customer_Account_Details),