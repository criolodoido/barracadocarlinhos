from django.conf.urls import include, url 
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^porcoes/', include('porcoes.urls', namespace='porcoes')),
    url(r'^bebidas/', include('bebidas.urls', namespace='bebidas')),
    url(r'^pastel/', include('pastel.urls', namespace='pastel')),
    url(r'^coqueteis/', include('coqueteis.urls', namespace='coqueteis')),
    url(r'^cupom/', include('cupom.urls', namespace='cupom')),
]
