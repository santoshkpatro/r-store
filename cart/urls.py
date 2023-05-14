from django.urls import path

from . import views

urlpatterns = [
    path("", views.cart_index, name="cart_index"),
    path("add/<str:product_id>/", views.cart_add, name="cart_add"),
    path("delete/<str:item_id>/", views.cart_delete, name="cart_delete"),
]