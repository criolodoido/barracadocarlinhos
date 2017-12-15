from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.pastel, name='pastel'),
	url(r'^pastel/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhepastel'),
	]