from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.coqueteis, name='coqueteis'),
	url(r'^coqueteis/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhecoqueteis'),
	]