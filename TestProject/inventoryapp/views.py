from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from inventoryapp.forms import ProductForm
from inventoryapp.models import Product
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.

def home(request):
    qs = Product.objects.all() # [{ }, {} ]
    context = {'base' : qs}
    return render(request, 'inventoryapp/base.html', context ) # HttpResponse

def listOfProducts(request):
    qs = Product.objects.all() # [{ }, {} ]
    context = {'inventory_list' : qs}
    return render(request, 'inventoryapp/inventory_list.html', context ) # HttpResponse


def listOfProductsdetail(request):
    qs = Product.objects.all() # [{ }, {} ]
   
    context = {'inventory_list' : qs}
    return render(request, 'inventoryapp/inventory_detail.html', context ) # HttpResponse

class ProductDetail(DetailView): # int is url - pk / slug
    model = Product
    template_name =  'inventoryapp/inventory_detail.html'
    # context_object_name = 'product' # object

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventoryapp/inventory_create.html'
    success_url = '/productsdetail' 
    context_object_name = 'form'

def productcreate(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'inventoryapp/inventory_create.html', {'form': form}) # form with data?
    else: # post
        form = ProductForm(request.POST) # ModelForm# Form
        if form.is_valid():
            form.save()
            # return HttpResponse('Product is added')
            return HttpResponseRedirect(reverse_lazy('inventoryapp:inventory_list'))
        else:
            return render(request,'inventoryapp/inventory_create.html', { 'form': form})

class ListOfProducts(ListView):
    print(ListView)
    model = Product
    template_name = 'inventoryapp/inventory_detail.html'

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventoryapp/inventory_update.html'
    context_object_name = 'form'
    success_url = reverse_lazy('inventoryapp:inventory_list')

def productupdate(request, product_id):
    product = get_object_or_404(Product, pk=product_id) # record from DB
    form = ProductForm(request.POST or None, instance=product)
    if request.method=='GET':
        return render(request, 'inventoryapp/inventory_update.html', {'form':form})
    else:
        if form.is_valid():
            form.save()
            return HttpResponse('Product has been updated')
        else:
            render(request, 'inventoryapp/inventory_update.html', {'form': form})

class ProductDeleteView(DeleteView):                                                         # view class to delete product
    template_name = "inventoryapp/inventory_delete.html"                                                 # 'inventory_delete.html' used as the template
    success_message = "Product has been deleted successfully"                             # displays message when form is submitted
    
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'object' : product})

    def post(self, request, pk):  
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        product.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventoryapp:inventory_list')

class ProductDelete(DeleteView):
    # success_url = reverse_lazy('inventoryapp:inventory_list')
    pass

