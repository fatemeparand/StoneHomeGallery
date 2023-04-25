from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreationForm


def product_list(request):
    products = Product.objects.filter(active=True).order_by('-datetime_modified')

    context = {'products': products}
    return render(request, 'product/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


def product_create(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')

    else:
        form = ProductCreationForm()

    context = {'form': form}
    return render(request, 'product/product_create.html', context)
