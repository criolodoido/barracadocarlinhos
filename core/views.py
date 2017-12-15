from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def index(request):
	objetos = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'core/index.html', {'objetos': objetos})	

def post_detail(request, pk):
    objeto = get_object_or_404(Post, pk=pk)
    Post.objects.get(pk=pk)
    return render(request, 'core/post_detail.html', {'objeto': objeto})
