# coding: utf8
from django.contrib import admin
from models import *

class ActionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'type', 'state', 'client', 
                    'date', 'user']

class PhoneInline(admin.TabularInline):
    model = Phone
    fields = ['number', 'type']
    extra = 0
    verbose_name_plural = "Números de teléfono"
    
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'cognom1', 'cognom2', 
                    'address', 'postal_code', 'city', 'region', 'country', 
                    'website', 'born_date', 'phones']
    inlines = [PhoneInline]

admin.site.register(ActionState)
admin.site.register(ActionType)
admin.site.register(Action, ActionAdmin)
admin.site.register(City)
admin.site.register(ContactAction)
admin.site.register(ContactRelationType)
admin.site.register(ContactRelation)
admin.site.register(ContactTreatment)
admin.site.register(ContactType)
admin.site.register(Contact, ContactsAdmin)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Sector)
#admin.site.register(Phone)
admin.site.register(PhoneType)