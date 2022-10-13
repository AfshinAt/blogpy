from django.shortcuts import render

from blog.views import sidbar_data


# Create your views here.

def home(request):


    sidbar = sidbar_data(request)

    return render(request, 'page/home.html', {'sidbar': sidbar})
