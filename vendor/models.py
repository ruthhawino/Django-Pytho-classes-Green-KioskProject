from django.db import models

class Vendor(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=43)
    email=models.EmailField(max_length=30)
    user_name=models.CharField(max_length=32)
    Password=models.CharField(max_length=8)
    date_updated=models.DateTimeField(auto_now=True)
