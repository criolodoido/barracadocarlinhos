#from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Porcao

def porcao(request):
	objetos = Porcao.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'porcoes/porcoes.html', {'objetos': objetos})
# Create your views here.

def post_detail(request, pk):
    objeto = get_object_or_404(Porcao, pk=pk)
    Porcao.objects.get(pk=pk)
    return render(request, 'porcoes/post_detail.html', {'objeto': objeto})
