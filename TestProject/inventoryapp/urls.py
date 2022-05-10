from django.urls import path, re_path, include
from django.views.generic import ListView, CreateView
from inventoryapp.forms import ProductForm
from inventoryapp.models import Product
from . import views

from inventoryapp.views import productcreate,listOfProducts, listOfProductsdetail, ListOfProducts, ProductCreate, ProductUpdate, ProductDelete, productupdate, ProductDeleteView




app_name = 'inventoryapp'
urlpatterns = [
    # re_path(r'^$', ListOfProducts.as_view(), name='inventory_list'),
    # path('create/', productcreate, name='inventory_create'),
    # path('delete/', ProductDeleteView.as_view(), name='delete'),
    
    # path('', listOfProducts),
    # path('1/', listOfProducts),
]