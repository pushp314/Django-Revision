from django.urls import path
from .views import *

# URL -> Routing for our application

urlpatterns = [
    path('',index, name='index'), # This is a route to the home page
    path('about/',about, name='about'), # This is a route to the about page
    path('contact/',contact, name='contact'), # This is a route to the contact page
]
