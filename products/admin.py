from django.contrib import admin
from .models import Product
from .models import Favorite

# Register your models here.
# admin.site.register(Product)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price',)
    list_filter = ('category',)

@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)
