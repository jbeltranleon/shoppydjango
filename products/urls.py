from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ProductList.as_view(), name='home'),
	url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), 
		name='detail'),
	url(r'^product/new', views.new_product, name='new_product')
]