# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Person, Sector, Company, Expense, Section, Media, ExpenseItem, Ot, ContactData
from skcrm.models import IVA_TYPE
from skcrm.tables import ExpenseItemDetailTable, ExpenseDetailTable
from skcrm.forms import  GastosPorOtrForm, GastosPorProveedorForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime


@login_required(login_url='/accounts/login/')
def index(request):        
    return render_to_response('index.html', 
                              context_instance=RequestContext(request)) 

@login_required
def report(request, report, id=None):
    if report == "gastos_por_ot":
        title = "Gastos por OT - Orbyce Comunicacion S.L."
        header_data = []
        detail_table = []
        resume_data = []
        total = 0
        form = GastosPorOtrForm()
        if request.method == 'POST':
            form = GastosPorOtrForm(request.POST, request.FILES)
            if form.is_valid():
                fecha_inicio = form.cleaned_data['fecha_inicio']
                fecha_final = form.cleaned_data['fecha_final']
                #get_object_or_404(Ot, pk=)
                ot = form.cleaned_data['ot']
                content_type = form.cleaned_data['content_type']
                header_data = [('FECHA EXTRACCIÓN:', str(datetime.date.today())),
                              ('PERIODO:', "%s - %s" % (fecha_inicio, fecha_final))]
                
                selected_expense_items = ExpenseItem.objects.all().filter(expense__date__range=(fecha_inicio, fecha_final)) 
                if ot:
                    selected_expense_items = selected_expense_items.filter(ot=ot)
                    header_data += [('OT:', str(ot)), ('CLIENTE:', str(ot.company))]
                if content_type:
                    selected_expense_items = selected_expense_items.filter(concept_type=content_type)
                    header_data += [('Concepto:', str(content_type))]                    
                detail_table = ExpenseItemDetailTable(selected_expense_items, order_by=request.GET.get('sort'))
                
                for iva_item, iva_desc in IVA_TYPE:
                    resume_data.append({'iva': iva_item, 'base': 0})
                    
                for item in selected_expense_items:
                    for table_resume_entry in resume_data:
                        if table_resume_entry['iva'] == item.iva:
                            table_resume_entry['base'] += item.base
                    total += item.base + (item.iva * item.base)/100                         
                                
        else: 
            form = GastosPorOtrForm()
            
        return render_to_response('report.html', 
                                  {'title':title, 'header_data': header_data, 'detail_table': detail_table, 'resume_data': resume_data, 
                                   'form': form, 'total': "%.2f" % total}, 
                                  context_instance=RequestContext(request))
   
    elif report == "gastos_por_proveedor":
        title = "Gastos por Proveedor - Orbyce Comunicacion S.L."
        header_data = []
        detail_table = []
        resume_data = []
        total = 0
        form = GastosPorProveedorForm()
        if request.method == 'POST':
            form = GastosPorProveedorForm(request.POST, request.FILES)
            if form.is_valid():
                fecha_inicio = form.cleaned_data['fecha_inicio']
                fecha_final = form.cleaned_data['fecha_final']
                #get_object_or_404(Ot, pk=)
                proveedor = form.cleaned_data['proveedor']
                estado = form.cleaned_data['estado']
                header_data = [('FECHA EXTRACCIÓN:', str(datetime.date.today())),
                              ('PERIODO:', "%s - %s" % (fecha_inicio, fecha_final))]
                                
                
                selected_expense = Expense.objects.all().filter(date__range=(fecha_inicio, fecha_final))
                if proveedor:
                    selected_expense = selected_expense.filter(provider=proveedor)
                    header_data += [('PROVEEDOR:', str(proveedor))]
                if estado:
                    selected_expense = selected_expense.filter(state=estado)
                    header_data += [('ESTADO:', str(estado))]
                detail_table = ExpenseDetailTable(selected_expense, order_by=request.GET.get('sort'))
                
#                for iva_item, iva_desc in IVA_TYPE:
#                    resume_data.append({'iva': iva_item, 'base': 0})
                    
                for expense in selected_expense:
#                    for table_resume_entry in resume_data:
#                        if table_resume_entry['iva'] == item.iva:
#                            table_resume_entry['base'] += item.base
                    total += expense.total()                         
                                
        else: 
            form = GastosPorProveedorForm()
            
        return render_to_response('report.html', 
                                  {'title':title, 'header_data': header_data, 'detail_table': detail_table, 'resume_data': resume_data, 
                                   'form': form, 'total': "%.2f" % total}, 
                                  context_instance=RequestContext(request))
    
     


      