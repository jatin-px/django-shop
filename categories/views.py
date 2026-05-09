from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.views import admin_required
from .models import Category, SubCategory
from .forms import CategoryForm, SubCategoryForm

# Create your views here.

# ─── Category Views ───────────────────────────────────────────────────────────

@login_required
def category_list(request):
    query = request.GET.get('q', '')
    categories = Category.objects.all()
    if query:
        categories = categories.filter(name__icontains=query)
    return render(request, 'categories/category_list.html', {
        'categories': categories,
        'query': query,
    })


@admin_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('categories:list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Add Category'})


@admin_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('categories:list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Edit Category', 'category': category})


@admin_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully.')
        return redirect('categories:list')
    return render(request, 'categories/confirm_delete.html', {'object': category, 'type': 'Category'})


# ─── SubCategory Views ────────────────────────────────────────────────────────

@login_required
def subcategory_list(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    query = request.GET.get('q', '')
    subcategories = SubCategory.objects.filter(category=category)
    if query:
        subcategories = subcategories.filter(name__icontains=query)
    return render(request, 'categories/subcategory_list.html', {
        'category': category,
        'subcategories': subcategories,
        'query': query,
    })


@admin_required
def add_subcategory(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategory added successfully.')
            return redirect('categories:list')
    else:
        category_pk = request.GET.get('category')
        initial = {'category': category_pk} if category_pk else {}
        form = SubCategoryForm(initial=initial)
    return render(request, 'categories/subcategory_form.html', {'form': form, 'title': 'Add Subcategory'})


@admin_required
def edit_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES, instance=subcategory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategory updated successfully.')
            return redirect('categories:subcategory_list', category_pk=subcategory.category.pk)
    else:
        form = SubCategoryForm(instance=subcategory)
    return render(request, 'categories/subcategory_form.html', {'form': form, 'title': 'Edit Subcategory', 'subcategory': subcategory})


@admin_required
def delete_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    category_pk = subcategory.category.pk
    if request.method == 'POST':
        subcategory.delete()
        messages.success(request, 'Subcategory deleted successfully.')
        return redirect('categories:subcategory_list', category_pk=category_pk)
    return render(request, 'categories/confirm_delete.html', {'object': subcategory, 'type': 'Subcategory'})