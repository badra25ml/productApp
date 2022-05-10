"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import path, include
# import inventoryapp


from inventoryapp.views import productcreate, listOfProducts, ProductCreate, ProductUpdate, ProductDelete, listOfProductsdetail, ProductDetail, ListOfProducts, ProductDeleteView, productupdate

from TestProject import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventoryapp/',include('inventoryapp.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('1/', listOfProducts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


