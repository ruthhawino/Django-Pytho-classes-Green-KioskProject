from django.db import models


class Deliver(models.Model):
    recipient_name = models.CharField(max_length=100)
    address = models.TextField()
    delivery_date = models.DateField()
    is_delivered = models.BooleanField(default=False)