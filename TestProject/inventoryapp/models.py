from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

# Create your models here.

class Product(models.Model):
    # id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField(null=False) # make it float data # Done
    description = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField(null=False)
    created_dat = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='inventoryapp/', null=True, blank=True) # locations S3, local, network// media

# writer = models.# logged in
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse_lazy('inventoryapp:inventory_list')
    
