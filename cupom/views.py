from django.shortcuts import render
from django.utils import timezone
from .models import Cupom

def cupom(request):
	objetos = Cupom.objects.filter(validade__gt=timezone.now())
	return render(request, 'cupom/cupom.html', {'objetos': objetos})
# Create your views here.

#objetos = Cupom.objects.filter(published_date__lte=timezone.now()).order_by('published_date')