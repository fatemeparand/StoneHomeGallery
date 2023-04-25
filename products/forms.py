from django import forms
from .models import Product


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_type',
            'stone',
            'product_material',
            'suitable_for',
            'product_color',
            'product_image',
            'price',
            'product_inventory',
            'product_owner',
            'active',
        ]
