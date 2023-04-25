from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Product
from .forms import ProductCreationForm


class ProductList(generic.ListView):
    context_object_name = 'products'
    template_name = 'product/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(active=True).order_by('-datetime_modified')


class ProductDetail(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product_detail.html'


class ProductCreate(generic.CreateView):
    model = Product
    form_class = ProductCreationForm
    context = 'form'
    template_name = 'product/product_create.html'


class ProductUpdate(generic.UpdateView):
    model = Product
    form_class = ProductCreationForm
    context_object_name = 'form'
    template_name = 'product/product_create.html'


class ProductDelete(generic.DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('products:product_list')


# def product_list(request):
#     products = Product.objects.filter(active=True).order_by('-datetime_modified')
#
#     context = {'products': products}
#     return render(request, 'product/product_list.html', context)

# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#
#     context = {'product': product}
#     return render(request, 'product/product_detail.html', context)

# def product_create(request):
#     if request.method == 'POST':
#         form = ProductCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('products:product_list')
#
#     else:
#         form = ProductCreationForm()
#
#     context = {'form': form}
#     return render(request, 'product/product_create.html', context)

# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     form = ProductCreationForm(request.POST or None, instance=product)
#     if form.is_valid():
#         form.save()
#         return redirect(product.get_absolute_url())
#
#     context = {'form': form}
#     return render(request, 'product/product_create.html', context)

# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.delete()
#         return redirect('products:product_list')
#
#     context = {'product': product}
#     return render(request, 'product/product_delete.html', context)
