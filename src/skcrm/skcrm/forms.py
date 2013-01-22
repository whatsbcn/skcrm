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

class SearchExpenseForm(forms.Form):
    num = forms.IntegerField(required=False, label='Numero')    

class GastosPorOtrForm(forms.Form):
    fecha_inicio = forms.DateField(required=True, label="Fecha inicio")
    fecha_final = forms.DateField(required=True, label="Fecha final")
    ot = forms.ModelChoiceField(Ot.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('OtAutocomplete'), required=False)
    content_type = forms.ModelChoiceField(ExpenseConceptType.objects.all(),
                                  #widget=autocomplete_light.ChoiceWidget('ExpenseConceptTypeAutocomplete'),
                                  required=False, label="Concepto")
    def __init__(self, *args, **kwargs):
        super(GastosPorOtrForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget.attrs.update({'class': "input-small datepicker"})
        self.fields['fecha_final'].widget.attrs.update({'class': "input-small datepicker"})    

class GastosPorProveedorForm(forms.Form):
    fecha_inicio = forms.DateField(required=True, label="Fecha inicio")
    fecha_final = forms.DateField(required=True, label="Fecha final")
    proveedor = forms.ModelChoiceField(Company.objects.all().filter(types=1),
                                  widget=autocomplete_light.ChoiceWidget('CompanyAutocomplete'), required=False)
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
    class Meta:
        widgets = autocomplete_light.get_widgets_dict(Company)
        #city = forms.ModelChoiceField(City.objects.all(),
        #                              widget=autocomplete_light.ChoiceWidget(AutocompleteCity))
        fields = ('name', 'comercial_name', 'NIF_CIF', 'address', 'postal_code', 'country', 
                  'region', 'city', 'website', 'types', 'disabled', 'is_group', 'in_group', 'account_number')
        model = Company
        exclude = ('relations',)
        
class OtForm(forms.ModelForm):
    class Meta:
        model = Ot   
        exclude = ('company',)

class ExpenseForm(forms.ModelForm):
    class Meta:
        widgets = autocomplete_light.get_widgets_dict(Expense)        
        model = Expense   
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': "input-small datepicker"})
        self.fields['payment_date'].widget.attrs.update({'class': "input-small datepicker"})
        self.fields['state'].widget.attrs.update({'class': "input-medium"})  

class ExpenseItemForm(forms.ModelForm):
    content_type = forms.ModelChoiceField(ExpenseConceptType.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('ExpenseConceptTypeAutocomplete'),
                                  required=False, label="Concepto")
    content_sub_type = forms.ModelChoiceField(ExpenseConceptSubType.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('ExpenseConceptSubTypeAutocomplete'),
                                  required=False, label="Subconcepto")
    #class Media:
    #    js = ('media/js/expenseitemform.js',)
    class Meta:        
        widgets = autocomplete_light.get_widgets_dict(ExpenseItem)        
        widgets['description'] = forms.Textarea(attrs={'rows':2, 'cols':180, 'class': "input-xxlarge"})
        model = ExpenseItem        
        exclude = ('expense',)
