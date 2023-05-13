from django.shortcuts import render, redirect

from .models import Product, Category


def product_list(request):
    category_title = request.GET.get('category', None)

    products = Product.objects.filter(is_available=True)
    categories = Category.objects.filter(is_active=True)

    if category_title:
        category = Category.objects.get(title=category_title)
        products = products.filter(category=category)

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, "catalog/product_list.html", context)


def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug, is_available=True)

        context = {
            'product': product
        }

        return render(request, "catalog/product_detail.html", context)
    except Product.DoesNotExist:
        return redirect('product_list')