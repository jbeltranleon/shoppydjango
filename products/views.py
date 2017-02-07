from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .mixins import LoginRequiredMixin

from .models import Product
from .forms import ProductForm

# Create your views here.

@login_required()
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


class ProductList(ListView):
    model = Product

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product