from django.urls import path, include

from blog.views import post_list, post_detail, category_list

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='list'),
    path('<int:id>/', post_detail, name='detail')
    path('category/<int:category_id>/', category_list, name='category_list')
]
