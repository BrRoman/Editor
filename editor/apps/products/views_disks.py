""" apps/products/views_disks.py """

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Charge, Product


def disks_list(request):
    """ List of disks. """
    disks = Product.objects.filter(
        category='disk').order_by('ref_tm', 'ean', 'title')
    return render(
        request,
        'products/disks/list.html',
        {
            'disks': disks
        }
    )


@login_required
def disk_create(request):
    """ Create a disk. """
    return render(request, 'products/disks/form.html')


def disk_details(request, **kwargs):
    """ Details of a disk. """
    disk = get_object_or_404(Product, pk=kwargs['pk'])
    charges = Charge.objects.filter(product=disk)
    total_charges = 0
    for index, charge in enumerate(charges):
        total_charges += charge.amount
    cost = (total_charges / disk.circulation) if disk.circulation != 0 else 0
    theorical_price = (cost * disk.coefficient) if disk.coefficient else 0
    return render(
        request,
        'products/disks/details.html',
        {
            'disk': disk,
            'charges': charges,
            'total_charges': total_charges,
            'cost': '{:.2f}'.format(cost),
            'theorical_price': '{:.2f}'.format(theorical_price),
        },
    )


@login_required
def disk_update(request, **kwargs):
    """ Update a disk. """
    disk = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'products/disks/form.html', {'disk': disk})


@login_required
def disk_delete(request, **kwargs):
    """ Delete a disk. """
    disk = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'products/disks/delete.html', {'disk': disk})
