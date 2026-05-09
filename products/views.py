from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.views import admin_required
from categories.models import SubCategory
from .models import Product
from .forms import ProductForm

# Create your views here.
@login_required
def product_list(request, subcategory_pk):
    subcategory = get_object_or_404(SubCategory, pk=subcategory_pk)
    query = request.GET.get('q', '')
    products = Product.objects.filter(category=subcategory)
    if query:
        products = products.filter(name__icontains=query)
    return render(request, 'products/product_list.html', {
        'subcategory': subcategory,
        'products': products,
        'query': query,
    })


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


@login_required
def all_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.select_related('category__category').all()
    if query:
        products = products.filter(name__icontains=query)
    return render(request, 'products/all_products.html', {
        'products': products,
        'query': query,
    })


@admin_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('products:all')
    else:
        subcategory_pk = request.GET.get('subcategory')
        initial = {'category': subcategory_pk} if subcategory_pk else {}
        form = ProductForm(initial=initial)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Add Product'})


@admin_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Edit Product', 'product': product})


@admin_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('products:all')
    return render(request, 'products/confirm_delete.html', {'object': product, 'type': 'Product'})


@admin_required
def update_stock(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        qty = request.POST.get('quantity', 0)
        try:
            product.quantity = max(0, int(qty))
            product.save()
            messages.success(request, f'Stock updated to {product.quantity} units.')
        except ValueError:
            messages.error(request, 'Invalid quantity value.')
    return redirect('products:detail', pk=pk)