""" apps/products/views_main.py """

from django.shortcuts import render


def home(request):
    """ Home view of products. """
    return render(request, 'products/home.html')
