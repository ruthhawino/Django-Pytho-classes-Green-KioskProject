from django.db import models

class Cart(models.Model):
   item_id = models.AutoField(primary_key=True)
   item_name = models.CharField(max_length=50)
   price = models.DecimalField(max_digits=8,decimal_places=2)
   quantity = models.PositiveIntegerField()
   total_price = models.DecimalField(max_digits=8,decimal_places=2)
   date_added = models.DateField()
   product_image = models.ImageField()
