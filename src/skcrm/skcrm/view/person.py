# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Person, ContactData
from skcrm.tables import PersonTable, PersonContactDataTable
from skcrm.forms import PersonForm, SearchPersonForm, PersonContactDataForm 
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
from django.contrib.auth.models import Group

@login_required
def ls(request, id=None):    
        m = Person.objects.all()
        if request.user.groups.filter(name='Sociedad').count() == 0:
            m = m.exclude(type=2)
                    
        search = SearchPersonForm()
        if request.method == 'POST':
            search = SearchPersonForm(request.POST, request.FILES)
            if search.is_valid():
                name = search.cleaned_data['name']
                m = m.filter(Q(name__icontains=name)|Q(surname__icontains=name)|Q(cognoms__icontains=name))        
                
        table = PersonTable(m, order_by=request.GET.get('sort'))
        table.paginate(page=request.GET.get('page', 1), per_page=25)
        

        return render_to_response('person_list.html', 
                                  {'form':search, 'table':table}, 
                                  context_instance=RequestContext(request)) 
        
@login_required
def edit(request, id=None):   
    if id:
        person = get_object_or_404(Person, pk=id)
    else:
        person = Person()
            
    form = PersonForm(instance=person)
    
    table = PersonContactDataTable(person.contactdata_set.all().filter(type_id=1), order_by=request.GET.get('sort'))

    if request.POST:
        form = PersonForm(request.POST, instance=person)
                
        if form.is_valid():
            person = form.save()
            
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('person_edit', id=person.id)
        
    return render_to_response('person_edit.html', 
                              {'form':form, 'table':table, 'obj':person}, 
                              context_instance=RequestContext(request))        
        
@login_required
def delete(request, id=None):             
    person = get_object_or_404(Person, pk=id)
    for cd in person.contactdata_set.all().filter(type_id=1):
        cd.delete()
    person.delete()
    return redirect('person_list')

@login_required
def edit_cd(request, id=None, cd_id=None):   
    person = get_object_or_404(Person, pk=id)
    
    if cd_id:
        cd = get_object_or_404(ContactData, pk=cd_id)
    else:
        cd = ContactData(person=person, type_id=1)
        
    form = PersonContactDataForm(instance=cd)
    
    if request.POST:
        form = PersonContactDataForm(request.POST, instance=cd)
        if form.is_valid():
            form.save()
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('person_edit', id=id)
        else:
            messages.error(request, "No se han podido guardar los cambios.")           
    
    return render_to_response('person_edit_cd.html', 
                              {'form':form, 'obj':person}, 
                              context_instance=RequestContext(request))        
     

@login_required
def del_cd(request, id=None, cd_id=None):   
    contact_data = get_object_or_404(ContactData, pk=cd_id)
    contact_data.delete()
    return redirect('person_edit', id=id)
