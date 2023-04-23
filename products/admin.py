from django.contrib import admin
from .models import Stone, ProductType, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('product_name', 'stone', 'product_color', 'datetime_modified', 'active')
    ordering = ('-datetime_modified',)


admin.site.register(Stone)
admin.site.register(ProductType)

