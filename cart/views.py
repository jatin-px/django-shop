from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import CartItem

# Create your views here.
@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product')
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })


@login_required
def add_to_cart(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if product.quantity == 0:
        messages.error(request, f'"{product.name}" is out of stock.')
        return redirect('products:detail', pk=product_pk)

    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        new_qty = cart_item.quantity + 1
        if new_qty > product.quantity:
            messages.warning(request, f'Only {product.quantity} units available.')
        else:
            cart_item.quantity = new_qty
            cart_item.save()
            messages.success(request, f'"{product.name}" quantity updated in cart.')
    else:
        messages.success(request, f'"{product.name}" added to cart.')

    return redirect(request.META.get('HTTP_REFERER', 'products:all'))


@login_required
def remove_from_cart(request, item_pk):
    item = get_object_or_404(CartItem, pk=item_pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item removed from cart.')
    return redirect('cart:view')


@login_required
def update_cart(request, item_pk):
    item = get_object_or_404(CartItem, pk=item_pk, user=request.user)
    if request.method == 'POST':
        try:
            qty = int(request.POST.get('quantity', 1))
            if qty <= 0:
                item.delete()
                messages.info(request, 'Item removed from cart.')
            elif qty > item.product.quantity:
                messages.warning(request, f'Only {item.product.quantity} units available.')
            else:
                item.quantity = qty
                item.save()
                messages.success(request, 'Cart updated.')
        except ValueError:
            messages.error(request, 'Invalid quantity.')
    return redirect('cart:view')