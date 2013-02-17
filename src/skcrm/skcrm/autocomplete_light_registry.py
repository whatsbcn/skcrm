#encoding: utf8
import autocomplete_light

from models import Country, Region, City, Sector, Section, Person, Company, Ot, ExpenseConceptType, ExpenseConceptSubType
from django.db.models import Q

class ExpenseConceptSubTypeAutocomplete(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de concepto ..'}
    search_fields=('name',)

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        concept_type_id = self.request.GET.get('concept_type_id', None)

        choices = self.choices.all()
        if q:
            choices = choices.filter(name__icontains=q)
        if concept_type_id:
            choices = choices.filter(concept_type_id=concept_type_id)

        return self.order_choices(choices)[0:self.limit_choices]

autocomplete_light.register(ExpenseConceptSubType, ExpenseConceptSubTypeAutocomplete)

class CityAutocomplete(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la ciudad ..'}
    search_fields=('name',)

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        region_id = self.request.GET.get('region_id', None)

        choices = self.choices.all()
        if q:
            choices = choices.filter(name__icontains=q)
        if region_id:
            choices = choices.filter(region_id=region_id)

        return self.order_choices(choices)[0:self.limit_choices]

autocomplete_light.register(City, CityAutocomplete)

class ProviderAutocomplete(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre del proveedor ..'}
    search_fields=('name',)

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        choices = self.choices.all().filter(type__name='Proveedor')
        if q:
            choices = choices.filter(Q(name__icontains=q)|Q(comercial_name__icontains=q))        
        return self.order_choices(choices)[0:self.limit_choices]

autocomplete_light.register(Company, ProviderAutocomplete)

class GroupAutocomplete(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de grupo ..'}
    search_fields=('name',)

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        choices = self.choices.all().filter(is_group=1)
        if q:
            choices = choices.filter(name__icontains=q)        
        return self.order_choices(choices)[0:self.limit_choices]

autocomplete_light.register(Company, GroupAutocomplete)

class SectorAutocomplete(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre del setcor ..'}
    search_fields=('name',)

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        choices = self.choices.all().filter(Q(name__icontains=q)|Q(parent__name__icontains=q)|Q(parent__parent__name__icontains=q))
        return self.order_choices(choices)[0:self.limit_choices]
    
autocomplete_light.register(Sector, SectorAutocomplete)

class SectionAutocomplete(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la seccion ..'}
    search_fields=('name',)

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        choices = self.choices.all().filter(Q(name__icontains=q)|Q(parent__name__icontains=q)|Q(parent__parent__name__icontains=q))
        return self.order_choices(choices)[0:self.limit_choices]
    
autocomplete_light.register(Section, SectionAutocomplete)


autocomplete_light.register(Country, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre del pais ..'})
autocomplete_light.register(Region, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la provincia ..'})
autocomplete_light.register(Person, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la persona ..'})
autocomplete_light.register(Company, search_fields=('name', 'comercial_name'),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la empresa ..'})
autocomplete_light.register(Ot, search_fields=('name', 'number', 'company__comercial_name'),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de ot ..'})
autocomplete_light.register(ExpenseConceptType, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de concepto ..'})


