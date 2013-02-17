# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Section
from skcrm.tables import SectionTable, MediaContactDataTable
from skcrm.forms import SearchSectionForm, SectionForm
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages

@login_required
def ls(request, id=None):    
        m = Section.objects.all()
        
        # The form has been used
        search = SearchSectionForm()
        if request.method == 'POST':
            search = SearchSectionForm(request.POST, request.FILES)
            if search.is_valid():
                name = search.cleaned_data['name']
                m = m.filter(name__icontains=name)        
                
        table = SectionTable(m, order_by=request.GET.get('sort'))
        table.paginate(page=request.GET.get('page', 1), per_page=25)
            
        return render_to_response('section_list.html', 
                                  {'form':search, 'table':table}, 
                                  context_instance=RequestContext(request)) 
        
@login_required
def edit(request, id=None):   
    if id:
        section = get_object_or_404(Section, pk=id)
    else:
        section = Section()
            
    form = SectionForm(instance=section)
    
    if request.POST:
        form = SectionForm(request.POST, instance=section)
                        
        if form.is_valid():
            sector = form.save()
            
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('section_edit', id=section.id)
        
    return render_to_response('section_edit.html', 
                              {'form':form, 'obj':section}, 
                              context_instance=RequestContext(request))        
    
    
@login_required
def delete(request, id=None):    
    section = get_object_or_404(Section, pk=id)
    section.delete()
    return redirect('section_list')
