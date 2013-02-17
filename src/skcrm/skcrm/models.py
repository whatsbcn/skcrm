# coding: utf8

from django.db import models
from django.contrib.auth.models import User
from django.core import urlresolvers


             
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

IVA_TYPE = (
    (0, '0%'),
    (4, '4%'),               
    (10, '10%'),
    (21, '21%'),
) 

IRPF_TYPE = (
    (0, '0%'),               
    (10, '10%'),
    (21, '21%'),
) 

EXPENSE_STATE = [
    (1, 'Pendiente'),
    (2, 'Pagada'),
    (3, 'Domiciliada'),
]

DEFAULT_COUNTRY_ID = 73
DEFAULT_REGION_ID = 33
DEFAULT_CITY_ID = 899

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'countries'
        ordering = ['name']
        verbose_name_plural = "Países"        
    def __unicode__(self):
        return self.name   
    def get_default(self):
        return Country.objects.get(name='Estaña') 

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

class ExpenseDocumentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'expense_document_types'
        ordering = ['name']
        verbose_name_plural = "Tipos de documento"
    def __unicode__(self):
        return self.name 
    
class ExpenseConceptType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'expense_concept_types'
        ordering = ['name']
        verbose_name_plural = "Conceptos de gasto"
    def __unicode__(self):
        return self.name 
        
class ExpenseConceptSubType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    concept_type = models.ForeignKey(ExpenseConceptType, null=False, blank=False, verbose_name="Concepto")
    class Meta:
        db_table = u'expense_concept_subtypes'
        ordering = ['name']
        verbose_name_plural = "Subconceptos de gasto"
    def __unicode__(self):
        return self.name 
    
class ContactDataType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'contact_data_types'
        ordering = ['name']
        verbose_name_plural = "Tipo de datos de contacto"
    def __unicode__(self):
        return self.name  
                
class Sector(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=False, verbose_name="Nombre")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child', verbose_name="Sector Padre")
    class Meta:
        db_table = u'sectors'
        ordering = ['parent__parent__name', 'parent__name', 'name']
        verbose_name_plural = "Sectores"
    def __unicode__(self):
        ret = ""
        p = self.parent
        while p != None:
            ret += unicode(p) + " - "
            p = p.parent   
        return ret + self.name
    
    def number_of_childs(self):
        s = Sector.objects.all().filter(parent=self)
        return len(s)

class Section(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=False, verbose_name="Nombre")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child', verbose_name="Sección Padre")
    class Meta:
        db_table = u'section'
        ordering = ['parent__parent__name', 'parent__name', 'name']
        verbose_name_plural = "Secciones"
    def __unicode__(self):
        ret = ""
        p = self.parent
        while p != None:
            ret += unicode(p) + " - "
            p = p.parent   
        return ret + self.name
    def number_of_childs(self):
        s = Section.objects.all().filter(parent=self)
        return len(s)        

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    cognoms = models.CharField(max_length=200, blank=True, verbose_name="Apellidos")
    surname = models.CharField(max_length=100, blank=True, verbose_name="Sobrenombre")
    treatment = models.ForeignKey(ContactTreatment, null=True, blank=True, verbose_name="Tratamiento")
    born_date = models.DateField(null=True, blank=True, verbose_name="Fecha nacimiento")
    
    #email = models.EmailField(max_length=45, blank=True)
    #address = models.CharField(max_length=100, blank=True, verbose_name="Dirección")
    #packets_address = models.CharField(max_length=100, blank=True, verbose_name="Dirección para paquetes")
    #postal_code = models.CharField(max_length=32, blank=True, verbose_name="Código postal")
    #country = models.ForeignKey(Country, default=DEFAULT_COUNTRY_ID, null=True, blank=True, verbose_name="País")
    #region = models.ForeignKey(Region, default=DEFAULT_REGION_ID, null=True, blank=True, verbose_name="Provincia")
    #city = models.ForeignKey(City, default=DEFAULT_CITY_ID, null=True, blank=True, verbose_name="Ciudad")
    website = models.URLField(max_length=100, blank=True, verbose_name="Página web")
    #mailing = models.BooleanField(verbose_name="Consiente que se le envien emails?")
    # Per els contactes que volem tenir però no voldrem convidar mai, ni enviar-lis coses
    disabled = models.BooleanField(verbose_name="Contacto desactivado?")
    NIF_CIF = models.CharField(max_length=45, blank=True, verbose_name="NIF/CIF")    
    #cognom2 = models.CharField(max_length=100, blank=True)
    #has_personal_assistant = models.ForeignKey('self', null=True, blank=True)
    type = models.ManyToManyField(PersonType, db_table="rel_person_types", null=True, blank=True, verbose_name="Tipo")
    sections = models.ManyToManyField(Section, db_table="rel_person_section", null=True, blank=True, verbose_name="Secciones")
    #positions = models.ManyToManyField('Company', through='ContactPosition', null=True, blank=True)
    class Meta:
        db_table = u'person'
        ordering = ['name']
        verbose_name_plural = "Personas"
    def __unicode__(self):
        return self.name + " " + self.cognoms
    def save(self, *args, **kwargs):
        if getattr(self, 'name', True):
            self.name = self.name.title()
        if getattr(self, 'cognoms', True):
            self.cognoms = self.cognoms.title()            
        if getattr(self, 'surname', True):
            self.surname = self.surname.title()   
        super(Person, self).save(*args, **kwargs)     
        
#class Contact(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=100, verbose_name="Nombre")
#    #email = models.EmailField(max_length=45, blank=True)
#    address = models.CharField(max_length=100, blank=True, verbose_name="Dirección")
#    packets_address = models.CharField(max_length=100, blank=True, verbose_name="Dirección para paquetes")
#    postal_code = models.CharField(max_length=32, blank=True, verbose_name="Código postal")
#    country = models.ForeignKey(Country, default=DEFAULT_COUNTRY_ID, null=True, blank=True, verbose_name="País")
#    region = models.ForeignKey(Region, default=DEFAULT_REGION_ID, null=True, blank=True, verbose_name="Provincia")
#    city = models.ForeignKey(City, default=DEFAULT_CITY_ID, null=True, blank=True, verbose_name="Ciudad")
#    
#    website = models.URLField(max_length=100, blank=True, verbose_name="Página web")
#    mailing = models.BooleanField(verbose_name="Consiente que se le envien emails?")
#    # Per els contactes que volem tenir però no voldrem convidar mai, ni enviar-lis coses
#    disabled = models.BooleanField(verbose_name="Contacto desactivado?")
#    NIF_CIF = models.CharField(max_length=45, blank=True, verbose_name="NIF/CIF")
#    class Meta:
#        db_table = u'contacts'
#        ordering = ['name']
#        verbose_name_plural = "Contactos"
#    def __unicode__(self):
#        return self.name
    
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    comercial_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre comercial")
    email = models.EmailField(max_length=45, blank=True) # TODO a borrar
    website = models.URLField(max_length=100, blank=True, verbose_name="Página web")
    #disabled = models.BooleanField(verbose_name="Contacto desactivado?")
    NIF_CIF = models.CharField(max_length=45, blank=True, verbose_name="NIF/CIF")    
    account_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Número de cuenta")  
    type = models.ManyToManyField(CompanyType, db_table="rel_company_types", null=True, blank=True, verbose_name="Tipo")
    context = models.ForeignKey(ContextType, null=True, blank=True, verbose_name="Ámbito")
    is_group = models.BooleanField(verbose_name="Es un grupo de empresas")
    in_group = models.ForeignKey('Company', null=True, blank=True, limit_choices_to= {"is_group" : True}, verbose_name="Permeneze al grupo")    
    
    account_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Número de cuenta")

    class Meta:
        db_table = u'company'
        ordering = ['name']
        verbose_name_plural = "Empresas"
    def __unicode__(self):
        if self.comercial_name:
            return self.comercial_name
        return self.name
    def get_absolute_url(self):
        return urlresolvers.reverse('non_admin:company_edit', args=(self.id,))
    def save(self, *args, **kwargs):
        if getattr(self, 'name', True):
            self.name = self.name.title()
        if getattr(self, 'comercial_name', True):
            self.comercial_name = self.comercial_name.title()
        super(Company, self).save(*args, **kwargs)     
    
class Media(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    website = models.URLField(max_length=100, blank=True, verbose_name="Página web")
    #mailing = models.BooleanField(verbose_name="Consiente que se le envien emails?")
    # Per els contactes que volem tenir però no voldrem convidar mai, ni enviar-lis coses
    #disabled = models.BooleanField(verbose_name="Contacto desactivado?")
    #NIF_CIF = models.CharField(max_length=45, blank=True, verbose_name="NIF/CIF")     
    type = models.ForeignKey(MediaType, null=True, blank=True, verbose_name="Tipo")
    context = models.ForeignKey(ContextType, null=True, blank=True, verbose_name="Contexto")
    sectors = models.ManyToManyField(Sector, db_table="rel_company_sectors", null=True, blank=True, verbose_name="Sectores")
    ditribution = models.ForeignKey(DistributionType, null=True, blank=True, verbose_name="Distribución")
    periodicity = models.ForeignKey(PeriodicityType, null=True, blank=True, verbose_name="Periodicidad")
    company = models.ForeignKey(Company, null=False, blank=False, verbose_name="Empresa")
    class Meta:
        db_table = u'media'
        verbose_name_plural = "Medios"
        ordering = ['name']
    def __unicode__(self):
        return unicode(self.name) 
    def save(self, *args, **kwargs):
        if getattr(self, 'name', True):
            self.name = self.name.title()
        super(Media, self).save(*args, **kwargs)     
    
           

class ContactData(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, null=True, blank=False)
    company = models.ForeignKey(Company, null=True, blank=False, verbose_name="Empresa")
    media = models.ForeignKey(Media, null=True, blank=True, verbose_name="Medio")
    position = models.ForeignKey(PositionTypes, null=True, blank=False, verbose_name="Cargo")
    type = models.ForeignKey(ContactDataType, null=False, blank=False)
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name="Descripción")
    address = models.CharField(max_length=100, blank=True, verbose_name="Dirección")
    packets_address = models.CharField(max_length=100, blank=True, verbose_name="Dirección para paquetes")
    postal_code = models.CharField(max_length=32, null=True, blank=True, verbose_name="Código postal")
    country = models.ForeignKey(Country, null=True, blank=True, verbose_name="País")
    region = models.ForeignKey(Region, null=True, blank=True, verbose_name="Provincia")
    city = models.ForeignKey(City, null=True, blank=True, verbose_name="Ciudad")
    telf_static = models.CharField(max_length=100, null=True, blank=True, verbose_name="Telf. fijo")
    telf_movile = models.CharField(max_length=100, null=True, blank=True, verbose_name="Telf. mobil")
    fax = models.CharField(max_length=100, null=True, blank=True, verbose_name="Fax")
    email = models.CharField(max_length=100, blank=True, verbose_name="Email")
    email_alt = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email alternativo")
    mailing = models.BooleanField(default=True, verbose_name="Consiente que se le envien emails?")
    class Meta:
        db_table = u'contact_data'
        #ordering = ['name']
        verbose_name_plural = "Datos de contacto"
    def __unicode__(self):
        return unicode(self.person) + " - " +  unicode(self.company) + " - " + unicode(self.media)
    
class Ot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, verbose_name="Nombre")
    number = models.IntegerField(unique=True, verbose_name="Número de OT", null=True, blank=True)
    company = models.ForeignKey(Company, null=False, blank=False, verbose_name="Empresa")
    class Meta:
        db_table = u'ot'
        verbose_name_plural = "Ots"
    def __unicode__(self):
        return unicode(self.number) + ": [" + unicode(self.company.comercial_name) + "] " + self.name
    def save(self, force_insert=False, force_update=False):
        if self.number == None:
            from django.db.models import Max
            self.number = Ot.objects.all().aggregate(Max('number'))['number__max'] + 1
        super(Ot, self).save(force_insert, force_update)
        
class Expense(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="#")
    doc_type = models.ForeignKey(ExpenseDocumentType, null=True, blank=True, verbose_name="Tipo")
    doc_num = models.CharField(max_length=64, null=True, blank=True, verbose_name="#Doc.")
    date = models.DateField(blank=True, verbose_name="Fecha")    
    state = models.IntegerField(choices=EXPENSE_STATE, default=1, verbose_name="Estado")
    payment_date = models.DateField(blank=True, verbose_name="F. pago")
    provider = models.ForeignKey(Company, limit_choices_to= {"type" : 1}, verbose_name="Proveedor", null=True, blank=True)
    irpf = models.IntegerField(null=False, blank=False, choices=IRPF_TYPE, default=0, verbose_name="%IRPF")
    class Meta:
        db_table = u'expense'
        ordering = ['-id']
        verbose_name_plural = "Gastos"
    def __unicode__(self):
        return unicode(self.id)
    def base(self):
        base = 0
        for item in self.expenseitem_set.all():
            base += item.base
        return base
    def iva(self):
        percent = []
        for item in self.expenseitem_set.all():
            if item.iva not in percent:
                percent.append(item.iva)
        return percent    
    def iva_value(self):
        iva = 0
        for item in self.expenseitem_set.all():
            iva += (item.base * item.iva)/100
        return iva
    def irpf_value(self):
        return (self.base()*self.irpf)/100
    def total(self):
        ret = 0
        for item in self.expenseitem_set.all():
            ret += item.total() 
        return ret
    def resume_data(self):
        table_resume_data = []
        total = 0
        for iva_item, iva_desc in IVA_TYPE:
            table_resume_data.append({'iva': iva_item, 'total': 0})
            
        for item in self.expenseitem_set.all():
            for table_resume_entry in table_resume_data:
                if table_resume_entry['iva'] == item.iva:
                    table_resume_entry['total'] += item.base
            total += item.base + (item.iva * item.base)/100
        return table_resume_data, total                

class ExpenseItem(models.Model):
    id = models.AutoField(primary_key=True)
    concept_type = models.ForeignKey(ExpenseConceptType, null=False, blank=False, verbose_name="Concepto")
    concept_sub_type = models.ForeignKey(ExpenseConceptSubType, null=True, blank=True, verbose_name="Subconcepto")    
    description = models.TextField(blank=True)
    expense = models.ForeignKey(Expense, verbose_name="#")
    ot = models.ForeignKey(Ot)
    iva = models.IntegerField(choices=IVA_TYPE, verbose_name="%IVA")
    base = models.DecimalField(verbose_name="Base", max_digits=6, decimal_places=2)    
    class Meta:
        db_table = u'expense_item'
        ordering = ['-id']
        verbose_name_plural = "Detalle de gasto"
    def __unicode__(self):
        return unicode(self.id)
    def total(self):
        return self.base + (self.base * self.iva / 100)
                
#class Phone(models.Model):
#    id = models.AutoField(primary_key=True)
#    number = models.IntegerField()
#    type = models.ForeignKey(PhoneType, null=True, blank=True)
#    contact_data = models.ForeignKey('ContactData', null=True, blank=True)
#    primary = models.BooleanField(verbose_name="Principal")                     
#    class Meta:
#        db_table = u'contact_phones'
#        verbose_name_plural = "Teléfonos"
#        ordering = ['-primary']        
#    def __unicode__(self):
#        return unicode(self.number)         
#                
#class Email(models.Model):
#    id = models.AutoField(primary_key=True)
#    email = models.EmailField(max_length=45, blank=True)
#    type = models.ForeignKey(EmailType, null=True, blank=True)
#    contact_data = models.ForeignKey('ContactData', null=True, blank=True)
#    primary = models.BooleanField(verbose_name="Principal")                
#    class Meta:
#        db_table = u'contact_emails'
#        verbose_name_plural = "Emails"
#        ordering = ['-primary']
#    def __unicode__(self):
#        return unicode(self.email)         


        
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


