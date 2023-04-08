from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
