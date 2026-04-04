from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def details1(request):
    # return HttpResponse("Hello, World! I'll fuck you")
    return render(request, 'post.html')
# Create your views here.

def details2(request):
    data=Post.objects.all()
    return render(request, 'home.html', {'data': data})