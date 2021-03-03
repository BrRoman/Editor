""" apps/products/urls.py """

from django.urls import path

from . import views_main
from . import views_books
from . import views_disks
from . import views_images

app_name = 'products'
urlpatterns = [
    path('', views_main.home, name='home'),

    # Books:
    path('books/', views_books.books_list, name='books_list'),
    path('books/create/', views_books.book_create, name='book_create'),
    path('books/<int:pk>/', views_books.book_details, name='book_details'),
    path('books/<int:pk>/update/', views_books.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views_books.book_delete, name='book_delete'),

    # Disks:
    path('disks/', views_disks.disks_list, name='disks_list'),
    path('disk/<int:pk>/', views_disks.disk_details, name='disk_details'),

    # Images:
    path('images/', views_images.images_list, name='images_list'),
    path('image/<int:pk>/', views_images.image_details, name='image_details'),
]
