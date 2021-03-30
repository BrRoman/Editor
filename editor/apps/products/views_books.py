""" apps/products/views_books.py """

import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import BookForm
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

    # Charges:
    charges = Charge.objects.filter(product=book)
    total_charges = 0
    for index, charge in enumerate(charges):
        total_charges += charge.amount
    cost = (total_charges / book.circulation) if book.circulation else 0
    theorical_price = (cost * book.coefficient) if book.coefficient else 0

    # Barcode:
    if book.ean:
        if not os.path.exists('{}.png'.format(book.ean)):
            # Create the png:
            os.system(
                "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o static/img/barcodes/barcode.svg; \
                convert static/img/barcodes/barcode.svg -transparent '#FFFFFF' -trim static/img/barcodes/{0}.png; \
                rm static/img/barcodes/*.svg"
                .format(book.ean)
            )

    return render(
        request,
        'products/books/details.html',
        {
            'book': book,
            'charges': charges,
            'total_charges': total_charges,
            'cost': '{:.2f}'.format(cost),
            'theorical_price': '{:.2f}'.format(theorical_price),
            'visual_path': '/img/visuals/{}.jpg'.format(book.ref_tm),
            'barcode_path': '/img/barcodes/{}.png'.format(book.ean),
        },
    )


@login_required
def book_update(request, **kwargs):
    """ Update a book. """
    book = Product.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'products:book_details',
                    kwargs={
                        'pk': book.pk,
                    }
                )
            )
        else:
            print('No valid')

    else:
        form = BookForm(instance=book)

    return render(
        request,
        'products/books/form.html',
        {
            'form': form,
            'book': book,
        }
    )


@login_required
def book_delete(request, **kwargs):
    """ Delete a book. """
    book = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'products/books/delete.html', {'book': book})
