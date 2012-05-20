# coding: utf8
from django.contrib import admin
from models import *
from datetime import datetime

#def create_action(modeladmin, request, queryset):
#    new_action = Action(name="Autegenerada " + request.user.first_name + " " + request.user.last_name + " " + str(datetime.now()), state=1, 
#                        user=request.user, date=datetime.now())
#    new_action.save()
#    
#    for c in queryset:
#        ContactAnswer(contact=c, action=new_action, attempt=0).save()
#    
#create_action.short_description = "Crea una acción con los contactos seleccionados."

#class AnswerInline(admin.TabularInline):
#    model = ContactAnswer
#    fields = ['contact', 'attempt', 'answer']
#    #readonly_fields = ['contact']
#    extra = 0
#    verbose_name_plural = "Contactos"
#    #readonly_fields = ['contact']
#
#class ActionAdmin(admin.ModelAdmin):
#    list_display = ['name', 'description', 'type', 'state', 'client', 
#                    'date', 'user', 'contactsReport']
#    readonly_fields = ['date', 'user'] 
#    #fields = ['contacts']
#    search_fields = ['name', 'description']
#    inlines = [AnswerInline]
#    date_hierarchy = 'date'
#    list_filter = ['type', 'state', 'client', 'user']
#
#class AnswerInline2(admin.TabularInline):
#    model = ContactAnswer
#    fields = ['action', 'answer']
#    extra = 0
#    verbose_name_plural = "Acciones participadas"
    
class RelationInline(admin.TabularInline):
    model = ContactPosition
    fields = ['name', 'company', 'type']
    extra = 0
    
class CompanyRelationInline(admin.TabularInline):
    model = ContactPosition
    fields = ['person', 'type']
    extra = 0
    
    
class PhoneInline(admin.TabularInline):
    model = Phone
    fields = ['number', 'type']
    extra = 0
    verbose_name_plural = "Números de teléfono"
    
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'cognoms', 
                    'address', 'city', 'website']
    inlines = [PhoneInline]
    search_fields = ['name', 'cognom1', 'cognom2', 
                    'address', 'website']
    #filter_horizontal  = ('sectors',)
    list_filter = ['types']
    #actions = [create_action]

class SectorAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']

class CompanyAdmin(admin.ModelAdmin):
    #list_display = ['address', 'city', 'NIF_CIF']
    inlines = [CompanyRelationInline]
    

#class CompanyAdmin(admin.ModelAdmin):
#    list_display = ['name', 'address', 'email', 'city', 'website', 'phones']
#    inlines = [PhoneInline]
#    search_fields = ['name', 'address', 'email', 'website']
#    filter_horizontal  = ('sectors',)
#    list_filter = ['types']
#    actions = [create_action]

class ContactAnswerAdmin(admin.ModelAdmin):
    list_display = ['contact', 'action', 'attempt', 'answer']


    
class ContryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']
    search_fields = ['name']
    list_filter = ['region']

admin.site.register(Country, ContryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(ContactTreatment)
admin.site.register(MediaType)
admin.site.register(PersonType)
admin.site.register(CompanyType)
admin.site.register(ContextType)
admin.site.register(DistributionType)
admin.site.register(PeriodicityType)
admin.site.register(PhoneType)
admin.site.register(EmailType)
admin.site.register(PositionTypes)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Section)
admin.site.register(Person, PersonAdmin)
admin.site.register(Company, CompanyAdmin)
#admin.site.register(Phone)
#admin.site.register(Email)
admin.site.register(Media)
admin.site.register(ContactPosition)


