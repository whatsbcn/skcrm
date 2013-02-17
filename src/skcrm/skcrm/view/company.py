# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Person, Sector, Company, Expense, Section, Media, ExpenseItem, Ot, ContactData
from skcrm.models import IVA_TYPE
from skcrm.tables import PersonaTable, SectorsTable, CompaniesTable, SectionsTable, MediasTable, OtTable, ExpenseTable, ExpenseItemTable, ResumeTable, ExpenseItemDetailTable, ExpenseDetailTable
from skcrm.forms import SearchSectionForm, SearchMediaForm, GastosPorOtrForm, GastosPorProveedorForm, SearchExpenseForm, ExpenseForm, ExpenseItemForm, SearchCompanyForm, CompanyForm, OtForm, SearchSectorForm, SearchContactForm, PersonForm, CompanyContactDataForm 
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime

@login_required
def list(request, id=None, ot_id=None):
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
                    
    i = 0    
    form = CompanyForm(prefix=str(i), instance=company)
    
    form_ext = []
    for contactdata in company.contactdata_set.all():
        i+=1
        form_ext += [CompanyContactDataForm(prefix=str(i), instance=contactdata)]
    i+=1
    form_ext += [CompanyContactDataForm(prefix=str(++i))]
    
    table = OtTable(company.ot_set.all(), order_by=request.GET.get('sort'))
    rel_form = OtForm()

    if request.POST:
        i = 0
        form = CompanyForm(request.POST, prefix=str(i), instance=company)
        form_ext = []
        for contactdata in company.contactdata_set.all():
            i+=1
            form_ext += [CompanyContactDataForm(request.POST, prefix=str(i), instance=contactdata)]
        i+=1
        form_ext += [CompanyContactDataForm(request.POST, prefix=str(i), instance=ContactData(company=company, type_id=2))]
                        
        if form.is_valid():
            company = form.save()
            
            for f in form_ext:
                if f.is_valid():
                    f.save()
            
            messages.success(request, "Cambios guardados correctamente.")
            return redirect('company_edit', id=company.id)
        
    return render_to_response('company_edit.html', 
                              {'form':form, 'form_ext': form_ext, 'rel_form': rel_form, 'table': table, 'obj':company}, 
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
    for cd in company.contactdata_set.all():
        cd.delete()
    for ot in company.ot_set.all():
        ot.delete()
    company.delete()
    return redirect('company_list')
