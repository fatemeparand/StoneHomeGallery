from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.filter(active=True).order_by('-datetime_modified')

    context = {'products': products}
    return render(request, 'product/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


