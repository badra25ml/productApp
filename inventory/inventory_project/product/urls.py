from django.urls import path, include
from product.views import listOfProducts
from product.views import listOfProductsdetail


urlpatterns = [
    path('', listOfProducts),
    path('1/', listOfProductsdetail),
]