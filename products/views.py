from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Product
from .forms import ProductForm

# Create your views here.

def hello_world(request):
    products = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    title = 'Shoppy - Home'
    context = {
        'products' : products,
        'title' : title
    }
    return HttpResponse(template.render(context, request))


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = loader.get_template('product_detail.html')
    context = {
        'product' : product
    }
    return HttpResponse(template.render(context, request))

def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()
            product.save()
            return HttpResponseRedirect('/')
    else:  
        form = ProductForm()

    template = loader.get_template('new_product.html')
    title = 'Nuevo Producto'
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))