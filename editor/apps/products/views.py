""" apps/products/views.py """

from django.shortcuts import render

from .models import Product


def home(request):
    """ Home view of products. """
    return render(request, 'products/home.html')


def books_list(request):
    """ List of books. """
    books = Product.objects.filter(ref_tm__icontains='L11')
    return render(
        request,
        'products/books_list.html',
        {
            'books': books
        }
    )
