# coding: utf8

from django.db import models
from django.contrib.auth.models import User
     
ACTION_STATE = (
    (1, 'Abierta'),
    (2, 'Cerrada'),
)

ACTION_TYPE = (
    (1, '1. Invitación'),
    (2, '2. Nota de prensa'),
)

ANSWER_TYPE = (
    (1, '1. Pendiente'),               
    (2, '2. Confirmado'),
    (3, '3. Rechazado'),
) 

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'countries'
        ordering = ['name']
        verbose_name_plural = "Países"        
    def __unicode__(self):
        return self.name        

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'regions'
        ordering = ['name']
        verbose_name_plural = "Provincias"
    def __unicode__(self):
        return self.name        

class City(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, null=True, blank=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'cities'
        ordering = ['name']
        unique_together = ('region', 'name',)
        verbose_name_plural = "Ciudades"
    def __unicode__(self):
        return self.name        

class ContactTreatment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True)
    class Meta:
        db_table = u'contact_treatments'
        ordering = ['name']
        verbose_name_plural = "Tratos"
    def __unicode__(self):
        return self.name        

class MediaType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'media_types'
        ordering = ['name']
        verbose_name_plural = "Tipo de medios"
    def __unicode__(self):
        return self.name     

class PersonType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'person_types'
        ordering = ['name']
        verbose_name_plural = "Tipo de personas"
    def __unicode__(self):
        return self.name     

class CompanyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'company_types'
        ordering = ['name']
        verbose_name_plural = "Tipo empresas"
    def __unicode__(self):
        return self.name 

class ContextType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'context_types'
        ordering = ['name']
        verbose_name_plural = "Ámbito de empresa"
    def __unicode__(self):
        return self.name 

class DistributionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'distribution_types'
        ordering = ['name']
        verbose_name_plural = "Típo de distribución"
    def __unicode__(self):
        return self.name

class PeriodicityType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'periodicity_types'
        ordering = ['name']
        verbose_name_plural = "Periodicidad"
    def __unicode__(self):
        return self.name
       
class PhoneType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=144, blank=True)
    class Meta:
        db_table = u'contact_phone_types'
        verbose_name_plural = "Tipo de teléfono"
    def __unicode__(self):
        return self.name    

class EmailType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=144, blank=True)
    class Meta:
        db_table = u'contact_email_types'
        verbose_name_plural = "Tipo de email"
    def __unicode__(self):
        return self.name

class PositionTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'contact_position_types'
        ordering = ['name']
        verbose_name_plural = "Cargos"
    def __unicode__(self):
        return self.name 


    
class Sector(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child')
    class Meta:
        db_table = u'sectors'
        ordering = ['name']
        verbose_name_plural = "Sectores"
    def __unicode__(self):
        return self.name

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45, blank=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child')
    class Meta:
        db_table = u'section'
        ordering = ['name']
        verbose_name_plural = "Secciones"
    def __unicode__(self):
        if self.parent != None:
            return self.parent.name + "__" + self.name
        else:
            return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    #email = models.EmailField(max_length=45, blank=True)
    address = models.CharField(max_length=100, blank=True, verbose_name="Dirección")
    packets_address = models.CharField(max_length=100, blank=True, verbose_name="Dirección para paquetes")
    postal_code = models.CharField(max_length=32, blank=True, verbose_name="Código postal")
    city = models.ForeignKey(City, null=True, blank=True, verbose_name="Ciudad")
    region = models.ForeignKey(Region, null=True, blank=True, verbose_name="Comunidad autónoma")
    country = models.ForeignKey(Country, null=True, blank=True, verbose_name="País")
    website = models.URLField(max_length=100, blank=True, verbose_name="Página web")
    mailing = models.BooleanField(verbose_name="Consiente que se le envien emails?")
    # Per els contactes que volem tenir però no voldrem convidar mai, ni enviar-lis coses
    disabled = models.BooleanField(verbose_name="Contacto desactivado?")
    NIF_CIF = models.CharField(max_length=45, blank=True, verbose_name="NIF/CIF")
    class Meta:
        db_table = u'contacts'
        ordering = ['name']
        verbose_name_plural = "Contactos"
    def __unicode__(self):
        return self.name
        
class Person(Contact):
    cognoms = models.CharField(max_length=200, blank=True)
    #cognom2 = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    has_personal_assistant = models.ForeignKey('self', null=True, blank=True)
    treatment = models.ForeignKey(ContactTreatment, null=True, blank=True)
    born_date = models.DateField(null=True, blank=True)
    types = models.ManyToManyField(PersonType, db_table="rel_person_types", null=True, blank=True)
    sections = models.ManyToManyField(Section, db_table="rel_person_section", null=True, blank=True)
    positions = models.ManyToManyField('Company', through='ContactPosition', null=True, blank=True)
    class Meta:
        db_table = u'person'
        ordering = ['name']
        verbose_name_plural = "Personas"
    def __unicode__(self):
        return self.name + " " + self.cognoms

class Company(Contact):
    types = models.ManyToManyField(CompanyType, db_table="rel_company_types", null=True, blank=True)
    context = models.ForeignKey(ContextType, null=True, blank=True, verbose_name="Ámbito")
    is_group = models.BooleanField(verbose_name="Es un grupo de empresas")
    in_group = models.ForeignKey('Company', null=True, blank=True, limit_choices_to= {"is_group" : True})
    relations = models.ManyToManyField(Person, through='ContactPosition', null=True, blank=True)
    class Meta:
        db_table = u'company'
        #ordering = ['name']
        verbose_name_plural = "Empresas"
    def __unicode__(self):
        return self.name
                
class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.ForeignKey(PhoneType, null=True, blank=True)
    contact = models.ForeignKey(Contact, null=True, blank=True)
    primary = models.BooleanField(verbose_name="Principal")                     
    class Meta:
        db_table = u'contact_phones'
        verbose_name_plural = "Teléfonos"
        ordering = ['-primary']        
    def __unicode__(self):
        return unicode(self.number)         
                
class Email(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=45, blank=True)
    type = models.ForeignKey(EmailType, null=True, blank=True)
    contact = models.ForeignKey(Contact, null=True, blank=True)
    primary = models.BooleanField(verbose_name="Principal")                
    class Meta:
        db_table = u'contact_emails'
        verbose_name_plural = "Emails"
        ordering = ['-primary']
    def __unicode__(self):
        return unicode(self.email)         

class Media(Contact):
    #id = models.AutoField(primary_key=True)
    #name = models.CharField(unique=True, max_length=144, blank=True)
    type = models.ForeignKey(MediaType, null=True, blank=True)
    context = models.ForeignKey(ContextType, null=True, blank=True)
    sectors = models.ManyToManyField(Sector, db_table="rel_company_sectors", null=True, blank=True)
    ditribution = models.ForeignKey(DistributionType, null=True, blank=True)
    periodicity = models.ForeignKey(PeriodicityType, null=True, blank=True)
    company = models.ForeignKey(Company, null=False, blank=False, limit_choices_to= {"is_group" : False})
    class Meta:
        db_table = u'media'
        verbose_name_plural = "Medios"
    def __unicode__(self):
        return unicode(self.name)         

class ContactPosition(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, null=False, blank=False)
    company = models.ForeignKey(Company, null=False, blank=False)
    media = models.ForeignKey(Media, null=True, blank=True)
    type = models.ForeignKey(PositionTypes, null=False, blank=False)
    class Meta:
        db_table = u'contact_position'
        #ordering = ['name']
        verbose_name_plural = "Relaciones laborales"
    def __unicode__(self):
        return unicode(self.person) + " - " +  unicode(self.company) + " - " + unicode(self.media)

        
#class Action(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=256, blank=True)
#    description = models.TextField(blank=True)
#    type = models.IntegerField(max_length=1, choices=ACTION_TYPE, null=True, blank=True)
#    state = models.IntegerField(max_length=1, default=1, choices=ACTION_STATE, null=True, blank=True)
#    client = models.ForeignKey(Contact, related_name="client_set", limit_choices_to = {'types__name__contains': "Cliente"}, null=True, blank=True)
#    date = models.DateTimeField(blank=True)
#    user = models.ForeignKey(User, null=True, blank=True)
#    contacts = models.ManyToManyField(Person, through='ContactAnswer', null=True, blank=True)
#    class Meta:
#        db_table = u'actions'
#        ordering = ['name']
#    def __unicode__(self):
#        return unicode(self.name) + " / " + unicode(self.date) + " / " + unicode(self.client)
#    def countContacts(self):
#        return ContactAnswer.objects.filter(action=self).count()
#    def countContactsAnswer(self, a):
#        return ContactAnswer.objects.filter(action=self, answer=a).count()
#    def contactsReport(self):
#        return unicode(self.countContactsAnswer(2)+self.countContactsAnswer(3)) + "/" + unicode(self.countContacts())
       

# MANY TO MANY RELATIONS


#class ContactAnswer(models.Model):
#    id = models.AutoField(primary_key=True)
#    contact = models.ForeignKey(Person, null=True, blank=True)
#    action = models.ForeignKey(Action, null=True, blank=True)
#    attempt = models.IntegerField(default=0)
#    answer = models.IntegerField(max_length=3, choices=ANSWER_TYPE, default=1)
#    class Meta:
#        db_table = u'contact_answer'
#        unique_together = ('contact', 'action',)
#    def __unicode__(self):
#        return "Answer: " + unicode(self.answer)         


