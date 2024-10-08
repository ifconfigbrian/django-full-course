from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',{'posts':posts})

def post_page(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,'posts/post_page.html',{'post':post})

@login_required(login_url="/users/login/")
def post_new(request):
    return render(request, 'posts/post_new.html')
