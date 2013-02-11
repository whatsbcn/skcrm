# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ContactPosition'
        db.delete_table(u'contact_position')

        # Deleting field 'Company.contact_ptr_id'
        db.delete_column(u'company', 'contact_ptr_id')


        # Changing field 'Company.id'
        db.alter_column(u'company', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))
        # Adding unique constraint on 'Company', fields ['id']
        db.create_unique(u'company', ['id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Company', fields ['id']
        db.delete_unique(u'company', ['id'])

        # Adding model 'ContactPosition'
        db.create_table(u'contact_position', (
            ('media', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Media'], null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Company'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Person'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.PositionTypes'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('skcrm', ['ContactPosition'])


        # User chose to not deal with backwards NULL issues for 'Company.contact_ptr_id'
        raise RuntimeError("Cannot reverse this migration. 'Company.contact_ptr_id' and its values cannot be restored.")

        # Changing field 'Company.id'
        db.alter_column(u'company', 'id', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'skcrm.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('region', 'name'),)", 'object_name': 'City', 'db_table': "u'cities'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Region']", 'null': 'True', 'blank': 'True'})
        },
        'skcrm.company': {
            'Meta': {'object_name': 'Company', 'db_table': "u'company'"},
            'NIF_CIF': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'comercial_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContextType']", 'null': 'True', 'blank': 'True'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '45', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']", 'null': 'True', 'blank': 'True'}),
            'is_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mailing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.CompanyType']", 'null': 'True', 'db_table': "'rel_company_types'", 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'})
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': '899', 'to': "orm['skcrm.City']", 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']", 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '73', 'to': "orm['skcrm.Country']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Media']", 'null': 'True', 'blank': 'True'}),
            'packets_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Person']", 'null': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.PositionTypes']", 'null': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'default': '33', 'to': "orm['skcrm.Region']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContactDataType']"})
        },
        'skcrm.contactdatatype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactDataType', 'db_table': "u'contact_data_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
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