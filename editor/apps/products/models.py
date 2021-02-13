""" apps/products/models.py """

from django.db import models


class Product(models.Model):
    """ Product model. """
    ean = models.CharField(
        max_length=13,
        db_column='EAN',
    )
    ref_tm = models.CharField(
        max_length=10,
        db_column='Ref_TM',
    )
    title = models.CharField(
        max_length=255,
        db_column='Titre',
    )
    sub_title = models.CharField(
        max_length=255,
        db_column='Sous_titre',
    )

    class Meta:
        managed = False
        db_table = 'Objets'

    def __str__(self):
        return '{}: {}'.format(self.ref_tm, self.title)
