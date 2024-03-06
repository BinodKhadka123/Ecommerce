from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django import forms

from .forms import ProductForm


from .models import *

class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request,'ecomapps/base.html')

   


class ProductList(ListView):
    model = Product
    context_object_name = 'list'
    template_name = 'ecomapps/product_list.html'
    
    

class ProductDetail(DetailView):
    model = Product
    template_name='ecomapps/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "ecomapps/create_product.html"
    success_url = reverse_lazy('ecomapps:list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product_update.html"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "Product_delete.html"

class ProductPriceList(ListView):
    model = Product
    template_name='ecomapps/product_price.html'
    queryset=Product.custom_objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = self.queryset
        return context
    def get_queryset(self):
        return super().get_queryset()
class CategoryList(ListView):
    model = Product
    template_name='ecomapps/category_list.html'
    context_object_name = 'list'

    queryset=Product.custom_objects.filter_by_category_name('laptop')


