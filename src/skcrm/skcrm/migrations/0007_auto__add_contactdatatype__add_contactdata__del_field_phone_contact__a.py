# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactDataType'
        db.create_table(u'contact_data_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['ContactDataType'])

        # Adding model 'ContactData'
        db.create_table(u'contact_data', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Person'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Company'])),
            ('media', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Media'], null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.PositionTypes'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.ContactDataType'], null=True, blank=True)),
        ))
        db.send_create_signal('skcrm', ['ContactData'])

        # Deleting field 'Phone.contact'
        db.delete_column(u'contact_phones', 'contact_id')

        # Adding field 'Phone.contact_data'
        db.add_column(u'contact_phones', 'contact_data',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.ContactData'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Media.contact_ptr'
        db.delete_column(u'media', 'contact_ptr_id')

        # Adding field 'Media.id'
        db.add_column(u'media', 'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Adding field 'Media.name'
        db.add_column(u'media', 'name',
                      self.gf('django.db.models.fields.CharField')(default='undefined', max_length=100),
                      keep_default=False)

        # Adding field 'Media.website'
        db.add_column(u'media', 'website',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Media.mailing'
        db.add_column(u'media', 'mailing',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Media.disabled'
        db.add_column(u'media', 'disabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Media.NIF_CIF'
        db.add_column(u'media', 'NIF_CIF',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)


        # Changing field 'Ot.number'
        db.alter_column(u'ot', 'number', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True))
        # Deleting field 'Email.contact'
        db.delete_column(u'contact_emails', 'contact_id')

        # Adding field 'Email.contact_data'
        db.add_column(u'contact_emails', 'contact_data',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.ContactData'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Person.contact_ptr'
        db.delete_column(u'person', 'contact_ptr_id')

        # Adding field 'Person.id'
        db.add_column(u'person', 'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Adding field 'Person.name'
        db.add_column(u'person', 'name',
                      self.gf('django.db.models.fields.CharField')(default='undefined', max_length=100),
                      keep_default=False)

        # Adding field 'Person.website'
        db.add_column(u'person', 'website',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Person.disabled'
        db.add_column(u'person', 'disabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Person.NIF_CIF'
        db.add_column(u'person', 'NIF_CIF',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Removing M2M table for field types on 'Person'
        db.delete_table('rel_person_types')

        # Adding M2M table for field type on 'Person'
        db.create_table('rel_person_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['skcrm.person'], null=False)),
            ('persontype', models.ForeignKey(orm['skcrm.persontype'], null=False))
        ))
        db.create_unique('rel_person_types', ['person_id', 'persontype_id'])


    def backwards(self, orm):
        # Deleting model 'ContactDataType'
        db.delete_table(u'contact_data_types')

        # Deleting model 'ContactData'
        db.delete_table(u'contact_data')

        # Adding field 'Phone.contact'
        db.add_column(u'contact_phones', 'contact',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Contact'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Phone.contact_data'
        db.delete_column(u'contact_phones', 'contact_data_id')


        # User chose to not deal with backwards NULL issues for 'Media.contact_ptr'
        raise RuntimeError("Cannot reverse this migration. 'Media.contact_ptr' and its values cannot be restored.")
        # Deleting field 'Media.id'
        db.delete_column(u'media', 'id')

        # Deleting field 'Media.name'
        db.delete_column(u'media', 'name')

        # Deleting field 'Media.website'
        db.delete_column(u'media', 'website')

        # Deleting field 'Media.mailing'
        db.delete_column(u'media', 'mailing')

        # Deleting field 'Media.disabled'
        db.delete_column(u'media', 'disabled')

        # Deleting field 'Media.NIF_CIF'
        db.delete_column(u'media', 'NIF_CIF')


        # User chose to not deal with backwards NULL issues for 'Ot.number'
        raise RuntimeError("Cannot reverse this migration. 'Ot.number' and its values cannot be restored.")
        # Adding field 'Email.contact'
        db.add_column(u'contact_emails', 'contact',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Contact'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Email.contact_data'
        db.delete_column(u'contact_emails', 'contact_data_id')


        # User chose to not deal with backwards NULL issues for 'Person.contact_ptr'
        raise RuntimeError("Cannot reverse this migration. 'Person.contact_ptr' and its values cannot be restored.")
        # Deleting field 'Person.id'
        db.delete_column(u'person', 'id')

        # Deleting field 'Person.name'
        db.delete_column(u'person', 'name')

        # Deleting field 'Person.website'
        db.delete_column(u'person', 'website')

        # Deleting field 'Person.disabled'
        db.delete_column(u'person', 'disabled')

        # Deleting field 'Person.NIF_CIF'
        db.delete_column(u'person', 'NIF_CIF')

        # Adding M2M table for field types on 'Person'
        db.create_table('rel_person_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['skcrm.person'], null=False)),
            ('persontype', models.ForeignKey(orm['skcrm.persontype'], null=False))
        ))
        db.create_unique('rel_person_types', ['person_id', 'persontype_id'])

        # Removing M2M table for field type on 'Person'
        db.delete_table('rel_person_types')


    models = {
        'skcrm.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('region', 'name'),)", 'object_name': 'City', 'db_table': "u'cities'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Region']", 'null': 'True', 'blank': 'True'})
        },
        'skcrm.company': {
            'Meta': {'ordering': "['name']", 'object_name': 'Company', 'db_table': "u'company'", '_ormbases': ['skcrm.Contact']},
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'comercial_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['skcrm.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContextType']", 'null': 'True', 'blank': 'True'}),
            'in_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']", 'null': 'True', 'blank': 'True'}),
            'is_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.Person']", 'null': 'True', 'through': "orm['skcrm.ContactPosition']", 'blank': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.CompanyType']", 'null': 'True', 'db_table': "'rel_company_types'", 'blank': 'True'})
        },
        'skcrm.companytype': {
            'Meta': {'ordering': "['name']", 'object_name': 'CompanyType', 'db_table': "u'company_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.contact': {
            'Meta': {'ordering': "['name']", 'object_name': 'Contact', 'db_table': "u'contacts'"},
            'NIF_CIF': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': '899', 'to': "orm['skcrm.City']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '73', 'to': "orm['skcrm.Country']", 'null': 'True', 'blank': 'True'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'packets_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'default': '33', 'to': "orm['skcrm.Region']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'})
        },
        'skcrm.contactdata': {
            'Meta': {'object_name': 'ContactData', 'db_table': "u'contact_data'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Media']", 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Person']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.PositionTypes']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContactDataType']", 'null': 'True', 'blank': 'True'})
        },
        'skcrm.contactdatatype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactDataType', 'db_table': "u'contact_data_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.contactposition': {
            'Meta': {'object_name': 'ContactPosition', 'db_table': "u'contact_position'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Media']", 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Person']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.PositionTypes']"})
        },
        'skcrm.contacttreatment': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactTreatment', 'db_table': "u'contact_treatments'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        },
        'skcrm.contexttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContextType', 'db_table': "u'context_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country', 'db_table': "u'countries'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.distributiontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'DistributionType', 'db_table': "u'distribution_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.email': {
            'Meta': {'ordering': "['-primary']", 'object_name': 'Email', 'db_table': "u'contact_emails'"},
            'contact_data': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContactData']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '45', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.EmailType']", 'null': 'True', 'blank': 'True'})
        },
        'skcrm.emailtype': {
            'Meta': {'object_name': 'EmailType', 'db_table': "u'contact_email_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '144', 'blank': 'True'})
        },
        'skcrm.expense': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Expense', 'db_table': "u'expense'"},
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'doc_num': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'doc_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ExpenseDocumentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irpf': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'payment_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'skcrm.expenseconceptsubtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ExpenseConceptSubType', 'db_table': "u'expense_concept_subtypes'"},
            'concept_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ExpenseConceptType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.expenseconcepttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ExpenseConceptType', 'db_table': "u'expense_concept_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.expensedocumenttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ExpenseDocumentType', 'db_table': "u'expense_document_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.expenseitem': {
            'Meta': {'ordering': "['-id']", 'object_name': 'ExpenseItem', 'db_table': "u'expense_item'"},
            'base': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'concept_sub_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ExpenseConceptSubType']", 'null': 'True', 'blank': 'True'}),
            'concept_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ExpenseConceptType']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Expense']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.IntegerField', [], {}),
            'ot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Ot']"})
        },
        'skcrm.media': {
            'Meta': {'object_name': 'Media', 'db_table': "u'media'"},
            'NIF_CIF': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']"}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContextType']", 'null': 'True', 'blank': 'True'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ditribution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.DistributionType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'periodicity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.PeriodicityType']", 'null': 'True', 'blank': 'True'}),
            'sectors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.Sector']", 'null': 'True', 'db_table': "'rel_company_sectors'", 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.MediaType']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'})
        },
        'skcrm.mediatype': {
            'Meta': {'ordering': "['name']", 'object_name': 'MediaType', 'db_table': "u'media_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.ot': {
            'Meta': {'object_name': 'Ot', 'db_table': "u'ot'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'skcrm.periodicitytype': {
            'Meta': {'ordering': "['name']", 'object_name': 'PeriodicityType', 'db_table': "u'periodicity_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person', 'db_table': "u'person'"},
            'NIF_CIF': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'born_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cognoms': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_personal_assistant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Person']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.Section']", 'null': 'True', 'db_table': "'rel_person_section'", 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContactTreatment']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.PersonType']", 'null': 'True', 'db_table': "'rel_person_types'", 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'})
        },
        'skcrm.persontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'PersonType', 'db_table': "u'person_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.phone': {
            'Meta': {'ordering': "['-primary']", 'object_name': 'Phone', 'db_table': "u'contact_phones'"},
            'contact_data': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContactData']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.PhoneType']", 'null': 'True', 'blank': 'True'})
        },
        'skcrm.phonetype': {
            'Meta': {'object_name': 'PhoneType', 'db_table': "u'contact_phone_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '144', 'blank': 'True'})
        },
        'skcrm.positiontypes': {
            'Meta': {'ordering': "['name']", 'object_name': 'PositionTypes', 'db_table': "u'contact_position_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region', 'db_table': "u'regions'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.section': {
            'Meta': {'ordering': "['name']", 'object_name': 'Section', 'db_table': "u'section'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['skcrm.Section']"})
        },
        'skcrm.sector': {
            'Meta': {'ordering': "['name']", 'object_name': 'Sector', 'db_table': "u'sectors'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['skcrm.Sector']"})
        }
    }

    complete_apps = ['skcrm']