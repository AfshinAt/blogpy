from django.shortcuts import render

# Create your views here.

def home(requst):
    return render(requst, template_name='base.html')