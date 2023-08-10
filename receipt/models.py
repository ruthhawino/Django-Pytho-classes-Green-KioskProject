from django.db import models

class Receipt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    transaction_id = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Receipt {self.id}"