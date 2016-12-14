from django.contrib import admin
from .models import Product

# Register your models here.
# admin.site.register(Product)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price',)
    list_filter = ('category',)