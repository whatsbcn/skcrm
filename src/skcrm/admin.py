# coding: utf8
from django.contrib import admin
from models import *
from datetime import datetime

def create_action(modeladmin, request, queryset):
    new_action = Action(name="Acción autogenerada", type=1, state=1, 
                        user=request.user, date=datetime.now())
    new_action.save()
    
create_action.short_description = "Crea una acción con los contactos seleccionados."

class ActionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'type', 'state', 'client', 
                    'date', 'user']
    readonly_fields = ['date', 'user'] 

class PhoneInline(admin.TabularInline):
    model = Phone
    fields = ['number', 'type']
    extra = 0
    verbose_name_plural = "Números de teléfono"
    
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'cognom1', 'cognom2', 
                    'address', 'email', 'city', 'website', 'phones']
    inlines = [PhoneInline]
    search_fields = ['name', 'cognom1', 'cognom2', 
                    'address', 'email', 'website']
    filter_horizontal  = ('sectors',)
    list_filter = ['types']
    actions = [create_action]

#admin.site.register(ActionState)
#admin.site.register(ActionType)
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