from django.contrib import admin
from .models import Product, Category, Club

# Register your models here.
admin.site.register(Club)
admin.site.register(Product)
admin.site.register(Category)
