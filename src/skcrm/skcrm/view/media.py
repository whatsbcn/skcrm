# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Media, ContactData
from skcrm.tables import MediasTable, MediaContactDataTable
from skcrm.forms import SearchMediaForm, MediaContactDataForm, MediaForm 
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages

@login_required
def ls(request, id=None):    
        m = Media.objects.all()
        
        # The form has been used
        search = SearchMediaForm()
        if request.method == 'POST':
            search = SearchMediaForm(request.POST, request.FILES)
            if search.is_valid():
                name = search.cleaned_data['name']
                m = m.filter(name__icontains=name)        
                
        table = MediasTable(m, order_by=request.GET.get('sort'))
        table.paginate(page=request.GET.get('page', 1), per_page=25)
            
        return render_to_response('media_list.html', 
                                  {'form':search, 'table':table}, 
                                  context_instance=RequestContext(request)) 
        
@login_required
def edit(request, id=None):   
    if id:
        media = get_object_or_404(Media, pk=id)
    else:
        media = Media()
            
    form = MediaForm(instance=media)
    
    table = MediaContactDataTable(media.contactdata_set.all().filter(type_id=3), order_by=request.GET.get('sort'))
    
    if request.POST:
        form = MediaForm(request.POST, instance=media)
                        
        if form.is_valid():
            media = form.save()
            
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('media_edit', id=media.id)
        
    return render_to_response('media_edit.html', 
                              {'form':form, 'table': table,  'obj':media}, 
                              context_instance=RequestContext(request))        
    
    
@login_required
def delete(request, id=None):    
    media = get_object_or_404(Media, pk=id)
    for cd in media.contactdata_set.all().filter(type_id=3):
        cd.delete()
    media.delete()
    return redirect('media_list')


@login_required
def edit_cd(request, id=None, cd_id=None):   
    media = get_object_or_404(Media, pk=id)
    
    if cd_id:
        cd = get_object_or_404(ContactData, pk=cd_id)
    else:
        cd = ContactData(media=media, type_id=3)
        
    form = MediaContactDataForm(instance=cd)
    
    if request.POST:
        form = MediaContactDataForm(request.POST, instance=cd)
        if form.is_valid():
            form.save()
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('media_edit', id=id)
        else:
            messages.error(request, "No se han podido guardar los cambios.")           
    
    return render_to_response('media_edit_cd.html', 
                              {'form':form, 'obj':media}, 
                              context_instance=RequestContext(request))        

     
@login_required
def del_cd(request, id=None, cd_id=None):   
    contact_data = get_object_or_404(ContactData, pk=cd_id)
    contact_data.delete()
    return redirect('media_edit', id=id)           