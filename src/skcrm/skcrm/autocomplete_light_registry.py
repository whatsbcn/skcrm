#encoding: utf8
import autocomplete_light

from models import Country, Region, City, Sector, Section, Person, Company, Ot

autocomplete_light.register(Country, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre del pais ..'})
autocomplete_light.register(Region, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la provincia ..'})
autocomplete_light.register(City, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la ciudad ..'})
autocomplete_light.register(Sector, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre del setcor ..'})
autocomplete_light.register(Section, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la seccion ..'})
autocomplete_light.register(Person, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la persona ..'})
autocomplete_light.register(Company, search_fields=('name',),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de la empresa ..'})
autocomplete_light.register(Ot, search_fields=('name', 'number'),
    autocomplete_js_attributes={'minimum_characters': 0, 'placeholder': 'Nombre de ot ..'})


class ProviderAutocomplete(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'placeholder': 'Número o nombre proveedor ..', 'minimum_characters': 0,}

    def choices_for_request(self):
        q = self.request.GET.get('q', '')

        choices = self.choices.all().filter(types=1)
        if q:
            choices = choices.filter(number__icontains=q)
            if len(choices) == 0:
                choices = choices.filter(name__icontains=q)

        return self.order_choices(choices)[0:self.limit_choices]
    
autocomplete_light.registry.register(Company, ProviderAutocomplete)



#autocomplete_light.register(City, AutocompleteCity)
#autocomplete_light.registry.register(Country)
#autocomplete_light.registry.register(Region)
#autocomplete_light.registry.register(City)
#autocomplete_light.registry.register(Sector)
#autocomplete_light.registry.register(Section)
#autocomplete_light.registry.register(Person)
#autocomplete_light.registry.register(Company)


