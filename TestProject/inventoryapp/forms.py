from django.forms import ModelForm

from inventoryapp.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'quantity', 'created_date', 'image')