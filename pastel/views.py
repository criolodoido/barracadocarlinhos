#from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Pastel

def pastel(request):
	objetos = Pastel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'pastel/pastel.html', {'objetos': objetos})

def post_detail(request, pk):
    objeto = get_object_or_404(Pastel, pk=pk)
    Pastel.objects.get(pk=pk)
    return render(request, 'pastel/post_detail.html', {'objeto': objeto})
