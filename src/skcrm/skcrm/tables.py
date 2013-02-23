# coding: utf8
import django_tables2 as tables
from skcrm.models import Person, Expense, ExpenseItem
from django.utils.safestring import mark_safe
from django_tables2.utils import A
from django.utils.html import escape

class SectionTable(tables.Table):
    name = tables.Column(verbose_name='Secciones')
    #number_of_childs = tables.Column(verbose_name='Cantidad de subsecciones', orderable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}

    def render_actions(self, value, record):
        ret = "<a href='/section/edit/%s'><i class='icon-pencil'></i>&nbsp;</a>" % record.id
        return ret
    
class MediasTable(tables.Table):
    name = tables.Column(verbose_name='Medios')
    #number_of_childs = tables.Column(verbose_name='Cantidad de subsectores', orderable=False)
    actions = tables.TemplateColumn("<a href='/media/edit/{{ record.id }}'><i class='icon-pencil'></i>&nbsp;</a>", verbose_name="Acciones")
    #actions = tables.Column(verbose_name='Acciones', accessor="id")

    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}


class ExpenseConceptTypeTable(tables.Table):
    name = tables.Column(verbose_name='Concepto de gasto')
    actions = tables.TemplateColumn("<a href='/concept_type/edit/{{ record.id }}'><i class='icon-pencil'></i>&nbsp;</a>", verbose_name="Acciones")

    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}

class ExpenseConceptSubTypeTable(tables.Table):
    name = tables.Column(verbose_name='Subconcepto de gasto')
    actions = tables.TemplateColumn("<a href='/sub_concept_type/edit/{{ record.id }}'><i class='icon-pencil'></i>&nbsp;</a>", verbose_name="Acciones")

    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}

class CompaniesTable(tables.Table):
    name = tables.Column(verbose_name='Empresa')
    comercial_name = tables.Column(verbose_name='Nombre comercial')
    #number_of_childs = tables.Column(verbose_name='Cantidad de subsectores', orderable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")
    #id = tables.Column(verbose_name='#')
    #name = tables.LinkColumn('empreses', args=[id])
    
    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}

    def render_actions(self, value):
        #ret = "<a href='/company/edit/"+ str(value) + "'><i class='icon-search'></i>&nbsp;</a>"
        ret = " <a href='/company/edit/"+ str(value) + "'><i class='icon-pencil'></i>&nbsp;</a>"           
        return mark_safe(ret)

class OtTable(tables.Table):
    number = tables.Column(verbose_name='Número')
    name = tables.Column(verbose_name='Nombre')
    #actions = tables.Column(verbose_name='Acciones', accessor="id")
    actions = tables.TemplateColumn("<a href='/company/{{ record.company.id }}/del_ot/{{ record.id }}'><i class='icon-trash'></i>&nbsp;</a>", verbose_name="Acciones")
    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}

class ExpenseTable(tables.Table):
    total = tables.Column(verbose_name='Total Fac.', attrs={"td": {"style": "text-align: right"}})
    actions = tables.TemplateColumn("<a href='/expense/edit/{{ record.id }}'><i class='icon-pencil'></i>&nbsp;</a>", verbose_name="Acciones")
    
    class Meta:
        model = Expense
        attrs = {"class": "table table-bordered table-condensed table-stripped"}
        exclude = ('payment_date', 'irpf')
        
    def render_payment_date(self, value):
        if not value:
            return ""
        else:
            return value

    def render_doc_num(self, value):
        if not value:
            return ""
        else:
            return value
    def render_total(self, value):
        ret = "%.2f" % value
        return ret.replace('.', ',')
    
    def render_provider(self, value):
        if not value:
            return ""

        return value        

class ExpenseDetailTable(tables.Table):
    sub_concepts = tables.Column(verbose_name='Subconceptos', default="")
    irpf_value = tables.Column(verbose_name='IRPF', attrs={"td": {"style": "text-align: right"}})
    iva = tables.Column(verbose_name='% IVA', attrs={"td": {"style": "text-align: right"}})
    iva_value = tables.Column(verbose_name='IVA', attrs={"td": {"style": "text-align: right"}})
    base = tables.Column(verbose_name='Base', attrs={"td": {"style": "text-align: right"}})
    total = tables.Column(verbose_name='Total Fac.', attrs={"td": {"style": "text-align: right"}})
    
    class Meta:
        model = Expense
        attrs = {"class": "table table-bordered table-condensed table-stripped", "style": "font-size:12px"}
        exclude = ('payment_date',)
    def render_sub_concepts(self, value):
        ret = u""
        for item in value:
            ret += item + u"</br>"
        return ret
    def render_payment_date(self, value):
        if not value:
            return ""
        else:
            return value

    def render_doc_num(self, value):
        if not value:
            return ""
        else:
            return value    
        
    def render_iva(self, value):
        ret = u""
        for item in value:
            ret += str(item) + "% </br>"
        return ret

    def render_irpf_value(self, value):
        ret = "%.2f" % value
        return ret.replace('.', ',')

    def render_iva_value(self, value):
        ret = "%.2f" % value
        return ret.replace('.', ',')

    def render_base(self, value):
        ret = "%.2f" % value
        return ret.replace('.', ',')
    
    def render_total(self, value):
        ret = "%.2f" % value
        return ret.replace('.', ',')


class ExpenseItemTable(tables.Table):
    total = tables.Column(verbose_name='Total Fac.')
    actions = tables.TemplateColumn("<a href='/expense/{{ record.expense.id }}/del_item/{{ record.id }}'><i class='icon-trash'></i>&nbsp;</a>", verbose_name="Acciones")
    
    class Meta:
        model = ExpenseItem
        fields = ('concept_type', 'iva', 'base', 'description', 'ot')
        attrs = {"class": "table table-bordered"}

class ExpenseItemDetailTable(tables.Table):
    doc_num = tables.Column(accessor="expense.doc_num", default='')
    date = tables.Column(accessor="expense.date", default='')
    #expense_id = tables.Column(accessor="expense.id", verbose_name="Número de registro")
    iva = tables.Column(attrs={"td": {"style": "text-align: right"}})
    base = tables.Column(attrs={"td": {"style": "text-align: right"}})
    total = tables.Column(verbose_name='Total', attrs={"td": {"style": "text-align: right"}})
    
    class Meta:
        model = ExpenseItem
        exclude = ('ot', 'id', 'concept_sub_type')
        sequence = ('expense', 'doc_num', 'date', 'concept_type', 'description', 'iva', 'base', 'total')
        attrs = {"class": "table table-condensed table-bordered table-stripped"}

    def render_base(self, value):
        ret = "%.2f" % value
        return ret.replace('.', ',')

    def render_total(self, value):
        ret = "%.2f" % value
        return ret.replace('.', ',')
    
    def render_payment_date(self, value):
        if not value:
            return ""
        else:
            return value 

class ResumeTable(tables.Table):
    iva = tables.Column(verbose_name="IVA")
    total = tables.Column(verbose_name='Base')
    class Meta:
        attrs = {"class": "table table-condensed table-bordered"}
        orderable = False
        
class SectorTable(tables.Table):
    name = tables.Column(verbose_name='Sector')
    #number_of_childs = tables.Column(verbose_name='Subsectores', orderable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}

    def render_actions(self, value, record):
        ret = "<a href='/sector/edit/%s'><i class='icon-pencil'></i>&nbsp;</a>" % record.id
        return ret
    
class PersonTable(tables.Table):
    
    #email = tables.EmailColumn(verbose_name='Email')
    name = tables.Column(verbose_name='Nombre', order_by=("name", "cognom1", "cognom2"))
    cognoms = tables.Column(verbose_name='Primer Apellido')

    #medias = tables.Column(verbose_name='Medios') 
    sections = tables.Column(verbose_name='secciones', accessor="sections")
    #phone  = tables.Column(verbose_name='Teléfono', accessor="phone_set")
    #positions = tables.Column(verbose_name='Cargos', accessor="contactposition_set")
    #actions = tables.Column(verbose_name='Acciones', accessor="id")
    actions = tables.TemplateColumn("""
    <a href='{% url person_edit record.id %}'><i class='icon-pencil'></i>&nbsp;</a>
    """, verbose_name="Acciones")

    #twitter = tables.Column(verbose_name='Twiter')
    #facebook = tables.Column(verbose_name='Facebook')
    
    #city = tables.Column(verbose_name='Ciudad')

    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped", 'cellspacing': '0'}    
    def render_sections(self, value):
        ret = u""
        for section in value.all():
            ret += unicode(section.name) + u"</br>"
        return mark_safe(ret)      
    
#    def render_phone(self, value):
#        ret = ""
#        for telf in value.all():
#            ret += str(telf.number) + "</br>"
#        return mark_safe(ret)      
      
#    def render_positions(self, value):
#        ret = ""
#        for rel in value.all():
#            ret += rel.type.name + " (" + rel.company.name + ")</br>"
#        return mark_safe(ret)
    
    def render_medias(self, value):
        ret = u""
        for media in value.all():
            ret += media.name + "</br>"
        return mark_safe(ret)
    
class PersonContactDataTable(tables.Table):
    description = tables.Column(default='')
    company = tables.Column(default='')
    media = tables.Column(default='')
    position = tables.Column(order_by=("position.name"))
    address = tables.Column()
    #packets_address = tables.Column()
    telf = tables.Column()
    email  = tables.Column()
    actions = tables.TemplateColumn("""
    <a href='/person/{{ record.person.id }}/edit_cd/{{ record.id }}'><i class='icon-pencil'></i>&nbsp;</a>
    <a href='/person/{{ record.person.id }}/del_cd/{{ record.id }}'><i class='icon-trash'></i>&nbsp;</a>""", orderable=False, verbose_name="Acciones")
    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}
    
    def render_address(self, value, record):
        ret = value
        if record.city:
            ret += u" (%s)" % record.city
        return ret
    
    def render_telf(self, value, record):
        ret = u""
        if record.telf_static:
            ret += "T: %s</br>" % record.telf_static
        if record.telf_movile:
            ret += "M: %s</br>" % record.telf_movile
        if record.fax:
            ret += "F: %s</br>" % record.fax 
        return ret    
    
    def render_email(self, value, record):
        ret = "%s" % record.email
        if record.email_alt:
            ret += "</br>%s" % record.email_alt
        return ret
    
class MediaContactDataTable(tables.Table):
    description = tables.Column(default='')
    address = tables.Column()
    #packets_address = tables.Column()
    telf = tables.Column()
    email  = tables.Column()
    actions = tables.TemplateColumn("""
    <a href='/media/{{ record.media.id }}/edit_cd/{{ record.id }}'><i class='icon-pencil'></i>&nbsp;</a>
    <a href='/media/{{ record.media.id }}/del_cd/{{ record.id }}'><i class='icon-trash'></i>&nbsp;</a>""", orderable=False, verbose_name="Acciones")
    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}
    
    def render_address(self, value, record):
        ret = value
        if record.city:
            ret += u", %s" % record.city
        if record.region:
            ret += u" (%s)" % record.region            
        return ret
    
    def render_telf(self, value, record):
        ret = u""
        if record.telf_static:
            ret += "T: %s</br>" % record.telf_static
        if record.telf_movile:
            ret += "M: %s</br>" % record.telf_movile
        if record.fax:
            ret += "F: %s</br>" % record.fax 
        return ret    
    
    def render_email(self, value, record):
        ret = "%s" % record.email
        if record.email_alt:
            ret += "</br>%s" % record.email_alt
        return ret

class CompanyContactDataTable(MediaContactDataTable):
    actions = tables.TemplateColumn("""
    <a href='/company/{{ record.company.id }}/edit_cd/{{ record.id }}'><i class='icon-pencil'></i>&nbsp;</a>
    <a href='/company/{{ record.company.id }}/del_cd/{{ record.id }}'><i class='icon-trash'></i>&nbsp;</a>""", orderable=False, verbose_name="Acciones")
    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped"}
 
        
class ContactTable(tables.Table):
    person = tables.Column(verbose_name='Nombre', order_by=("person.name", "person.cognoms"))
    media = tables.Column(verbose_name='Medio', default='', order_by=("media.name"))
    company = tables.Column(verbose_name='Empresa', default='', order_by=("company.comercial_name"))
    position = tables.Column(verbose_name='Cargo', order_by=("position.name"))
    
    #medias = tables.Column(verbose_name='Medios') 
    #sections = tables.Column(verbose_name='Secciones')
    #phone  = tables.Column(verbose_name='Teléfono', accessor="phone_set")
    #positions = tables.Column(verbose_name='Cargos', accessor="contactposition_set")
    #twitter = tables.Column(verbose_name='Twiter')
    #facebook = tables.Column(verbose_name='Facebook')
    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped", 'cellspacing': '0'}  
        orderable = False
      
    def render_sections(self, value, record):
        ret = u""
        for section in record.person.sections.all():
            ret += str(section.name) + "</br>"
        return mark_safe(ret)
   

class SelectedContactTable(ContactTable):
    #repetitions = tables.Column(empty_values=(), verbose_name="Repeticiones")
    rep = tables.Column(verbose_name="Repeticiones", accessor="person.rep")
    actions = tables.Column(orderable=False)
    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-stripped", 'cellspacing': '0'}    
      
    def render_actions(self, value, record):
        ret = "<a href='/contact/unselect/%s'><i class='icon-remove'></i>&nbsp;</a>" % record.id
        return ret

#    def __init__(self, *args, **kwargs):
#        super(SelectedContactTable, self).__init__(*args, **kwargs)
#        self.counter = []
    