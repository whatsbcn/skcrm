# coding: utf-8
from django import forms
from models import *

MES_CHOICES = (
    ('1', 'Gener'),
    ('2', 'Febrer'),
    ('3', 'Març'),
    ('4', 'Abril'),
    ('5', 'Maig'),
    ('6', 'Juny'),
    ('7', 'Juliol'),
    ('8', 'Agost'),
    ('9', 'Setembre'),
    ('10', 'Octubre'),
    ('11', 'Novembre'),
    ('12', 'Desembre'),
)

ANY_CHOICES = (
    ('2011', '2011'),
    ('2012', '2012'),
)

MAILING_CHOICES = (
    (None, ''),
    (True, 'Si'),
    (False, 'No'),
)

MAIL_REQUERIDO = (
    (False, 'No'),                  
    (True, 'Sí'),
)

class SearchForm(forms.Form):
    CARREC_CHOICES = [('', '')]
    CARREC_CHOICES.extend([(c.id, c.name) for c in PositionTypes.objects.all()])
    SECTOR_CHOICES = [('', '')]
    SECTOR_CHOICES.extend([(c.id, c.name) for c in Sector.objects.all()])
    CIUTAT_CHOICES = [('', '')]
    CIUTAT_CHOICES.extend([(c.id, c.name) for c in City.objects.all().distinct()])
    PROVINCIA_CHOICES = [('', '')]
    PROVINCIA_CHOICES.extend([(c.id, c.name) for c in Region.objects.all()])

    name = forms.CharField(required=False, label='Nombre o apellidos')   
    company = forms.CharField(required=False, label='Empresa')       
    carrec = forms.IntegerField(required=False, widget=forms.Select(choices=CARREC_CHOICES))
    mailing = forms.BooleanField(required=False, label='Acceptar Mailing', widget=forms.Select(choices=MAILING_CHOICES))
    withmail = forms.BooleanField(required=False, label='Solo contactos con mail', widget=forms.Select(choices=MAIL_REQUERIDO))
    sector = forms.IntegerField(required=False, widget=forms.Select(choices=SECTOR_CHOICES))
    ciutat = forms.IntegerField(required=False, widget=forms.Select(choices=CIUTAT_CHOICES))
    provincia = forms.IntegerField(required=False, widget=forms.Select(choices=PROVINCIA_CHOICES))

class SearchContactForm(forms.Form):
    CARREC_CHOICES = [('', '')]
    CARREC_CHOICES.extend([(c.id, c.name) for c in PositionTypes.objects.all()])
    SECTOR_CHOICES = [('', '')]
    SECTOR_CHOICES.extend([(c.id, c.name) for c in Sector.objects.all()])
    
    name = forms.CharField(required=False, label='Nombre y apellidos')   
    company = forms.CharField(required=False, label='Empresa')
    carrec = forms.IntegerField(required=False, widget=forms.Select(choices=CARREC_CHOICES), label='Cargo')
    #sector = forms.IntegerField(required=False, widget=forms.Select(choices=SECTOR_CHOICES))


class AnyMesForm(forms.Form):
    mes = forms.IntegerField(required=True, widget=forms.Select(choices=MES_CHOICES))    
    any = forms.IntegerField(required=True, widget=forms.Select(choices=ANY_CHOICES))
    