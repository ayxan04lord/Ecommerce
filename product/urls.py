from django.contrib import admin
from django.urls import path    
from .views import *

urlpatterns = [
    path('', index),
    path('home', index, name='index'),
    path('allProducts', allProducts, name='allProducts'),
    path('product_detail', product_detail, name='product_detail'),
    path('register', register, name="register"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('product_list', product_list, name="product_list"),
    
]