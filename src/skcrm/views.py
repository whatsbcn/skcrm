from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Person
from skcrm.tables import PersonaTable
from skcrm.forms import SearchForm

@login_required
def index(request):  
    if request.method == 'POST':
        search = SearchForm(request.POST, request.FILES)
        if search.is_valid():
            # Filter people
            found_people = Person.objects.all()
            if search.cleaned_data['sector']:
                found_people = found_people.filter(sectors__id=search.cleaned_data['sector'])
            if search.cleaned_data['carrec']:
                found_people = found_people.filter(contactrelation__type=search.cleaned_data['carrec'])            
            if search.cleaned_data['ciutat']:
                found_people = found_people.filter(city__id=search.cleaned_data['ciutat'])
            if search.cleaned_data['provincia']:
                found_people = found_people.filter(region__id=search.cleaned_data['provincia'])                
            # Show filtered people
            if 'search' in request.POST:
                people = PersonaTable(found_people)
            # Add filtered people to the selected list
            elif 'add' in request.POST:
                people = PersonaTable([])
                if 'selected_people' in request.session:
                    new_people = set(list(found_people)) - request.session['selected_people']
                    request.session['selected_people'] |= new_people
                else:
                    request.session['selected_people'] = set(list(found_people))              
        else:
            people = PersonaTable([])
            #selection = PersonaTable(Person.objects.all())
            #formset.save()
            # do something.
    else:
        search = SearchForm()
        people = PersonaTable([])
        
    # Mostrem la gent seleccionada    
    if 'selected_people' in request.session:
        selection = PersonaTable(request.session['selected_people'])
    else:
        selection = PersonaTable([])
                
        
        
    return render_to_response('index.html', 
                              {'form':search, 'table':people, 'selection':selection}, 
                              context_instance=RequestContext(request)) 

