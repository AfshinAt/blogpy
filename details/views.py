from django.shortcuts import render
from blog.views import sidbar_data


def home(request):


    sidbar = sidbar_data(request)

    return render(request, 'page/home.html', {'sidbar': sidbar})


def about(request):


    sidbar = sidbar_data(request)

    return render(request, 'page/about.html', {'sidbar': sidbar})


def contact(request):


    sidbar = sidbar_data(request)

    return render(request, 'page/contact.html', {'sidbar': sidbar})