from django.db import models
from django.contrib.auth.models import User

from catalog.models import Product


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ("created", "Created"),
        ("processing", "Processing"),
        ("placed", "Placed"),
        ("cancelled", "Cancelled"),
    )

    ORDER_PAYMENT_STATUS_CHOICES = (
        ("initated", "Initiated"),
        ("processing", "Processing"),
        ("complete", "Complete"),
    )

    METHOD_CHOICES = (("cod", "Cash On Delivery"), ("online", "Online"))

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="orders", null=True
    )
    order_id = models.CharField(max_length=10)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(
        max_length=15, choices=ORDER_STATUS_CHOICES, default="created"
    )
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    payment_status = models.CharField(
        max_length=15, choices=ORDER_PAYMENT_STATUS_CHOICES, blank=True, null=True
    )
    payment_id = models.CharField(max_length=50, blank=True, null=True)
    order_placed_at = models.DateTimeField(blank=True, null=True)

    @property
    def total_amount(self):
        self.total_price - self.total_amount

    def __str__(self) -> str:
        return self.order_id


class OrderItem(models.CharField):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="product_items", null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)
