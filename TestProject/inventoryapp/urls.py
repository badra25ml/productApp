from django.urls import path, re_path
from django.views.generic import ListView, CreateView
from inventoryapp.forms import ProductForm
from inventoryapp.models import Product

from inventoryapp.views import listOfProducts, listOfProductsdetail, ListOfProducts, ProductCreate, ProductUpdate, ProductDelete




app_name = 'inventoryapp'
urlpatterns = [
    re_path(r'^$', ListOfProducts.as_view(), name='inventory_list'),
    path('create/', ProductCreate.as_view(), name='inventory_create'),
    re_path(r'^(?P<pk>\d+)/update/$', ProductUpdate.as_view(), name='inventory_update'),
    # path('', listOfProducts),
    # path('1/', listOfProducts),
]