from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Person
from skcrm.tables import PersonaTable
from skcrm.forms import *
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def index(request):        
    # Mostrem la gent seleccionada    
    if 'selected_people' in request.session:
        selection = PersonaTable(request.session['selected_people'], order_by=request.GET.get('sort'))
    else:
        selection = PersonaTable([])
    
    # Paginem la gent seleccionada  
    selection.paginate(page=request.GET.get('page', 1), per_page=25)
        
    return render_to_response('index.html', 
                              {'form':search, 'selection':selection}, 
                              context_instance=RequestContext(request)) 

@login_required
def search(request):  
    if request.method == 'POST':
        search = SearchForm(request.POST, request.FILES)
        if search.is_valid():
            # Filter people
            found_people = Person.objects.select_related().all()
            if search.cleaned_data['sector']:
                found_people = found_people.filter(sectors__id=search.cleaned_data['sector'])
            if search.cleaned_data['carrec']:
                found_people = found_people.filter(contactrelation__type=search.cleaned_data['carrec'])            
            if search.cleaned_data['ciutat']:
                found_people = found_people.filter(city__id=search.cleaned_data['ciutat'])
            if search.cleaned_data['provincia']:
                found_people = found_people.filter(region__id=search.cleaned_data['provincia'])  
            if search.cleaned_data['withmail']:
                found_people = found_people.filter(email__isnull=False, email__contains='@')
            # Show filtered people
            if 'search' in request.POST:
                people = PersonaTable(found_people)
                # Paginem la gent seleccionada  
                people.paginate(page=request.GET.get('page', 1), per_page=25)
                
            # Add filtered people to the selected list
            elif 'add' in request.POST:
                people = PersonaTable([])
                if 'selected_people' in request.session:
                    new_people = set(list(found_people)) - request.session['selected_people']
                    request.session['selected_people'] |= new_people
                else:
                    request.session['selected_people'] = set(list(found_people))
                return HttpResponseRedirect("/")              
        else:
            people = PersonaTable([])

    else:
        search = SearchForm()
        people = PersonaTable([])

        
    return render_to_response('search.html', 
                              {'form':search, 'table':people}, 
                              context_instance=RequestContext(request)) 

@login_required
def reset(request):        
    del request.session['selected_people']
        
    return HttpResponseRedirect("/") 

@login_required
def export(request):            
    import xlwt
    export_fields = ['email', 'name', 'cognom1', 'cognom2']
    
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=export.xls'
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Contactos')
    
    j = 0
    for contact in request.session['selected_people']:
        i = 0
        #for field in contact._meta.get_all_field_names():
        for field in export_fields:
            if j == 0:
                ws.write(0, i, field)
            try:
                ws.write(j+1, i, getattr(contact, field))
            except:
                pass
            i += 1
        j += 1

    wb.save(response)
    return response

@login_required
def contacts(request):
    if request.method == 'POST':
        search = SearchContactForm(request.POST, request.FILES)
        if search.is_valid():
            # Filter people
            found_people = Person.objects.select_related().all()
            if search.cleaned_data['company']:
                found_people = found_people.filter(positions__name__icontains=search.cleaned_data['company'])
            if search.cleaned_data['carrec']:
                found_people = found_people.filter(contactposition__type=search.cleaned_data['carrec'])            
            if search.cleaned_data['name']:
                found_people = found_people.filter(name__icontains=search.cleaned_data['name'])

            # Show filtered people
            people = PersonaTable(found_people)
            # Paginem la gent seleccionada  
            people.paginate(page=request.GET.get('page', 1), per_page=25)
        else:
            search = SearchContactForm()
            people = PersonaTable([])

    else:
        search = SearchContactForm()
        people = PersonaTable([])

            
    return render_to_response('contacts.html', 
                              {'form':search, 'contacts':people}, 
                              context_instance=RequestContext(request)) 
      