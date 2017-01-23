from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^login/$', views.authentication, name='authentication'),
	url(r'^registered/$', views.registered, name='registered'),
	url(r'^logout$', auth_views.logout, {'next_page': '/login'}, name='logout')
]