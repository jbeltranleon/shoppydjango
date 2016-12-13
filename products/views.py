from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Product

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

def snapchat(request):
    glasses = Product.objects.filter(id = 1)
    template = loader.get_template('snapchat.html')
    title = 'Snap'
    context = {
        'glasses' : glasses,
        'title' : title
    }
    return HttpResponse(template.render(context, request))
