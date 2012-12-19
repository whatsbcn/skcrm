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

class SearchContactForm(forms.Form):
    CARREC_CHOICES = [('', '')]
    CARREC_CHOICES.extend([(c.id, c.name) for c in PositionTypes.objects.all()])
    
    SECTOR_CHOICES = [('', '')]
    for s in Sector.objects.all().order_by("name"):
        if s.parent == None:
            SECTOR_CHOICES.extend([(s.id, s.name)])
            SECTOR_CHOICES.extend([(c.id, "__" + c.name) for c in Sector.objects.filter(parent__id=s.id)])    
    CIUTAT_CHOICES = [('', '')]
    CIUTAT_CHOICES.extend([(c.id, c.name) for c in City.objects.all().distinct()])
    PROVINCIA_CHOICES = [('', '')]
    PROVINCIA_CHOICES.extend([(c.id, c.name) for c in Region.objects.all()])
    
    SECTION_CHOICES = [('', '')]
    for s in Section.objects.all().order_by("name"):
        if s.parent == None:
            SECTION_CHOICES.extend([(s.id, s.name)])
            SECTION_CHOICES.extend([(c.id, "__" + c.name) for c in Section.objects.filter(parent__id=s.id)])

    TIPO_MEDIOS_CHOICES = [('', '')]
    TIPO_MEDIOS_CHOICES.extend([(c.id, c.name) for c in MediaType.objects.all()])
        
    #SECTION_CHOICES.extend([(c.id, c.name) 
    #SECTION_CHOICES.extend([(c.id, "--" + c.name) for c in Section.objects.all().order_by("name") if c.parent != None])
    

    name = forms.CharField(required=False, label='Nombre o apellidos')   
    company = forms.CharField(required=False, label='Empresa')
    media = forms.CharField(required=False, label='Medio de comunicación')
    carrec = forms.IntegerField(required=False, label='Cargo', widget=forms.Select(choices=CARREC_CHOICES))
    mailing = forms.BooleanField(required=False, label='Aceptar Mailing', widget=forms.Select(choices=MAILING_CHOICES))
    withmail = forms.BooleanField(required=False, label='Solo contactos con mail', widget=forms.Select(choices=MAIL_REQUERIDO))
    sector = forms.IntegerField(required=False, label='Sector del medio de comunicación del contacto', widget=forms.Select(choices=SECTOR_CHOICES))
    tipo_medio = forms.IntegerField(required=False, label='Tipo del medio de comunicación del contacto', widget=forms.Select(choices=TIPO_MEDIOS_CHOICES))
    ciutat = forms.IntegerField(required=False, label='Ciudad del contacto', widget=forms.Select(choices=CIUTAT_CHOICES))
    provincia = forms.IntegerField(required=False,  label='Provincia del contacto',widget=forms.Select(choices=PROVINCIA_CHOICES))
    section = forms.IntegerField(required=False, label='Sección donde se encuentra el contacto', widget=forms.Select(choices=SECTION_CHOICES))

class SearchSectorForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')

class SearchCompanyForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')

class SearchMediaForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')
    
class SearchSectionForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')    

class AnyMesForm(forms.Form):
    mes = forms.IntegerField(required=True, widget=forms.Select(choices=MES_CHOICES))    
    any = forms.IntegerField(required=True, widget=forms.Select(choices=ANY_CHOICES))
    