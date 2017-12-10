from django.shortcuts import render
from django.utils import timezone
from .models import Porcao

def porcao(request):
	objetos = Porcao.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'porcoes/porcoes.html', {'objetos': objetos})
# Create your views here.
