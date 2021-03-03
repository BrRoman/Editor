""" apps/products/views_disks.py """

from django.shortcuts import get_object_or_404, render

from .models import Product


def disks_list(request):
    """ List of disks. """
    disks = Product.objects.filter(
        category='disk').order_by('ref_tm', 'ean', 'title')
    return render(
        request,
        'products/disks/disks_list.html',
        {
            'disks': disks
        }
    )


def disk_details(request, **kwargs):
    """ Details of a disk. """
    disk = get_object_or_404(Product, pk=kwargs['pk'])
    return render(
        request,
        'products/disks/disk_details.html',
        {
            'disk': disk,
        },
    )
