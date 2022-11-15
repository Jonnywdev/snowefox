from django.contrib import admin
from .models import Product, Category, Club

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'club',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'sport',
    )


admin.site.register(Club, ClubAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
