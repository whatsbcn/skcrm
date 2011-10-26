from django.db import models
from django.contrib.auth.models import User

class ActionStates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'action_states'

class ActionTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'action_types'

class Countries(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'countries'

class Regions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'regions'

class Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'cities'

class ContactTreatments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'contact_treatments'

class ContactTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'contact_types'

class Sectors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=135, blank=True)
    class Meta:
        db_table = u'sectors'
        
class Contacts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=768, blank=True)
    cognom1 = models.CharField(max_length=768, blank=True)
    cognom2 = models.CharField(max_length=768, blank=True)
    surname = models.CharField(max_length=768, blank=True)
    personal_assistant = models.ForeignKey('self', null=True, blank=True)
    treatment = models.ForeignKey(ContactTreatments, null=True, blank=True)
    address = models.CharField(max_length=768, blank=True)
    postal_code = models.CharField(max_length=96, blank=True)
    city = models.ForeignKey(Cities, null=True, blank=True)
    region = models.ForeignKey(Regions, null=True, blank=True)
    country = models.ForeignKey(Countries, null=True, blank=True)
    website = models.CharField(max_length=768, blank=True)
    born_date = models.DateField(null=True, blank=True)
    type = models.ForeignKey(ContactTypes, null=True, blank=True)
    sectors = models.ManyToManyField(Sectors)
    class Meta:
        db_table = u'contacts'

class Actions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=144, blank=True)
    description = models.TextField(blank=True)
    type = models.ForeignKey(ActionTypes, null=True, blank=True)
    state = models.ForeignKey(ActionStates, null=True, blank=True)
    client = models.ForeignKey(Contacts, null=True, blank=True)
    date = models.CharField(max_length=135, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    class Meta:
        db_table = u'actions'

class ContactRelationTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'contact_relation_types'

# MANY TO MANY RELATIONS

class ContactActions(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey(Contacts, null=True, blank=True)
    action = models.ForeignKey(Actions, null=True, blank=True)
    value = models.CharField(max_length=192, blank=True)
    class Meta:
        db_table = u'contact_actions'

class ContactRelations(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    contacte1 = models.ForeignKey(Contacts, null=True, db_column='contact_id1', blank=True, related_name='topic_content_type')
    contacte2 = models.ForeignKey(Contacts, null=True, db_column='contact_id2', blank=True, related_name='topic_content_type2')
    type = models.ForeignKey(ContactRelationTypes, null=True, blank=True)
    class Meta:
        db_table = u'contact_relations'

