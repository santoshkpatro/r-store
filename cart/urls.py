from django.urls import path

from . import views

urlpatterns = [
    path("add/<str:product_id>/", views.cart_add, name="cart-add")
]