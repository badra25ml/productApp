from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from inventoryapp.forms import ProductForm
from inventoryapp.models import Product
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView

# Create your views here.



def listOfProducts(request):
    qs = Product.objects.all() # [{ }, {} ]
    context = {'inventory_list' : qs}
    return render(request, 'inventoryapp/inventory_list.html', context ) # HttpResponse

def listOfProductsdetail(request):
    return HttpResponse('This is one specific')

class ProductDetail(DetailView): # int is url - pk / slug
    model = Product
    template_name =  'inventoryapp/inventory_detail.html'
    # context_object_name = 'blog' # object

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventoryapp/inventory_create.html'
    context_object_name = 'form'

class ListOfProducts(ListView):
    model = Product
    template_name = 'inventoryapp/inventory_list.html'

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventoryapp/inventory_update.html'
    context_object_name = 'form'
    # success_url = reverse_lazy('blogapp:blog_list')

class ProductDelete(DeleteView):
    # success_url = reverse_lazy('blogapp:blog_list')
    pass

