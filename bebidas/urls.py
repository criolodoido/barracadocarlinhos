from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.bebidas, name='bebidas'),
	url(r'^bebidas/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhebebidas'),
	]