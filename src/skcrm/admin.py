# coding: utf8
from django.contrib import admin
from models import *
from datetime import datetime
from django.http import HttpResponseRedirect

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
    fields = ['person', 'type', 'company', 'media']
    extra = 0
    
class PhoneInline(admin.TabularInline):
    model = Phone
    fields = ['number', 'type', 'primary']
    extra = 0
    verbose_name_plural = "Números de teléfono"
    
class EmailInline(admin.TabularInline):
    model = Email
    fields = ['email', 'type', 'primary']
    extra = 0
    verbose_name_plural = "Emails"    
    
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'cognoms', 
                    'address', 'city', 'website']
    inlines = [CompanyRelationInline,PhoneInline,EmailInline]
    search_fields = ['name', 'cognom1', 'cognom2', 
                    'address', 'website']
    #filter_horizontal  = ('sectors',)
    list_filter = ['types']
    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/contacts/")    
    def response_change(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/contacts/" )
    #actions = [create_action]

class SectorAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']
    list_display = fields
    list_filter = ['parent']
    search_fields = ['name']
    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/")    
    def response_change(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/" )
        
class SectionAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']
    list_display = fields
    list_filter = ['parent']
    search_fields = ['name']    
    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/")    
    def response_change(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/" )
    
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_group']
    inlines = [CompanyRelationInline,PhoneInline,EmailInline]
    list_filter = ['is_group']
    search_fields = ['name']
    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/")    
    def response_change(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/" )    
    
class MediaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [PhoneInline,EmailInline]
    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/")    
    def response_change(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/" )    
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
admin.site.register(Section, SectionAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Company, CompanyAdmin)
#admin.site.register(Phone)
#admin.site.register(Email)
admin.site.register(Media, MediaAdmin)
admin.site.register(ContactPosition)


