# coding: utf8
from django.contrib import admin
from models import *
from datetime import datetime

def create_action(modeladmin, request, queryset):
    new_action = Action(name="Autegenerada " + request.user.first_name + " " + request.user.last_name + " " + str(datetime.now()), state=1, 
                        user=request.user, date=datetime.now())
    new_action.save()
    
    for c in queryset:
        ContactAnswer(contact=c, action=new_action, attempt=0).save()
    
create_action.short_description = "Crea una acción con los contactos seleccionados."

class AnswerInline(admin.TabularInline):
    model = ContactAnswer
    fields = ['contact', 'attempt', 'answer']
    #readonly_fields = ['contact']
    extra = 0
    verbose_name_plural = "Contactos"

class ActionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'type', 'state', 'client', 
                    'date', 'user', 'contactsReport']
    readonly_fields = ['date', 'user'] 
    search_fields = ['name', 'description']
    inlines = [AnswerInline]
    date_hierarchy = 'date'
    list_filter = ['type', 'state', 'client', 'user']

class AnswerInline2(admin.TabularInline):
    model = ContactAnswer
    fields = ['action', 'answer']
    extra = 0
    verbose_name_plural = "Acciones participadas"

class PhoneInline(admin.TabularInline):
    model = Phone
    fields = ['number', 'type']
    extra = 0
    verbose_name_plural = "Números de teléfono"
    
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'cognom1', 'cognom2', 
                    'address', 'email', 'city', 'website', 'phones']
    inlines = [PhoneInline, AnswerInline2]
    search_fields = ['name', 'cognom1', 'cognom2', 
                    'address', 'email', 'website']
    filter_horizontal  = ('sectors',)
    list_filter = ['types']
    actions = [create_action]

class ContactAnswerAdmin(admin.ModelAdmin):
    list_display = ['contact', 'action', 'attempt', 'answer']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']
    search_fields = ['name']
    list_filter = ['region']

class ContryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ContactTypeAdmin(admin.ModelAdmin):
    pass



admin.site.register(Action, ActionAdmin)
admin.site.register(City, CityAdmin)
#admin.site.register(ContactAnswer, ContactAnswerAdmin)
admin.site.register(ContactRelationType)
admin.site.register(ContactRelation)
admin.site.register(ContactTreatment)
admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(Contact, ContactsAdmin)
admin.site.register(Country, ContryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Sector)
#admin.site.register(Phone)
admin.site.register(PhoneType)