#from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Cupom

def cupom(request):
	objetos = Cupom.objects.filter(validade__gt=timezone.now())
	return render(request, 'cupom/cupom.html', {'objetos': objetos})


def post_detail(request, pk):
    objeto = get_object_or_404(Cupom, pk=pk)
    Cupom.objects.get(pk=pk)
    return render(request, 'cupom/post_detail.html', {'objeto': objeto})
