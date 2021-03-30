""" apps/products/forms.py """

from django import forms

from .models import Collection, Interpreter, Product


class BookForm(forms.ModelForm):
    """ Form for Book. """
    category = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'book',
            }
        )
    )
    ean = forms.CharField(
        required=False,
    )
    ref_tm = forms.CharField(
        required=False,
    )
    title = forms.CharField(
        required=False,
    )
    sub_title = forms.CharField(
        required=False,
    )
    author = forms.CharField(
        required=False,
    )
    collection = forms.ModelChoiceField(
        required=False,
        queryset=Collection.objects.all().order_by('name')
    )
    number_in_collection = forms.IntegerField(
        required=False,
    )
    presentation_product = forms.CharField(
        required=False,
        widget=forms.Textarea(),
    )
    presentation_author = forms.CharField(
        required=False,
    )
    strong_points = forms.CharField(
        required=False,
    )
    target_audience = forms.CharField(
        required=False,
    )
    number_of_pages = forms.IntegerField(
        required=False,
    )
    circulation = forms.IntegerField(
        required=False,
    )
    publication = forms.DateField(
        required=False,
    )
    width = forms.IntegerField(
        required=False,
    )
    height = forms.IntegerField(
        required=False,
    )
    weight = forms.IntegerField(
        required=False,
    )
    coefficient = forms.FloatField(
        required=False,
    )
    price = forms.FloatField(
        required=False,
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'title',
            'sub_title',
            'author',
            'collection',
            'number_in_collection',
            'presentation_product',
            'presentation_author',
            'strong_points',
            'target_audience',
            'number_of_pages',
            'circulation',
            'publication',
            'width',
            'height',
            'weight',
            'coefficient',
            'price',
        ]


class DiskForm(forms.ModelForm):
    """ Form for CD. """
    category = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'disk',
            }
        )
    )
    ean = forms.CharField(
        required=False,
    )
    ref_tm = forms.CharField(
        required=False,
    )
    title = forms.CharField(
        required=False,
    )
    sub_title = forms.CharField(
        required=False,
    )
    interpreter = forms.ModelChoiceField(
        required=False,
        queryset=Interpreter.objects.all().order_by('name')
    )
    circulation = forms.IntegerField(
        required=False,
    )
    publication = forms.DateField(
        required=False,
    )
    weight = forms.IntegerField(
        required=False,
    )
    coefficient = forms.FloatField(
        required=False,
    )
    pght = forms.FloatField(
        required=False,
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'title',
            'sub_title',
            'interpreter',
            'circulation',
            'publication',
            'weight',
            'coefficient',
            'pght',
        ]


class ImageForm(forms.ModelForm):
    """ Form for Image. """
    category = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'image',
            }
        )
    )
    ean = forms.CharField(
        required=False,
    )
    ref_tm = forms.CharField(
        required=False,
    )
    recto_img = forms.CharField(
        max_length=255,
        required=False,
    )
    verso_img = forms.CharField(
        required=False,
        max_length=255,
    )
    width = forms.IntegerField(
        required=False,
    )
    height = forms.IntegerField(
        required=False,
    )
    price = forms.FloatField(
        required=False,
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'recto_img',
            'verso_img',
            'width',
            'height',
            'price',
        ]
