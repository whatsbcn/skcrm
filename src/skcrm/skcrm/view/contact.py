# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Person, ContactData
from skcrm.tables import ContactTable, SelectedContactTable
from skcrm.forms import SearchContactForm, PersonForm 
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode

#@login_required
def ls(request, select=False):   
    search = SearchContactForm()
    people = ContactTable([])
    selection = SelectedContactTable([])
    selection_entries = entries = 0
    if 'selected_contacts' in request.session:
        selection = SelectedContactTable(request.session['selected_contacts'], order_by=request.GET.get('sort'))
        selection.paginate(page=request.GET.get('page', 1), per_page=25)
        selection_entries = len(request.session['selected_contacts'])

    if request.method == 'POST':
        search = SearchContactForm(request.POST, request.FILES)
        if search.is_valid():
            # Filter people
            found_people = ContactData.objects.select_related().distinct().filter(type_id=1)
            if request.user.groups.filter(name='Sociedad').count() == 0:
                found_people = found_people.exclude(person__type=2)

            if search.cleaned_data['name']:
                found_people = found_people.filter(person__name__icontains=search.cleaned_data['name'])                
            if search.cleaned_data['company']:
                found_people = found_people.filter(company__name__icontains=search.cleaned_data['company'])
            if search.cleaned_data['media']:
                found_people = found_people.filter(media__name__icontains=search.cleaned_data['media'])                                    
            if search.cleaned_data['sector']:
                found_people = found_people.filter(Q(media__sectors__id=search.cleaned_data['sector'])|
                                                   Q(media__sectors__parent__id=search.cleaned_data['sector']))
            if search.cleaned_data['tipo_medio']:
                found_people = found_people.filter(media__type__id=search.cleaned_data['tipo_medio'])
            if search.cleaned_data['section']:
                found_people = found_people.filter(Q(person__sections__id=search.cleaned_data['section'])|
                                                   Q(person__sections__parent__id=search.cleaned_data['section']))                
            if search.cleaned_data['carrec']:
                found_people = found_people.filter(position__id=search.cleaned_data['carrec'])            
            if search.cleaned_data['language']:
                found_people = found_people.filter(person__language__id=search.cleaned_data['language'])
            if search.cleaned_data['city']:
                found_people = found_people.filter(city__id=search.cleaned_data['city'])
            if search.cleaned_data['region']:
                found_people = found_people.filter(region__id=search.cleaned_data['region'])  
            if search.cleaned_data['country']:
                found_people = found_people.filter(country__id=search.cleaned_data['country'])
            if search.cleaned_data['withmail']:
                found_people = found_people.filter(email__isnull=False, email__contains='@')
            if search.cleaned_data['mailing']:
                found_people = found_people.filter(mailing=True)

            entries = len(found_people)
            people = ContactTable(found_people[:25])
            #people.paginate(page=request.GET.get('page', 1), per_page=25)

            # Add filtered people to the selected list
            if select:
                people = ContactTable([])
                if 'selected_contacts' in request.session:
                    new_people = set(list(found_people)) - request.session['selected_contacts']
                    request.session['selected_contacts'] |= new_people
                else:
                    request.session['selected_contacts'] = set(list(found_people))
                return redirect('contact_list')

    return render_to_response('contacts.html',
                              {'form': search, 'table_entries': entries, 'table': people,
                               'selection': selection, 'selection_entries': selection_entries}, 
                              context_instance=RequestContext(request))

@login_required
def reset(request):
    try:
        del request.session['selected_contacts']
    except:
        pass

    return redirect('contact_list')


@login_required
def export(request):
    import xlwt
    export_fields = ["Email", "Nombre", "Apellidos", "Cargos", "Medio", "Empresa", u"Teléfonos", "Secciones", u"Dirección", u"Código postal", "Ciudad", u"País", "Idioma"]
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=export.xls'
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Contactos')
    
    i = 0
    j = 0
    for field in export_fields:
        ws.write(i, j, field)
        j += 1
        
    i = 1   
    for contact in request.session['selected_contacts']:
        try:
            ws.write(i, 0, contact.email)
        except:
            ws.write(i, 0, "")
        
        try:
            ws.write(i, 1, contact.person.name)
        except:
            ws.write(i, 1, "")
        
        try:
            ws.write(i, 2, contact.person.cognoms)
        except:
            ws.write(i, 2, "")

        try:
            ws.write(i, 3, contact.position.name)
        except:
            ws.write(i, 3, "")

        try:
            ws.write(i, 4, contact.media.name)
        except:
            ws.write(i, 4, "")

        try:
            ws.write(i, 5, contact.company.name)
        except:
            ws.write(i, 5, "")

        try:
            list = ""
            if contact.telf_static:
                list += "T: %s," % contact.telf_static
            if contact.telf_movile:
                list += "M: %s," % contact.telf_movile
            if contact.fax:
                list += "F: %s" % contact.fax
            ws.write(i, 6, list)
        except:
            ws.write(i, 6, "")

        try:
            list = ""
            for section in contact.person.sections.all():
                list = list + section.name + ", "
            ws.write(i, 7, list)
        except:
            ws.write(i, 7, "")

        try:
            ws.write(i, 8, contact.address)
        except:
            ws.write(i, 8, "")

        try:
            ws.write(i, 9, contact.postal_code)
        except:
            ws.write(i, 9, "")

        try:
            ws.write(i, 10, contact.city.name)
        except:
            ws.write(i, 10, "")

        try:
            ws.write(i, 11, contact.country.name)
        except:
            ws.write(i, 11, "")

        try:
            ws.write(i, 12, contact.person.language.name)
        except:
            ws.write(i, 12, "")

        i += 1


    wb.save(response)
    
#     LogEntry.objects.log_action(
#                                 user_id=request.user.pk, 
#                                 content_type_id = ContentType.objects.get_for_model(ContactData).pk,
#                                 object_id       = ContactData.pk,
#                                 object_repr     = force_unicode(ContactData), 
#                                 action_flag     = ADDITION,
#                                 change_message  = "Exportats %d contactes" % len(request.session['selected_contacts'])
#     )

    
    return response
    
    
@login_required         
def unselect(request, id=None):
        if id:
            cd = get_object_or_404(ContactData, pk=id)
            request.session['selected_contacts'] -= set([cd])
            return redirect('contact_list')
        else:
            return redirect('contact_list')
        
#@login_required         
#def edit(request, id=None):         
#        if id:
#            person = get_object_or_404(Person, pk=id)
#        else:
#            person = Person()
#                                    
#        form = PersonForm(instance=person)
#        #table = PersonTable(company.ot_set.all(), order_by=request.GET.get('sort'))
#        #rel_form = OtForm()
#
#        if request.POST:
#            form = PersonForm(request.POST, instance=person)
#            if form.is_valid():
#                person = form.save()
#                messages.success(request, "Cambios guardados correctamente.")              
#                return redirect('contact_edit', id=person.id)
#            
#        return render_to_response('contact_edit.html', 
#                                  {'form':form, 'obj':person}, 
#                                  context_instance=RequestContext(request))
