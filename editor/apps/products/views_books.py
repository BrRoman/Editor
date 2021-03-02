""" apps/products/views_books.py """

from django.shortcuts import get_object_or_404, render

from .models import Product


def books_list(request):
    """ List of books. """
    books = Product.objects.filter(ref_tm__icontains='L11')
    return render(
        request,
        'products/books/books_list.html',
        {
            'books': books
        }
    )


def book_details(request, **kwargs):
    """ Details of a book. """
    book = get_object_or_404(Product, pk=kwargs['pk'])
    return render(
        request,
        'products/books/book_details.html',
        {
            'book': book,
        },
    )
