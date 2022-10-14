from django.urls import path
from details.views import home, about, contact

app_name = 'details'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
