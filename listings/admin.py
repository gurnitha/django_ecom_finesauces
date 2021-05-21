# listings/admin.py

# Django modules
from django.contrib import admin

# Local
from listings.models import Category, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)