from django.contrib import admin

# Register your models here.

from inventoryapp.models import Product

admin.site.register(Product)