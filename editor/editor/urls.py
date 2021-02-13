""" editor/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('editor/', include('apps.products.urls')),
    path('editor/accounts/', include('apps.accounts.urls')),
    path('editor/admin/', admin.site.urls, name='admin'),
]
