from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
# Create your views here.



def sidbar_data(request):
    caregory = Category.objects.all()
    popular_post = Post.objects.filter(status=1).order_by('-visit')[:3]

    context = {
        'caregory': caregory,
        'popular_post': popular_post
    }

    return context


def post_list(request):
    posts = Post.objects.filter(status=1)
    sidbar = sidbar_data(request)

    return  render(request, 'list.html',{'posts': posts, 'sidbar': sidbar})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.visit += 1
    post.save()

    sidbar = sidbar_data(request)

    return render(request, 'detail.html',{'post': post, 'sidbar': sidbar})

def category_list(request, category_id):
    posts = Post.objects.filter(status=1, category=category_id)
    sidbar = sidbar_data(request)
    category = get_object_or_404(Category, id=category_id)
    return  render(request, 'category.html',{'posts': posts, 'sidbar': sidbar, 'category': category})