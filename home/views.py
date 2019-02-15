from django.shortcuts import render, redirect
from .models import Category, Post
from .forms import PostForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    return render(request,'home.html',{"categories":categories,"posts":posts})

def post_by_category(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category=category_id)
    return render(request,'post_by_category.html',{"categories":categories,"posts":posts})

def post_detail(request, post_id):
    categories = Category.objects.all()
    post = Post.objects.get(pk=post_id)
    return render(request,'post_detail.html',{"categories":categories,"post":post})

def add_post(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {"categories":categories,'form': form})