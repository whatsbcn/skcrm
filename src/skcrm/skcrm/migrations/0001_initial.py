# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'countries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['Country'])

        # Adding model 'Region'
        db.create_table(u'regions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['Region'])

        # Adding model 'City'
        db.create_table(u'cities', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Region'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['City'])

        # Adding unique constraint on 'City', fields ['region', 'name']
        db.create_unique(u'cities', ['region_id', 'name'])

        # Adding model 'ContactTreatment'
        db.create_table(u'contact_treatments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
        ))
        db.send_create_signal('skcrm', ['ContactTreatment'])

        # Adding model 'MediaType'
        db.create_table(u'media_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['MediaType'])

        # Adding model 'PersonType'
        db.create_table(u'person_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['PersonType'])

        # Adding model 'CompanyType'
        db.create_table(u'company_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['CompanyType'])

        # Adding model 'ContextType'
        db.create_table(u'context_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['ContextType'])

        # Adding model 'DistributionType'
        db.create_table(u'distribution_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['DistributionType'])

        # Adding model 'PeriodicityType'
        db.create_table(u'periodicity_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['PeriodicityType'])

        # Adding model 'PhoneType'
        db.create_table(u'contact_phone_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=144, blank=True)),
        ))
        db.send_create_signal('skcrm', ['PhoneType'])

        # Adding model 'EmailType'
        db.create_table(u'contact_email_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=144, blank=True)),
        ))
        db.send_create_signal('skcrm', ['EmailType'])

        # Adding model 'PositionTypes'
        db.create_table(u'contact_position_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['PositionTypes'])

        # Adding model 'ExpenseDocumentType'
        db.create_table(u'expense_document_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['ExpenseDocumentType'])

        # Adding model 'ExpenseConceptType'
        db.create_table(u'expense_concept_types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['ExpenseConceptType'])

        # Adding model 'Sector'
        db.create_table(u'sectors', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['skcrm.Sector'])),
        ))
        db.send_create_signal('skcrm', ['Sector'])

        # Adding model 'Section'
        db.create_table(u'section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['skcrm.Section'])),
        ))
        db.send_create_signal('skcrm', ['Section'])

        # Adding model 'Contact'
        db.create_table(u'contacts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('packets_address', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(default=73, to=orm['skcrm.Country'], null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(default=33, to=orm['skcrm.Region'], null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(default=899, to=orm['skcrm.City'], null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('mailing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('NIF_CIF', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('skcrm', ['Contact'])

        # Adding model 'Person'
        db.create_table(u'person', (
            ('contact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['skcrm.Contact'], unique=True, primary_key=True)),
            ('cognoms', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('has_personal_assistant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Person'], null=True, blank=True)),
            ('treatment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.ContactTreatment'], null=True, blank=True)),
            ('born_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('skcrm', ['Person'])

        # Adding M2M table for field types on 'Person'
        db.create_table('rel_person_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['skcrm.person'], null=False)),
            ('persontype', models.ForeignKey(orm['skcrm.persontype'], null=False))
        ))
        db.create_unique('rel_person_types', ['person_id', 'persontype_id'])

        # Adding M2M table for field sections on 'Person'
        db.create_table('rel_person_section', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['skcrm.person'], null=False)),
            ('section', models.ForeignKey(orm['skcrm.section'], null=False))
        ))
        db.create_unique('rel_person_section', ['person_id', 'section_id'])

        # Adding model 'Company'
        db.create_table(u'company', (
            ('contact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['skcrm.Contact'], unique=True, primary_key=True)),
            ('comercial_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('context', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.ContextType'], null=True, blank=True)),
            ('is_group', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('in_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Company'], null=True, blank=True)),
        ))
        db.send_create_signal('skcrm', ['Company'])

        # Adding M2M table for field types on 'Company'
        db.create_table('rel_company_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['skcrm.company'], null=False)),
            ('companytype', models.ForeignKey(orm['skcrm.companytype'], null=False))
        ))
        db.create_unique('rel_company_types', ['company_id', 'companytype_id'])

        # Adding model 'Ot'
        db.create_table(u'ot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Company'])),
        ))
        db.send_create_signal('skcrm', ['Ot'])

        # Adding model 'Expense'
        db.create_table(u'expense', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doc_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.ExpenseDocumentType'], null=True, blank=True)),
            ('doc_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('payment_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Company'], null=True, blank=True)),
            ('irpf', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('skcrm', ['Expense'])

        # Adding model 'ExpenseItem'
        db.create_table(u'expense_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('concept_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.ExpenseConceptType'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('expense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Expense'])),
            ('ot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Ot'])),
            ('iva', self.gf('django.db.models.fields.IntegerField')()),
            ('base', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('skcrm', ['ExpenseItem'])

        # Adding model 'Phone'
        db.create_table(u'contact_phones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.PhoneType'], null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Contact'], null=True, blank=True)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('skcrm', ['Phone'])

        # Adding model 'Email'
        db.create_table(u'contact_emails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=45, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.EmailType'], null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Contact'], null=True, blank=True)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('skcrm', ['Email'])

        # Adding model 'Media'
        db.create_table(u'media', (
            ('contact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['skcrm.Contact'], unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.MediaType'], null=True, blank=True)),
            ('context', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.ContextType'], null=True, blank=True)),
            ('ditribution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.DistributionType'], null=True, blank=True)),
            ('periodicity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.PeriodicityType'], null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Company'])),
        ))
        db.send_create_signal('skcrm', ['Media'])

        # Adding M2M table for field sectors on 'Media'
        db.create_table('rel_company_sectors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('media', models.ForeignKey(orm['skcrm.media'], null=False)),
            ('sector', models.ForeignKey(orm['skcrm.sector'], null=False))
        ))
        db.create_unique('rel_company_sectors', ['media_id', 'sector_id'])

        # Adding model 'ContactPosition'
        db.create_table(u'contact_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Person'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Company'])),
            ('media', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.Media'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skcrm.PositionTypes'])),
        ))
        db.send_create_signal('skcrm', ['ContactPosition'])


    def backwards(self, orm):
        # Removing unique constraint on 'City', fields ['region', 'name']
        db.delete_unique(u'cities', ['region_id', 'name'])

        # Deleting model 'Country'
        db.delete_table(u'countries')

        # Deleting model 'Region'
        db.delete_table(u'regions')

        # Deleting model 'City'
        db.delete_table(u'cities')

        # Deleting model 'ContactTreatment'
        db.delete_table(u'contact_treatments')

        # Deleting model 'MediaType'
        db.delete_table(u'media_types')

        # Deleting model 'PersonType'
        db.delete_table(u'person_types')

        # Deleting model 'CompanyType'
        db.delete_table(u'company_types')

        # Deleting model 'ContextType'
        db.delete_table(u'context_types')

        # Deleting model 'DistributionType'
        db.delete_table(u'distribution_types')

        # Deleting model 'PeriodicityType'
        db.delete_table(u'periodicity_types')

        # Deleting model 'PhoneType'
        db.delete_table(u'contact_phone_types')

        # Deleting model 'EmailType'
        db.delete_table(u'contact_email_types')

        # Deleting model 'PositionTypes'
        db.delete_table(u'contact_position_types')

        # Deleting model 'ExpenseDocumentType'
        db.delete_table(u'expense_document_types')

        # Deleting model 'ExpenseConceptType'
        db.delete_table(u'expense_concept_types')

        # Deleting model 'Sector'
        db.delete_table(u'sectors')

        # Deleting model 'Section'
        db.delete_table(u'section')

        # Deleting model 'Contact'
        db.delete_table(u'contacts')

        # Deleting model 'Person'
        db.delete_table(u'person')

        # Removing M2M table for field types on 'Person'
        db.delete_table('rel_person_types')

        # Removing M2M table for field sections on 'Person'
        db.delete_table('rel_person_section')

        # Deleting model 'Company'
        db.delete_table(u'company')

        # Removing M2M table for field types on 'Company'
        db.delete_table('rel_company_types')

        # Deleting model 'Ot'
        db.delete_table(u'ot')

        # Deleting model 'Expense'
        db.delete_table(u'expense')

        # Deleting model 'ExpenseItem'
        db.delete_table(u'expense_item')

        # Deleting model 'Phone'
        db.delete_table(u'contact_phones')

        # Deleting model 'Email'
        db.delete_table(u'contact_emails')

        # Deleting model 'Media'
        db.delete_table(u'media')

        # Removing M2M table for field sectors on 'Media'
        db.delete_table('rel_company_sectors')

        # Deleting model 'ContactPosition'
        db.delete_table(u'contact_position')


    models = {
        'skcrm.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('region', 'name'),)", 'object_name': 'City', 'db_table': "u'cities'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Region']", 'null': 'True', 'blank': 'True'})
        },
        'skcrm.company': {
            'Meta': {'ordering': "['name']", 'object_name': 'Company', 'db_table': "u'company'", '_ormbases': ['skcrm.Contact']},
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
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Contact']", 'null': 'True', 'blank': 'True'}),
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
            'doc_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'doc_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ExpenseDocumentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irpf': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'payment_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '1'})
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
            'concept_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ExpenseConceptType']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Expense']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.IntegerField', [], {}),
            'ot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Ot']"})
        },
        'skcrm.media': {
            'Meta': {'ordering': "['name']", 'object_name': 'Media', 'db_table': "u'media'", '_ormbases': ['skcrm.Contact']},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Company']"}),
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['skcrm.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContextType']", 'null': 'True', 'blank': 'True'}),
            'ditribution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.DistributionType']", 'null': 'True', 'blank': 'True'}),
            'periodicity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.PeriodicityType']", 'null': 'True', 'blank': 'True'}),
            'sectors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.Sector']", 'null': 'True', 'db_table': "'rel_company_sectors'", 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.MediaType']", 'null': 'True', 'blank': 'True'})
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
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        'skcrm.periodicitytype': {
            'Meta': {'ordering': "['name']", 'object_name': 'PeriodicityType', 'db_table': "u'periodicity_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person', 'db_table': "u'person'", '_ormbases': ['skcrm.Contact']},
            'born_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cognoms': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['skcrm.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'has_personal_assistant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Person']", 'null': 'True', 'blank': 'True'}),
            'positions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.Company']", 'null': 'True', 'through': "orm['skcrm.ContactPosition']", 'blank': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.Section']", 'null': 'True', 'db_table': "'rel_person_section'", 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.ContactTreatment']", 'null': 'True', 'blank': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['skcrm.PersonType']", 'null': 'True', 'db_table': "'rel_person_types'", 'blank': 'True'})
        },
        'skcrm.persontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'PersonType', 'db_table': "u'person_types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        'skcrm.phone': {
            'Meta': {'ordering': "['-primary']", 'object_name': 'Phone', 'db_table': "u'contact_phones'"},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skcrm.Contact']", 'null': 'True', 'blank': 'True'}),
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