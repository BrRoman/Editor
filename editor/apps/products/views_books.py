""" apps/products/views_books.py """

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Charge, Product


def books_list(request):
    """ List of books. """
    books = Product.objects.filter(
        category='book').order_by('ref_tm', 'ean', 'title')
    return render(
        request,
        'products/books/list.html',
        {
            'books': books
        }
    )


@login_required
def book_create(request):
    """ Create a book. """
    return render(request, 'products/books/form.html')


def book_details(request, **kwargs):
    """ Details of a book. """
    book = get_object_or_404(Product, pk=kwargs['pk'])
    charges = Charge.objects.filter(product=book)
    return render(
        request,
        'products/books/details.html',
        {
            'book': book,
            'charges': charges,
        },
    )


@login_required
def book_update(request, **kwargs):
    """ Update a book. """
    book = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'products/books/form.html', {'book': book})


@login_required
def book_delete(request, **kwargs):
    """ Delete a book. """
    book = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'products/books/delete.html', {'book': book})
