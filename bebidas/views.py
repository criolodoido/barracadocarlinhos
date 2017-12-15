from django.shortcuts import render, get_object_or_404
from .models import Bebidas
from django.utils import timezone

def bebidas(request):
	objetos = Bebidas.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'bebidas/bebidas.html', {'objetos': objetos})
# Create your views here.

def post_detail(request, pk):
    objeto = get_object_or_404(Bebidas, pk=pk)
    Bebidas.objects.get(pk=pk)
    return render(request, 'bebidas/post_detail.html', {'objeto': objeto})
