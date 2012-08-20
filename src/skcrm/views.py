# coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Person
from skcrm.tables import PersonaTable
from skcrm.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

@login_required
def index(request):        

    selection = PersonaTable([])

        
    return render_to_response('index.html', 
                              {'selection':selection}, 
                              context_instance=RequestContext(request)) 

@login_required
def contacts(request):  
    if request.method == 'POST':
        search = SearchForm(request.POST, request.FILES)
        if search.is_valid():
            # Filter people
            found_people = Person.objects.select_related().all()
            if search.cleaned_data['name']:
                found_people = found_people.filter(name__icontains=search.cleaned_data['name'])                
            if search.cleaned_data['company']:
                found_people = found_people.filter(Q(positions__name__icontains=search.cleaned_data['company'])|
                                                   Q(positions__in_group__name__icontains=search.cleaned_data['company']))
            if search.cleaned_data['media']:
                found_people = found_people.filter(positions__media__name__icontains=search.cleaned_data['media'])                                    
            if search.cleaned_data['sector']:
                found_people = found_people.filter(Q(contactposition__media__sectors__id=search.cleaned_data['sector'])|
                                                   Q(contactposition__media__sectors__parent__id=search.cleaned_data['sector']))
            if search.cleaned_data['section']:
                found_people = found_people.filter(Q(sections__id=search.cleaned_data['section'])|
                                                   Q(sections__parent__id=search.cleaned_data['section']))                
            if search.cleaned_data['carrec']:
                found_people = found_people.filter(contactposition__type=search.cleaned_data['carrec'])            
            if search.cleaned_data['ciutat']:
                found_people = found_people.filter(city__id=search.cleaned_data['ciutat'])
            if search.cleaned_data['provincia']:
                found_people = found_people.filter(region__id=search.cleaned_data['provincia'])  
            if search.cleaned_data['withmail']:
                found_people = found_people.filter(email__isnull=False, email__contains='@')

                
            # Add filtered people to the selected list
            if 'add' in request.POST:
                people = PersonaTable([])
                if 'selected_people' in request.session:
                    new_people = set(list(found_people)) - request.session['selected_people']
                    request.session['selected_people'] |= new_people
                else:
                    request.session['selected_people'] = set(list(found_people))
                return HttpResponseRedirect("/contacts/")                   
            # Show filtered people
            else:
                people = PersonaTable(found_people)
                # Paginem la gent seleccionada  
                people.paginate(page=request.GET.get('page', 1), per_page=25)
           
        else:
            people = PersonaTable([])

    else:
        search = SearchForm()
        people = PersonaTable([])
        
    # Mostrem la gent seleccionada    
    search = SearchForm(request.POST, request.FILES)
    if 'selected_people' in request.session:
        selection = PersonaTable(request.session['selected_people'], order_by=request.GET.get('sort'))
    else:
        selection = PersonaTable([])
        
    return render_to_response('search.html', 
                              {'form':search, 'table':people, 'selection':selection}, 
                              context_instance=RequestContext(request)) 

@login_required
def reset(request):      
    try:  
        del request.session['selected_people']
    except:
        pass
        
    return HttpResponseRedirect("/contacts/") 

@login_required
#TODO: it doesn't work
def unselect(request, pk):      
    try:  
        del request.session['selected_people']
    except:
        pass
        
    return HttpResponseRedirect("/contacts/") 


@login_required
def export(request):            
    import xlwt
    export_fields = ["Email", "Nombre", "Apellidos", u"Teléfonos", "Cargos", "Secciones"]
    
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
    for contact in request.session['selected_people']:
        try:
            ws.write(i, 0, contact.email_set.all()[0].email)
        except:
            pass
        
        try:
            ws.write(i, 1, contact.name)
        except:
            pass
        
        try:
            ws.write(i, 2, contact.cognoms)
        except:
            pass                
                                
        try:
            list = ""
            for phone in contact.phone_set.all():
                list = list + str(phone.number) + ", "
            ws.write(i, 3, list)
        except:
            pass

        try:
            list = ""
            for position in contact.contactposition_set.all():
                list = list + position.type.name + " (" + position.media.name + "), "
            ws.write(i, 4, list)
        except:
            pass

        try:
            list = ""
            for section in contact.sections.all():
                list = list + section.name + ", "
            ws.write(i, 5, list)
        except:
            pass        
        i += 1
        

    wb.save(response)
    return response

      