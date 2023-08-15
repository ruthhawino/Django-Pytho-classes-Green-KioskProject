from django.db import models
from customer.models import Customer
from orders.models import Order
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, default='USD')
    date = models.DateTimeField(auto_now=True)
    # method = models.CharField(max_length=10,default=)
    customer = models.ForeignKey(Customer,null=True ,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,null=True,on_delete=models.CASCADE)

    def customer_name(self):
        return self.customer.name

    def is_valid(self):
        if self.amount > 0 and self.currency and self.method and self.customer and self.order:
            return True
        else:
            return False
