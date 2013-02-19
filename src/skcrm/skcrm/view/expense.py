# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Expense, ExpenseItem
from skcrm.tables import ExpenseTable, ExpenseItemTable, ResumeTable
from skcrm.forms import SearchExpenseForm, ExpenseForm, ExpenseItemForm 
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages

@login_required
def ls(request, id=None, item_id=None):
    e = Expense.objects.all()
    # The form has been used
    search = SearchExpenseForm()
    if request.method == 'POST':
        search = SearchExpenseForm(request.POST, request.FILES)
        if search.is_valid():
            filter = search.cleaned_data['filter']
            if filter != None:
                try:
                    num = int(filter)
                    e = e.filter(Q(id=num)|Q(doc_num=num)|Q(provider__name__icontains=filter)|Q(provider__comercial_name__icontains=filter))  
                except:
                    e = e.filter(Q(provider__name__icontains=filter)|Q(provider__comercial_name__icontains=filter))
                    
            
    table = ExpenseTable(e, order_by=request.GET.get('sort'))
    table.paginate(page=request.GET.get('page', 1), per_page=25)
        
    return render_to_response('expense_list.html', 
                              { 'form':search, 'table':table}, 
                              context_instance=RequestContext(request))

@login_required
def edit(request, id=None, item_id=None):        
    if id:
        expense = get_object_or_404(Expense, pk=id)
    else:
        expense = Expense()            
    form = ExpenseForm(instance=expense)
    table = ExpenseItemTable(expense.expenseitem_set.all(), order_by=request.GET.get('sort'))
    rel_form = ExpenseItemForm()
    
    table_resume_data, total = expense.resume_data()
    table_resume = ResumeTable(table_resume_data)       
         
    if request.POST:
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save()
            messages.success(request, "Cambios guardados correctamente.")              
            return redirect('expense_edit', id=expense.id)
    
    return render_to_response('expense_edit.html', 
                  {'form':form, 'rel_form':rel_form, 'table': table, 'table_resume':table_resume, 'total': total, 'obj':expense}, 
                  context_instance=RequestContext(request))

@login_required
def add_item(request, id=None, item_id=None):
    expense = get_object_or_404(Expense, pk=id)
    if request.POST:
        rel_form = ExpenseItemForm(request.POST, instance=ExpenseItem(expense=expense))
        if rel_form.is_valid():
            rel_form.save()
            messages.success(request, "Cambios guardados correctamente.")  
            return redirect('expense_edit', id=id)
        else:
            form = ExpenseForm(instance=expense)
            table = ExpenseItemTable(expense.expenseitem_set.all(), order_by=request.GET.get('sort'))
            table_resume_data, total = expense.resume_data()
            table_resume = ResumeTable(table_resume_data) 
            return render_to_response('expense_edit.html', 
                          {'form':form, 'rel_form':rel_form, 'table': table, 'table_resume':table_resume, 'total': total, 'obj':expense}, 
                          context_instance=RequestContext(request))
    return redirect('expense_edit', id=id)

@login_required
def del_item(request, id=None, item_id=None):
    expense = get_object_or_404(Expense, pk=id)
    item = get_object_or_404(ExpenseItem, pk=item_id)
    item.delete()
    
    return redirect('expense_edit', id=id)
            
@login_required
def delete(request, id=None, item_id=None):
    expense = get_object_or_404(Expense, pk=id)
    expense.delete()
    return redirect('expense_list')



   