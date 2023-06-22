from django.db import models

class Order(models.Model):
    quantity = models.PositiveIntegerField()
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()