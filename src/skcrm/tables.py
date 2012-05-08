# coding: utf8
import django_tables2 as tables
from skcrm.models import Person 
#from django.utils.safestring import mark_safe
      
        
class PersonaTable(tables.Table):
    #name = tables.Column(verbose_name='Nombre')
    #cognom1 = tables.Column(verbose_name='Primer Apellido')
    #cognom2 = tables.Column(verbose_name='Segundo Apellido')   
    #email = tables.EmailColumn(verbose_name='Email')
    #city = tables.Column(verbose_name='Ciudad')  
    class Meta:
        attrs = {'class': 'paleblue'}
        order_by = 'name'
        model = Person