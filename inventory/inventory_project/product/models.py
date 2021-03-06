from django.db import models
from numpy import product
from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model): # Please add Image Field here 
    # id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False) # make if float data
    description = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField(null=False)
    created_dat = models.DateField(default=timezone.now)
    
