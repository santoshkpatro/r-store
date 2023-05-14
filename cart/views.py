from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Item


@login_required(login_url="/accounts/login/")
def cart_index(request):
    user = request.user
    items = Item.objects.filter(user=user)

    total = 0
    for item in items:
        total += item.amount

    context = {"items": items, "total": total}
    return render(request, "cart/index.html", context)


@login_required(login_url="/accounts/login/")
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id, is_available=True)
    quantity = request.GET.get("quantity", 1)

    try:
        existing_item = Item.objects.get(user=request.user, product=product)
        existing_item.quantity += int(quantity)
        existing_item.save()
    except Item.DoesNotExist:
        Item.objects.create(user=request.user, quantity=quantity, product=product)

    return redirect("product_detail", slug=product.slug)


@login_required(login_url="/accounts/login/")
def cart_delete(request, item_id):
    try:
        item = Item.objects.get(id=item_id, user=request.user)
        item.delete()
    except Item.DoesNotExist:
        pass

    return redirect('cart_index')