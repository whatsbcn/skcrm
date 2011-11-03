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
        verbose_name_plural = "Regiones"
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
    def __unicode__(self):
        return self.name        

class ContactTreatment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True)
    class Meta:
        db_table = u'contact_treatments'
        ordering = ['name']
    def __unicode__(self):
        return self.name        

class ContactType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'contact_types'
        ordering = ['name']
    def __unicode__(self):
        return self.name        

class Sector(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45, blank=True)
    class Meta:
        db_table = u'sectors'
        ordering = ['name']
    def __unicode__(self):
        return self.name
        
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100, blank=True)
    cognom2 = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=45, blank=True)
    personal_assistant = models.ForeignKey('self', null=True, blank=True)
    treatment = models.ForeignKey(ContactTreatment, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=32, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    region = models.ForeignKey(Region, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    website = models.URLField(max_length=100, blank=True)
    born_date = models.DateField(null=True, blank=True)
    types = models.ManyToManyField(ContactType, db_table="rel_contact_types", null=True, blank=True)
    sectors = models.ManyToManyField(Sector, db_table="rel_contact_sectors", null=True, blank=True)
    mailing = models.BooleanField()
    NIF_CIF = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'contacts'
        ordering = ['name']
    def __unicode__(self):
        return self.name + " " + self.cognom1 + " " + self.cognom2
    def phones(self):
        return Phone.objects.filter(contact=self)
        
class PhoneType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=144, blank=True)
    class Meta:
        db_table = u'contact_phone_types'
    def __unicode__(self):
        return self.name
                
class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.ForeignKey(PhoneType, null=True, blank=True)
    contact = models.ForeignKey(Contact, null=True, blank=True)                
    class Meta:
        db_table = u'contact_phones'
    def __unicode__(self):
        return unicode(self.number)         
        
class Action(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    type = models.IntegerField(max_length=1, choices=ACTION_TYPE, null=True, blank=True)
    state = models.IntegerField(max_length=1, default=1, choices=ACTION_STATE, null=True, blank=True)
    client = models.ForeignKey(Contact, limit_choices_to = {'types__name__contains': "Cliente"}, null=True, blank=True)
    date = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    #contacts = models.ManyToManyField(Contact, db_table="rel_?????", null=True, blank=True)
    class Meta:
        db_table = u'actions'
        ordering = ['name']
    def __unicode__(self):
        return unicode(self.name) + " / " + unicode(self.date) + " / " + unicode(self.client)
    def countContacts(self):
        return ContactAnswer.objects.filter(action=self).count()
    def countContactsAnswer(self, a):
        return ContactAnswer.objects.filter(action=self, answer=a).count()
    def contactsReport(self):
        return unicode(self.countContactsAnswer(2)+self.countContactsAnswer(3)) + "/" + unicode(self.countContacts())

class ContactRelationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'contact_relation_types'
        ordering = ['name']
    def __unicode__(self):
        return self.name        

# MANY TO MANY RELATIONS


class ContactAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Contact, null=True, blank=True)
    action = models.ForeignKey(Action, null=True, blank=True)
    attempt = models.IntegerField(default=0)
    answer = models.IntegerField(max_length=3, choices=ANSWER_TYPE, default=1)
    class Meta:
        db_table = u'contact_answer'
        unique_together = ('contact', 'action',)
    def __unicode__(self):
        return "Answer: " + unicode(self.answer)         

class ContactRelation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    contacte1 = models.ForeignKey(Contact, null=True, db_column='contact_id1', blank=True, related_name='topic_content_type')
    contacte2 = models.ForeignKey(Contact, null=True, db_column='contact_id2', blank=True, related_name='topic_content_type2')
    type = models.ForeignKey(ContactRelationType, null=True, blank=True)
    class Meta:
        db_table = u'contact_relations'
        ordering = ['name']
    def __unicode__(self):
        return self.name    

