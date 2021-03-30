""" apps/products/views_disks.py """

import os

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

    # Charges:
    charges = Charge.objects.filter(product=disk)
    total_charges = 0
    for index, charge in enumerate(charges):
        total_charges += charge.amount
    cost = (total_charges / disk.circulation) if disk.circulation else 0
    theorical_price = (cost * disk.coefficient) if disk.coefficient else 0

    # Barcode:
    if disk.ean:
        if not os.path.exists('{}.png'.format(disk.ean)):
            # Create the png:
            os.system(
                "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o static/img/barcodes/barcode.svg; \
                convert static/img/barcodes/barcode.svg -transparent '#FFFFFF' -trim static/img/barcodes/{0}.png; \
                rm static/img/barcodes/*.svg"
                .format(disk.ean)
            )

    return render(
        request,
        'products/disks/details.html',
        {
            'disk': disk,
            'charges': charges,
            'total_charges': total_charges,
            'cost': '{:.2f}'.format(cost),
            'theorical_price': '{:.2f}'.format(theorical_price),
            'visual_path': '/img/visuals/{}.jpg'.format(disk.ref_tm),
            'barcode_path': '/img/barcodes/{}.png'.format(disk.ean),
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
