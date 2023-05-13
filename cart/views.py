from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Cart


@login_required(login_url="/accounts/login/")
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id, is_available=True)
    quantity = request.GET.get("quantity", 1)

    try:
        existing_cart = Cart.objects.get(user=request.user, product=product)
        existing_cart.quantity += int(quantity)
        existing_cart.save()
    except Cart.DoesNotExist:
        Cart.objects.create(user=request.user, quantity=quantity, product=product)

    return redirect('product_detail', slug=product.slug)
