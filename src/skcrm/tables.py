# coding: utf8
import django_tables2 as tables
from skcrm.models import Person 
from django.utils.safestring import mark_safe
from django_tables2.utils import A

class SectionsTable(tables.Table):
    name = tables.LinkColumn('skcrm.views.sections', args=[A('id')],verbose_name='Secciones')
    number_of_childs = tables.Column(verbose_name='Cantidad de subsecciones', sortable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    def render_actions(self, value):
        ret = "<ul>"
        ret += "<li class='change-link'><a href='/admin/skcrm/section/"+ str(value) + "/'></a></li>"
        ret += "</ul>"
        return mark_safe(ret)
    
class MediasTable(tables.Table):
    name = tables.Column(verbose_name='Medios')
    #number_of_childs = tables.Column(verbose_name='Cantidad de subsectores', sortable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    def render_actions(self, value):
        ret = "<ul>"
        ret += "<li class='change-link'><a href='/admin/skcrm/media/"+ str(value) + "/'></a></li>"
        ret += "</ul>"
        return mark_safe(ret)

class CompaniesTable(tables.Table):
    name = tables.Column(verbose_name='Empresa')
    #number_of_childs = tables.Column(verbose_name='Cantidad de subsectores', sortable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    def render_actions(self, value):
        ret = "<ul>"
        ret += "<li class='change-link'><a href='/admin/skcrm/company/"+ str(value) + "/'></a></li>"
        ret += "</ul>"
        return mark_safe(ret)

class SectorsTable(tables.Table):
    name = tables.LinkColumn('skcrm.views.sectors', args=[A('id')], verbose_name='Sector')
    number_of_childs = tables.Column(verbose_name='Cantidad de subsectores', sortable=False)
    actions = tables.Column(verbose_name='Acciones', accessor="id")

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
    actions = tables.Column(verbose_name='Acciones', accessor="id")

    #twitter = tables.Column(verbose_name='Twiter')
    #facebook = tables.Column(verbose_name='Facebook')
    
    #city = tables.Column(verbose_name='Ciudad')
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
    
    
    
    def render_actions(self, value):
        ret = "<ul>"
        ret += "<li class='change-link'><a href='/admin/skcrm/person/"+ str(value) + "/'></a></li>"
        ret += "<li class='delete-link'><a href='/unselect/"+ str(value) + "/'></a></li>"
        ret += "</ul>"
        return mark_safe(ret)
    
    class Meta:
        attrs = {'cellspacing': '0'}
        #order_by = 'name'
        #model = Person
        #sequence = ("email", "name", "cognom1", "cognom2", "cargos", "...")