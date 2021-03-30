""" apps/products/views_images.py """

import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Product


def images_list(request):
    """ List of images. """
    images = Product.objects.filter(category='image').order_by(
        'ref_tm', 'ean', 'recto_img', 'verso_img')
    return render(
        request,
        'products/images/list.html',
        {
            'images': images
        }
    )


@login_required
def image_create(request):
    """ Create a image. """
    return render(request, 'products/images/form.html')


def image_details(request, **kwargs):
    """ Details of an image. """
    image = get_object_or_404(Product, pk=kwargs['pk'])

    # Barcode:
    if image.ean:
        if not os.path.exists('{}.png'.format(image.ean)):
            # Create the png:
            os.system(
                "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o static/img/barcodes/barcode.svg; \
                convert static/img/barcodes/barcode.svg -transparent '#FFFFFF' -trim static/img/barcodes/{0}.png; \
                rm static/img/barcodes/*.svg"
                .format(image.ean)
            )

    return render(
        request,
        'products/images/details.html',
        {
            'image': image,
            'visual_path': '/img/visuals/{}.jpg'.format(image.ref_tm),
            'barcode_path': '/img/barcodes/{}.png'.format(image.ean),
        },
    )


@login_required
def image_update(request, **kwargs):
    """ Update a image. """
    image = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'products/images/form.html', {'image': image})


@login_required
def image_delete(request, **kwargs):
    """ Delete a image. """
    image = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'products/images/delete.html', {'image': image})
