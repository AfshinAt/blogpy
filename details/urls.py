from django.urls import path
from details.views import home

app_name = 'details'

urlpatterns = [
    path('', home, name='home'),
]
