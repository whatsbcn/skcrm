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
def list(request, id=None):    
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
def delete(request, id=None):    
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