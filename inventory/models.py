from django.db import models
from vendor.models import Vendor
from django.utils import timezone


class Product(models.Model):
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField()
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
