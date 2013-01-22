# coding: utf8
import django_tables2 as tables
from skcrm.models import Person, Expense, ExpenseItem
from django.utils.safestring import mark_safe
from django_tables2.utils import A
from django.utils.html import escape

class SectionsTable(tables.Table):
    name = tables.LinkColumn('skcrm.views.sections', args=[A('id')],verbose_name='Secciones')
    number_of_childs = tables.Column(verbose_name='Cantidad de subsecciones', orderable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    class Meta:
        attrs = {"class": "table table-bordered"}

    def render_actions(self, value):
        ret = "<ul>"
        ret += "<li class='change-link'><a href='/admin/skcrm/section/"+ str(value) + "/'></a></li>"
        ret += "</ul>"
        return mark_safe(ret)
    
class MediasTable(tables.Table):
    name = tables.Column(verbose_name='Medios')
    #number_of_childs = tables.Column(verbose_name='Cantidad de subsectores', orderable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    class Meta:
        attrs = {"class": "table table-bordered"}

    def render_actions(self, value):
        ret = "<ul>"
        ret += "<li class='change-link'><a href='/admin/skcrm/media/"+ str(value) + "/'></a></li>"
        ret += "</ul>"
        return mark_safe(ret)

class CompaniesTable(tables.Table):
    name = tables.Column(verbose_name='Empresa')
    #number_of_childs = tables.Column(verbose_name='Cantidad de subsectores', orderable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")
    #id = tables.Column(verbose_name='#')
    #name = tables.LinkColumn('empreses', args=[id])
    
    class Meta:
        attrs = {"class": "table table-bordered"}

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
        attrs = {"class": "table table-bordered"}

class ExpenseTable(tables.Table):
    total = tables.Column(verbose_name='Total Fac.')
    actions = tables.TemplateColumn("<a href='/expense/edit/{{ record.id }}'><i class='icon-pencil'></i>&nbsp;</a>", verbose_name="Acciones")
    
    class Meta:
        model = Expense
        attrs = {"class": "table table-bordered"}
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

class ExpenseDetailTable(tables.Table):
    irpf_value = tables.Column(verbose_name='IRPF')
    iva = tables.Column(verbose_name='% IVA')
    iva_value = tables.Column(verbose_name='IVA')
    base = tables.Column(verbose_name='Base')
    total = tables.Column(verbose_name='Total Fac.')
    
    class Meta:
        model = Expense
        attrs = {"class": "table table-bordered"}
        exclude = ('payment_date',)
        
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
        ret = ""
        for item in value:
            ret += str(item) + "% </br>"
        return ret

class ExpenseItemTable(tables.Table):
    total = tables.Column(verbose_name='Total Fac.')
    actions = tables.TemplateColumn("<a href='/expense/{{ record.expense.id }}/del_item/{{ record.id }}'><i class='icon-trash'></i>&nbsp;</a>", verbose_name="Acciones")
    
    class Meta:
        model = ExpenseItem
        fields = ('concept_type', 'iva', 'base', 'description', 'ot')
        attrs = {"class": "table table-bordered"}

class ExpenseItemDetailTable(tables.Table):
    doc_num = tables.Column(accessor="expense.doc_num")
    date = tables.Column(accessor="expense.date")
    #expense_id = tables.Column(accessor="expense.id", verbose_name="Número de registro")
    iva = tables.Column(attrs={"td": {"style": "text-align: right"}})
    base = tables.Column(attrs={"td": {"style": "text-align: right"}})
    total = tables.Column(verbose_name='Total', attrs={"td": {"style": "text-align: right"}})
    
    class Meta:
        model = ExpenseItem
        exclude = ('ot', 'id', 'concept_sub_type')
        sequence = ('expense', 'doc_num', 'date', 'concept_type', 'description', 'iva', 'base', 'total')
        attrs = {"class": "table table-condensed table-bordered"}

    def render_base(self, value):
        return str("%.2f €" % value)

    def render_total(self, value):
        return str("%.2f €" % value)
    
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

class ResumeTable(tables.Table):
    iva = tables.Column(verbose_name="IVA")
    total = tables.Column(verbose_name='Base')
    class Meta:
        attrs = {"class": "table table-condensed table-bordered"}
        orderable = False
        
class SectorsTable(tables.Table):
    name = tables.LinkColumn('skcrm.views.sectors', args=[A('id')], verbose_name='Sector')
    number_of_childs = tables.Column(verbose_name='Cantidad de subsectores', orderable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    class Meta:
        attrs = {"class": "table table-bordered"}

    def render_actions(self, value):
        ret = "<ul>"
        ret += "<li class='change-link'><a href='/admin/skcrm/sector/"+ str(value) + "/'></a></li>"
        ret += "</ul>"
        return mark_safe(ret)
    
class PersonaTable(tables.Table):
    #email = tables.EmailColumn(verbose_name='Email')
    name = tables.Column(verbose_name='Nombre', order_by=("name", "cognom1", "cognom2"))
    cognoms = tables.Column(verbose_name='Primer Apellido')

    #medias = tables.Column(verbose_name='Medios') 
    sections = tables.Column(verbose_name='secciones', accessor="sections")
    phone  = tables.Column(verbose_name='Teléfono', accessor="phone_set")
    positions = tables.Column(verbose_name='Cargos', accessor="contactposition_set")
    #actions = tables.Column(verbose_name='Acciones', accessor="id")
    actions = tables.TemplateColumn("""
    <a href='{% url contact_edit record.id %}'><i class='icon-pencil'></i>&nbsp;</a>
    <a href='{% url contact_unselect record.id %}'><i class='icon-trash'></i>&nbsp;</a>
    """, verbose_name="Acciones")

    #twitter = tables.Column(verbose_name='Twiter')
    #facebook = tables.Column(verbose_name='Facebook')
    
    #city = tables.Column(verbose_name='Ciudad')

    class Meta:
        attrs = {"class": "table table-bordered", 'cellspacing': '0'}    
    def render_sections(self, value):
        ret = ""
        for section in value.all():
            ret += str(section.name) + "</br>"
        return mark_safe(ret)      
    
    def render_phone(self, value):
        ret = ""
        for telf in value.all():
            ret += str(telf.number) + "</br>"
        return mark_safe(ret)      
      
    def render_positions(self, value):
        ret = ""
        for rel in value.all():
            ret += rel.type.name + " (" + rel.company.name + ")</br>"
        return mark_safe(ret)
    
    def render_medias(self, value):
        ret = ""
        for media in value.all():
            ret += media.name + "</br>"
        return mark_safe(ret)
    
    

        #order_by = 'name'
        #model = Person
        #sequence = ("email", "name", "cognom1", "cognom2", "cargos", "...")