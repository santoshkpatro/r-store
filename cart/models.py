from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_users")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_items")
    quantity = models.IntegerField(default=1)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        unique_together = ["user", "product"]

    @property
    def amount(self):
        return self.product.price * self.quantity