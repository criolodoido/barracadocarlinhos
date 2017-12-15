from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.cupom, name='cupom'),
	url(r'^cupom/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhecupom'),
	]