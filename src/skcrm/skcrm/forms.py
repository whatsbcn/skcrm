# coding: utf-8
from django import forms
#from django.forms.widgets import CheckboxSelectMultiple, CheckboxInput
from skcrm.models import *
#from autocomplete_light_registry import AutocompleteOt
import autocomplete_light
from skcrm.models import EXPENSE_STATE

EXPENSE_STATE_AND_EMPTY = [('','')] + EXPENSE_STATE

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
    mailing = forms.BooleanField(required=False, label='Contactos que aceptan mailing', widget=forms.CheckboxInput)
    withmail = forms.BooleanField(required=False, label='Contactos con mail', widget=forms.CheckboxInput)
    sector = forms.IntegerField(required=False, label='Sector del medio de comunicación del contacto', widget=forms.Select(choices=SECTOR_CHOICES))
    tipo_medio = forms.IntegerField(required=False, label='Tipo del medio de comunicación del contacto', widget=forms.Select(choices=TIPO_MEDIOS_CHOICES))
    region = forms.IntegerField(required=False,  label='Provincia del contacto',widget=autocomplete_light.ChoiceWidget('RegionAutocomplete'))    
    city = forms.IntegerField(required=False, label='Ciudad del contacto', widget=autocomplete_light.ChoiceWidget('CityAutocomplete'))
    section = forms.IntegerField(required=False, label='Sección donde se encuentra el contacto', widget=forms.Select(choices=SECTION_CHOICES))
    
class SearchPersonForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre o apellidos')

class SearchSectorForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')

class SearchCompanyForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')

class SearchMediaForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')
    
class SearchSectionForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')    

class SearchExpenseForm(forms.Form):
    filter = forms.CharField(required=False, label='Numero')    

class SearchExpenseConceptTypeForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')    

class SearchExpenseConceptSubTypeForm(forms.Form):
    name = forms.CharField(required=False, label='Nombre')    
    
    

class GastosPorOtrForm(forms.Form):
    fecha_inicio = forms.DateField(required=True, label="Fecha inicio")
    fecha_final = forms.DateField(required=True, label="Fecha final")
    ot = forms.ModelChoiceField(Ot.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('OtAutocomplete'), required=False)
#    content_type = forms.ModelChoiceField(ExpenseConceptType.objects.all(),
#                                  #widget=autocomplete_light.ChoiceWidget('ExpenseConceptTypeAutocomplete'),
#                                  required=False, label="Concepto")
    concept_type = forms.ModelChoiceField(ExpenseConceptType.objects.all(), widget=autocomplete_light.ChoiceWidget('ExpenseConceptTypeAutocomplete'), required=False, label="Concepto de gasto")
    concept_sub_type = forms.ModelChoiceField(ExpenseConceptSubType.objects.all(), widget=autocomplete_light.ChoiceWidget('ExpenseConceptSubTypeAutocomplete'), required=False, label="Subconcepto de gasto")
     
    def __init__(self, *args, **kwargs):
        super(GastosPorOtrForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget.attrs.update({'class': "input-small datepicker"})
        self.fields['fecha_final'].widget.attrs.update({'class': "input-small datepicker"})    

class GastosPorProveedorForm(forms.Form):
    fecha_inicio = forms.DateField(required=True, label="Fecha inicio")
    fecha_final = forms.DateField(required=True, label="Fecha final")
    proveedor = forms.ModelChoiceField(Company.objects.all().filter(type=1),
                                  widget=autocomplete_light.ChoiceWidget('CompanyProviderAutocomplete'), required=False)
    estado = forms.ChoiceField(choices=EXPENSE_STATE_AND_EMPTY, required=False)        
    def __init__(self, *args, **kwargs):
        super(GastosPorProveedorForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget.attrs.update({'class': "input-small datepicker"})
        self.fields['fecha_final'].widget.attrs.update({'class': "input-small datepicker"})
        self.fields['estado'].widget.attrs.update({'class': "input-medium"})    


class AnyMesForm(forms.Form):
    mes = forms.IntegerField(required=True, widget=forms.Select(choices=MES_CHOICES))    
    any = forms.IntegerField(required=True, widget=forms.Select(choices=ANY_CHOICES))

#from autocomplete_light_registry import AutocompleteCity
    
class CompanyForm(forms.ModelForm):
    in_group = forms.ModelChoiceField(Company.objects.all().filter(is_group=1),
                        widget=autocomplete_light.ChoiceWidget('CompanyGroupAutocomplete'), required=False)
    class Meta:
        #widgets = autocomplete_light.get_widgets_dict(Company)
        #city = forms.ModelChoiceField(City.objects.all(),
        #                              widget=autocomplete_light.ChoiceWidget(AutocompleteCity))
        fields = ('name', 'comercial_name', 'NIF_CIF', 'website', 'type', 'is_group', 'in_group', 'account_number')
        # , 'address', 'postal_code', 'country', 'region', 'city',
        model = Company
        exclude = ('relations',)

class MediaForm(forms.ModelForm):
    company = forms.ModelChoiceField(Company.objects.all(),
                        widget=autocomplete_light.ChoiceWidget('CompanyAutocomplete'), required=False)    
    class Meta:
        model = Media        
        widgets = autocomplete_light.get_widgets_dict(Media)
    def __init__(self, *args, **kwargs):
        super(MediaForm, self).__init__(*args, **kwargs)
        self.fields['sectors'].help_text = ''
        
    def clean_company(self):
        data = self.cleaned_data['company']
        if data == None:
            raise forms.ValidationError("Falta especificar la empresa a la que pertenece.")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data        
        
class CompanyContactDataForm(forms.ModelForm):
    class Meta:
        model = ContactData        
        widgets = autocomplete_light.get_widgets_dict(ContactData)
        exclude = ('person', 'company', 'media', 'position', 'type', 'packets_address', 'country')

class MediaContactDataForm(forms.ModelForm):
    class Meta:
        model = ContactData        
        widgets = autocomplete_light.get_widgets_dict(ContactData)
        exclude = ('person', 'company', 'media', 'position', 'type', 'packets_address', 'country')

class PersonContactDataForm(forms.ModelForm):
    
    class Meta:
        model = ContactData        
        widgets = autocomplete_light.get_widgets_dict(ContactData)
        exclude = ('person', 'type', 'country')
        
        
class OtForm(forms.ModelForm):
    class Meta:
        model = Ot   
        exclude = ('company',)

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section

class ExpenseConceptTypeForm(forms.ModelForm):
    class Meta:
        model = ExpenseConceptType

class ExpenseConceptSubTypeForm(forms.ModelForm):
    class Meta:
        model = ExpenseConceptSubType
        
class ExpenseForm(forms.ModelForm):
    provider = forms.ModelChoiceField(Company.objects.all(),
                        widget=autocomplete_light.ChoiceWidget('CompanyProviderAutocomplete'), required=False)    
    class Meta:
        widgets = autocomplete_light.get_widgets_dict(Expense)        
        model = Expense   
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': "input-small datepicker"})
        self.fields['payment_date'].widget.attrs.update({'class': "input-small datepicker"})
        self.fields['state'].widget.attrs.update({'class': "input-medium"})  

class ExpenseItemForm(forms.ModelForm):
#    content_type = forms.ModelChoiceField(ExpenseConceptType.objects.all(),
#                                  widget=autocomplete_light.ChoiceWidget('ExpenseConceptTypeAutocomplete'),
#                                  required=False, label="Concepto")
#    content_sub_type = forms.ModelChoiceField(ExpenseConceptSubType.objects.all(),
#                                  widget=autocomplete_light.ChoiceWidget('ExpenseConceptSubTypeAutocomplete'),
#                                  required=False, label="Subconcepto")
    #class Media:
    #    js = ('media/js/expenseitemform.js',)
    class Meta:        
        widgets = autocomplete_light.get_widgets_dict(ExpenseItem)        
        widgets['description'] = forms.Textarea(attrs={'rows':2, 'cols':180, 'class': "input-xxlarge"})
        model = ExpenseItem        
        exclude = ('expense',)

class PersonForm(forms.ModelForm):
    class Meta:
        widgets = autocomplete_light.get_widgets_dict(Person)        
        model = Person
        #fields = ['name', 'cognoms', 'surname']
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['type'].help_text = ''
        self.fields['sections'].help_text = ''
        self.fields['born_date'].widget.attrs.update({'class': "datepicker"})        
#class PhoneForm(forms.ModelForm):
#    class Meta:
#        model = Phone
#        exclude = ('contact_data',)
#                        
#class EmailForm(forms.ModelForm):
#    class Meta:
#        model = Email
#        exclude = ('contact_data',)
#    def __init__(self, *args, **kwargs):
#        super(ExpenseForm, self).__init__(*args, **kwargs)
#        self.fields['date'].widget.attrs.update({'class': "input-small datepicker"})
#        self.fields['payment_date'].widget.attrs.update({'class': "input-small datepicker"})
#        self.fields['state'].widget.attrs.update({'class': "input-medium"})  

