from django.urls import path, include
from product.views import listOfProducts
from product.views import listOfProductsdetail


urlpatterns = [
    path('', listOfProducts),
    path('1/', listOfProductsdetail),
] # I understand you still are working here. Add urls and views  to add. update and delete a product. Also create the Category Model and assiciate it with product.
