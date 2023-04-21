from django.contrib import admin
from .models import Stone, ProductType, Product

admin.site.register(Product)
admin.site.register(Stone)
admin.site.register(ProductType)
