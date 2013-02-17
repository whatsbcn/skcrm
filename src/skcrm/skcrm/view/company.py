# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Company, Ot, ContactData
from skcrm.tables import CompaniesTable, OtTable, CompanyContactDataTable
from skcrm.forms import SearchCompanyForm, CompanyForm, OtForm, CompanyContactDataForm 
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.contrib import messages


@login_required
def ls(request, id=None, ot_id=None):
    c = Company.objects.all()
    # The form has been used
    search = SearchCompanyForm()
    if request.method == 'POST':
        search = SearchCompanyForm(request.POST, request.FILES)
        if search.is_valid():
            name = search.cleaned_data['name']
            c = c.filter(Q(name__icontains=name)|Q(comercial_name__icontains=name))        
            
    table = CompaniesTable(c, order_by=request.GET.get('sort'))
    table.paginate(page=request.GET.get('page', 1), per_page=25)
        
    return render_to_response('company_list.html', 
                              {'form':search, 'table':table}, 
                              context_instance=RequestContext(request))

@login_required
def edit(request, id=None, ot_id=None):
    if id:
        company = get_object_or_404(Company, pk=id)
    else:
        company = Company()
                    
    form = CompanyForm(instance=company)
    
    table = OtTable(company.ot_set.all(), order_by=request.GET.get('sort'))
    table2 = CompanyContactDataTable(company.contactdata_set.all().filter(type_id=2), order_by=request.GET.get('sort'))
    rel_form = OtForm()

    if request.POST:
        form = CompanyForm(request.POST, instance=company)

        if form.is_valid():
            company = form.save()

            
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('company_edit', id=company.id)
        
    return render_to_response('company_edit.html', 
                              {'form':form, 'rel_form': rel_form, 'table': table, 'table2': table2, 'obj':company}, 
                              context_instance=RequestContext(request))

@login_required
def add_ot(request, id=None, ot_id=None):
    company = get_object_or_404(Company, pk=id)
    if request.POST:
        rel_form = OtForm(request.POST, instance=Ot(company=company))
        if rel_form.is_valid():
            rel_form.save()
            messages.success(request, "Cambios guardados correctamente.")
        else:
            messages.error(request, "No se han podido guardar los cambios.")           
    
    return redirect('company_edit', id=id)

@login_required
def del_ot(request, id=None, ot_id=None):
    company = get_object_or_404(Company, pk=id)
    ot = get_object_or_404(Ot, pk=ot_id)
    ot.delete()
    
    return redirect('company_edit', id=id)

@login_required
def delete(request, id=None, ot_id=None):            
    company = get_object_or_404(Company, pk=id)
    for cd in company.contactdata_set.all().filter(type_id=2):
        cd.delete()
    for ot in company.ot_set.all():
        ot.delete()
    company.delete()
    return redirect('company_list')


@login_required
def edit_cd(request, id=None, cd_id=None):   
    company = get_object_or_404(Company, pk=id)
    
    if cd_id:
        cd = get_object_or_404(ContactData, pk=cd_id)
    else:
        cd = ContactData(company=company, type_id=2)
        
    form = CompanyContactDataForm(instance=cd)
    
    if request.POST:
        form = CompanyContactDataForm(request.POST, instance=cd)
        if form.is_valid():
            form.save()
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('company_edit', id=id)
        else:
            messages.error(request, "No se han podido guardar los cambios.")           
    
    return render_to_response('company_edit_cd.html', 
                              {'form':form, 'obj':company}, 
                              context_instance=RequestContext(request))        

     
@login_required
def del_cd(request, id=None, cd_id=None):   
    contact_data = get_object_or_404(ContactData, pk=cd_id)
    contact_data.delete()
    return redirect('company_edit', id=id)  