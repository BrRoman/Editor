""" apps/products/views.py """

from django.shortcuts import render


def home(request):
    """ Home view of products. """
    return render(request, 'products/home.html')
