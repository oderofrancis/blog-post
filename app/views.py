from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request):
    blog = Blog.objects.all()
    blog_one = Blog.objects.get(id=1)

    context = {
        'blog':blog,
        'blog_one':blog_one
        }
        
    return render(request,'home.html',context)