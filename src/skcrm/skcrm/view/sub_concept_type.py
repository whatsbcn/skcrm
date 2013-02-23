# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import ExpenseConceptSubType
from skcrm.tables import ExpenseConceptSubTypeTable
from skcrm.forms import SearchExpenseConceptSubTypeForm, ExpenseConceptSubTypeForm
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages

@login_required
def ls(request, id=None):    
        m = ExpenseConceptSubType.objects.all()
        
        # The form has been used
        search = SearchExpenseConceptSubTypeForm()
        if request.method == 'POST':
            search = SearchExpenseConceptSubTypeForm(request.POST, request.FILES)
            if search.is_valid():
                name = search.cleaned_data['name']
                m = m.filter(name__icontains=name)        
                
        table = ExpenseConceptSubTypeTable(m, order_by=request.GET.get('sort'))
        table.paginate(page=request.GET.get('page', 1), per_page=25)
            
        return render_to_response('sub_concept_type_list.html', 
                                  {'form':search, 'table':table}, 
                                  context_instance=RequestContext(request)) 
        
@login_required
def edit(request, id=None):   
    if id:
        concept_type = get_object_or_404(ExpenseConceptSubType, pk=id)
    else:
        concept_type = ExpenseConceptSubType()
            
    form = ExpenseConceptSubTypeForm(instance=concept_type)
    
    if request.POST:
        form = ExpenseConceptSubTypeForm(request.POST, instance=concept_type)
                        
        if form.is_valid():
            sector = form.save()
            
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('sub_concept_type_edit', id=concept_type.id)
        
    return render_to_response('sub_concept_type_edit.html', 
                              {'form':form, 'obj':concept_type}, 
                              context_instance=RequestContext(request))        
    
    
@login_required
def delete(request, id=None):    
    concept_type = get_object_or_404(ExpenseConceptSubType, pk=id)
    concept_type.delete()
    return redirect('sub_concept_type_list')
