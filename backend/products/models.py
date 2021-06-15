from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.CharField(max_length=200, blank=False)
    quantity = models.IntegerField(blank=True, null=True)
    image =models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)