# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Sector
from skcrm.tables import SectorTable, MediaContactDataTable
from skcrm.forms import SearchSectorForm, MediaContactDataForm, MediaForm, SectorForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages

@login_required
def ls(request, id=None):    
        m = Sector.objects.all()
        
        # The form has been used
        search = SearchSectorForm()
        if request.method == 'POST':
            search = SearchSectorForm(request.POST, request.FILES)
            if search.is_valid():
                name = search.cleaned_data['name']
                m = m.filter(name__icontains=name)        
                
        table = SectorTable(m, order_by=request.GET.get('sort'))
        table.paginate(page=request.GET.get('page', 1), per_page=25)
            
        return render_to_response('sector_list.html', 
                                  {'form':search, 'table':table}, 
                                  context_instance=RequestContext(request)) 
        
@login_required
def edit(request, id=None):   
    if id:
        sector = get_object_or_404(Sector, pk=id)
    else:
        sector = Sector()
            
    form = SectorForm(instance=sector)
    
    if request.POST:
        form = SectorForm(request.POST, instance=sector)
                        
        if form.is_valid():
            sector = form.save()
            
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('sector_edit', id=sector.id)
        
    return render_to_response('sector_edit.html', 
                              {'form':form, 'obj':sector}, 
                              context_instance=RequestContext(request))        
    
    
@login_required
def delete(request, id=None):    
    sector = get_object_or_404(Sector, pk=id)
    sector.delete()
    return redirect('sector_list')
