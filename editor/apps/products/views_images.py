""" apps/products/views_images.py """

from django.shortcuts import get_object_or_404, render

from .models import Product


def images_list(request):
    """ List of images. """
    images = Product.objects.filter(ref_tm__icontains='CP')
    return render(
        request,
        'products/images/images_list.html',
        {
            'images': images
        }
    )


def image_details(request, **kwargs):
    """ Details of an image. """
    image = get_object_or_404(Product, pk=kwargs['pk'])
    return render(
        request,
        'products/images/image_details.html',
        {
            'image': image,
        },
    )
