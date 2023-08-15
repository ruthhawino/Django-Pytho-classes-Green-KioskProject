from django.db import models

class Vendor(models.Model):
    # name = models.CharField(max_length=100)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=43)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=8)
    date_updated=models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.name