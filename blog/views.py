from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    category = Category.objects.all()

    return  render(request, 'list.html',{'posts': posts, 'category': category})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html',{'post': post})