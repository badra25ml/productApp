from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def listOfProducts(request):
    print(request.body)
    return HttpResponse("This is the product's page")

def listOfProductsdetail(request):
    return HttpResponse('This is one specific')

