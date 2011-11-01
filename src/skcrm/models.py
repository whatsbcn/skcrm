from django.db import models
from django.contrib.auth.models import User

class ActionState(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'action_states'
        ordering = ['name']
    def __unicode__(self):
        return self.name        

class ActionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'action_types'
        ordering = ['name']
    def __unicode__(self):
        return self.name        

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'countries'
        ordering = ['name']
    def __unicode__(self):
        return self.name        

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'regions'
        ordering = ['name']
    def __unicode__(self):
        return self.name        

class City(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, null=True, blank=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'cities'
        ordering = ['name']
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
    name = models.CharField(max_length=256)
    cognom1 = models.CharField(max_length=256, blank=True)
    cognom2 = models.CharField(max_length=256, blank=True)
    surname = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=45, blank=True)
    personal_assistant = models.ForeignKey('self', null=True, blank=True)
    treatment = models.ForeignKey(ContactTreatment, null=True, blank=True)
    address = models.CharField(max_length=256, blank=True)
    postal_code = models.CharField(max_length=32, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    region = models.ForeignKey(Region, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    website = models.URLField(max_length=256, blank=True)
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
    name = models.CharField(unique=True, max_length=144, blank=True)
    description = models.TextField(blank=True)
    type = models.ForeignKey(ActionType, null=True, blank=True)
    state = models.ForeignKey(ActionState, null=True, blank=True)
    client = models.ForeignKey(Contact, limit_choices_to = {'types__name__contains': "Cliente"}, null=True, blank=True)
    date = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    class Meta:
        db_table = u'actions'
        ordering = ['name']
    def __unicode__(self):
        return unicode(self.name)        

class ContactRelationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'contact_relation_types'
        ordering = ['name']
    def __unicode__(self):
        return self.name        

# MANY TO MANY RELATIONS

class ContactAction(models.Model):
    id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Contact, null=True, blank=True)
    action = models.ForeignKey(Action, null=True, blank=True)
    state = models.IntegerField()
    value = models.CharField(max_length=192, blank=True)
    class Meta:
        db_table = u'contact_actions'
    def __unicode__(self):
        return self.action + " => " + self.contact        

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

