""" apps/products/views_images.py """

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
    return render(
        request,
        'products/images/details.html',
        {
            'image': image,
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
