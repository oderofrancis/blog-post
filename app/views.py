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

import pandas as pd

def post_view(request):

    post = Post.objects.all()

    data = pd.read_csv('https://raw.githubusercontent.com/oderofrancis/suicide_data/main/master.csv')
    data = data.drop_duplicates(subset=['country'])
    data_names = data['country'].tolist()
    data_values = data['suicides/100k pop'].tolist()
    

    context = {
        'post':post,
        # 'data_names':data_names,
        # 'data_values':data_values,

        }
    return render(request,'post_view.html',context)