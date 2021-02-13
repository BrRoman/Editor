""" apps/products/urls.py """

from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.books_list, name='books_list'),
]
