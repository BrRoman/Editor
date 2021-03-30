""" apps/products/models.py """

from django.db import models


class Product(models.Model):
    """ Product model. """
    category = models.CharField(
        max_length=25,
        db_column='Categorie',
    )
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
    author = models.CharField(
        max_length=255,
        db_column='Auteur',
    )
    interpreter = models.ForeignKey(
        'Interpreter',
        null=True,
        on_delete=models.CASCADE,
        db_column='Interprete_CD',
    )
    collection = models.ForeignKey(
        'Collection',
        on_delete=models.CASCADE,
        db_column='Collection',
    )
    number_in_collection = models.IntegerField(
        db_column='Num_dans_collection',
    )
    circulation = models.IntegerField(
        db_column='Chiffre_tirage',
    )
    publication = models.DateField(
        db_column='Date_fin_tirage',
    )
    width = models.IntegerField(
        db_column='Largeur',
    )
    height = models.IntegerField(
        db_column='Hauteur',
    )
    number_of_pages = models.IntegerField(
        db_column='Nb_pages',
    )
    weight = models.IntegerField(
        db_column='Poids',
    )
    presentation_product = models.TextField(
        db_column='Pres_objet',
    )
    presentation_author = models.TextField(
        db_column='Pres_auteur',
    )
    strong_points = models.TextField(
        db_column='Points_forts',
    )
    target_audience = models.TextField(
        db_column='Public_vise',
    )
    price = models.FloatField(
        db_column='Prix_public',
    )
    coefficient = models.FloatField(
        db_column='Coefficient',
    )
    pght = models.FloatField(
        db_column='PGHT',
    )
    recto_img = models.CharField(
        max_length=255,
        db_column='Recto_img',
    )
    verso_img = models.CharField(
        max_length=255,
        db_column='Verso_img',
    )

    class Meta:
        managed = False
        db_table = 'Objets'

    def __str__(self):
        designation = ''
        if self.category == 'book':
            if self.ref_tm:
                designation += self.ref_tm
            if self.title:
                if self.ref_tm:
                    designation += ' - '
                designation += self.title
            if self.sub_title:
                if self.title:
                    designation += ' '
                designation += '({})'.format(self.sub_title)

        elif self.category == 'disk':
            if self.ref_tm:
                designation += self.ref_tm
            if self.title:
                if self.ref_tm:
                    designation += ' - '
                designation += self.title
            if self.interpreter:
                designation += ', par {}'.format(self.interpreter.name)

        elif self.category == 'image':
            if self.ref_tm:
                designation += self.ref_tm

        return designation


class Collection(models.Model):
    """ Collection model. """
    collection = models.CharField(
        max_length=255,
        db_column='Collection',
    )
    issn = models.CharField(
        max_length=10,
        db_column='ISSN',
    )

    class Meta:
        managed = False
        db_table = 'Collections'


class Interpreter(models.Model):
    """ Interpreter model. """
    name = models.CharField(
        max_length=50,
        db_column='Interprete',
    )

    class Meta:
        managed = False
        db_table = 'Interpretes_CD'


class Charge(models.Model):
    """ Charge model. """
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        db_column='ID_objet',
    )
    name = models.CharField(
        max_length=50,
        db_column='Charge'
    )
    amount = models.FloatField(
        db_column='Montant',
    )

    class Meta:
        managed = False
        db_table = 'Charges'
