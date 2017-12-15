from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Coqueteis

def coqueteis(request):
	objetos = Coqueteis.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'bebidas/bebidas.html', {'objetos': objetos})
# Create your views here.

def post_detail(request, pk):
    objeto = get_object_or_404(Coqueteis, pk=pk)
    Coqueteis.objects.get(pk=pk)
    return render(request, 'coqueteis/post_detail.html', {'objeto': objeto})
