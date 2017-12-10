from django.shortcuts import render
from django.utils import timezone
from .models import Pastel

def pastel(request):
	objetos = Pastel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'bebidas/bebidas.html', {'objetos': objetos})
# Create your views here.
