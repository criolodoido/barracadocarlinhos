from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.porcao, name='porcao'),
	url(r'^porcoes/(?P<pk>[0-9]+)/$', views.post_detail, name='detalheporcoes'),
	]