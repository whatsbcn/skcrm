from django.contrib import admin
from models import *

class ActionStatesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']

class ActionTypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']    

class ActionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'type', 'state', 'client', 'date', 'user']
    readonly_fields = ['id']    

class CitiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']
    readonly_fields = ['id']  

class ContactActionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact', 'action', 'state', 'value']
    readonly_fields = ['id']

class ContactRelationTypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']

class ContactRelationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']
   
class ContactTreatmentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']

class ContactTypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cognom1', 'cognom2', 
                    'address', 'postal_code', 'city', 'region', 'country', 
                    'website', 'born_date', 'phones']
    readonly_fields = ['id'] 
    
class CountriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']

class RegionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']
    
class SectorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']    
    
class PhonesAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'type', 'contact']
    readonly_fields = ['id']
    
class PhoneTypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id']    

admin.site.register(ActionState, ActionStatesAdmin)
admin.site.register(ActionType, ActionTypesAdmin)
admin.site.register(Action, ActionsAdmin)
admin.site.register(City, CitiesAdmin)
admin.site.register(ContactAction, ContactActionsAdmin)
admin.site.register(ContactRelationType, ContactRelationTypesAdmin)
admin.site.register(ContactRelation, ContactRelationsAdmin)
admin.site.register(ContactTreatment, ContactTreatmentsAdmin)
admin.site.register(ContactType, ContactTypesAdmin)
admin.site.register(Contact, ContactsAdmin)
admin.site.register(Country, CountriesAdmin)
admin.site.register(Region, RegionsAdmin)
admin.site.register(Sector, SectorsAdmin)
admin.site.register(Phone, PhonesAdmin)
admin.site.register(PhoneType, PhoneTypesAdmin)