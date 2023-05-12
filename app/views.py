from django.shortcuts import render,redirect
from .models import Blog,Post
from app.forms import PostForm

# Create your views here.

def home(request):
    blog = Blog.objects.all()
    blog_one = Blog.objects.get(id=1)

    context = {
        'blog':blog,
        'blog_one':blog_one
        }
        
    return render(request,'home.html',context)


def post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_view')

    context = {
        'form':form
        }

    return render(request,'post.html',context)


def post_view(request):

    post = Post.objects.all()

    context = {
        'post':post
        }
    return render(request,'post_view.html',context)