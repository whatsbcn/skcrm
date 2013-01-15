# coding: utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skcrm.models import Person, Sector, Company, Expense
from skcrm.tables import PersonaTable, SectorsTable, CompaniesTable, SectionsTable, MediasTable, OtTable, ExpenseTable, ExpenseItemTable, ResumeTable, ExpenseItemDetailTable, ExpenseDetailTable
from skcrm.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime

@login_required(login_url='/accounts/login/')
def index(request):        

    selection = PersonaTable([])
    
        
    return render_to_response('index.html', 
                              {'selection':selection}, 
                              context_instance=RequestContext(request)) 
@login_required
def sections(request, section_id=None):    
    s = Section.objects.all()
    
    # The form has been used
    search = SearchSectionForm()
    if request.method == 'POST':
        search = SearchSectionForm(request.POST, request.FILES)
        if search.is_valid():
            name = search.cleaned_data['name']
            s = s.filter(name__icontains=name)    
                
    # We are selecting a sector
    if section_id:
        s = s.filter(parent__id=section_id)
        sector_name = Section.objects.get(id=section_id).name
    else:
        s = s.filter(parent=None)           
    table = SectionsTable(s, order_by=request.GET.get('sort'))
    table.paginate(page=request.GET.get('page', 1), per_page=25)
        
    return render_to_response('sections.html', 
                              {'form':search, 'table':table}, 
                              context_instance=RequestContext(request)) 
@login_required
def medias(request, media_id=None):    
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
        
    return render_to_response('medias.html', 
                              {'form':search, 'table':table}, 
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
                header_data = [('FECHA EXTRACCIÓN:', str(datetime.date.today())),
                              ('PERIODO:', "%s - %s" % (fecha_inicio, fecha_final))]
                
                selected_expense_items = ExpenseItem.objects.all().filter(expense__date__range=(fecha_inicio, fecha_final)) 
                if ot:
                    selected_expense_items = selected_expense_items.filter(ot=ot)
                    header_data += [('OT:', str(ot)), ('CLIENTE:', str(ot.company))]
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
    

@login_required
def expense(request, action, id=None, item_id=None):
    if action == "list":
        e = Expense.objects.all()
        # The form has been used
        search = SearchExpenseForm()
        if request.method == 'POST':
            search = SearchExpenseForm(request.POST, request.FILES)
            if search.is_valid():
                num = search.cleaned_data['num']
                if num != None:
                    e = e.filter(Q(id=num)|Q(doc_num=num))        
                
        table = ExpenseTable(e, order_by=request.GET.get('sort'))
        table.paginate(page=request.GET.get('page', 1), per_page=25)
            
        return render_to_response('expense_list.html', 
                                  { 'form':search, 'table':table}, 
                                  context_instance=RequestContext(request))
        
    elif action == "edit":
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

    elif action == "add_item":
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

    elif action == "del_item":
        expense = get_object_or_404(Expense, pk=id)
        item = get_object_or_404(ExpenseItem, pk=item_id)
        item.delete()
        
        return redirect('expense_edit', id=id)
            
    elif action == "del" and id:
        expense = get_object_or_404(Expense, pk=id)
        expense.delete()
        return redirect('expense_list')
    
    return redirect('company_list')

@login_required
def company(request, action, id=None, ot_id=None):

    if action == "list":
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
    elif action == "edit":
        if id:
            company = get_object_or_404(Company, pk=id)
        else:
            company = Company()            
        form = CompanyForm(instance=company)
        table = OtTable(company.ot_set.all(), order_by=request.GET.get('sort'))
        rel_form = OtForm()

        if request.POST:
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                company = form.save()
                messages.success(request, "Cambios guardados correctamente.")              
                return redirect('company_edit', id=company.id)
            
        return render_to_response('company_edit.html', 
                                  {'form':form, 'rel_form': rel_form, 'table': table, 'obj':company}, 
                                  context_instance=RequestContext(request))
    elif action == "add_ot":
        company = get_object_or_404(Company, pk=id)
        if request.POST:
            rel_form = OtForm(request.POST, instance=Ot(company=company))
            if rel_form.is_valid():
                rel_form.save()
                messages.success(request, "Cambios guardados correctamente.")              
        
        return redirect('company_edit', id=id)

    elif action == "del_ot":
        company = get_object_or_404(Company, pk=id)
        ot = get_object_or_404(Ot, pk=ot_id)
        ot.delete()
        
        return redirect('company_edit', id=id)
            
    elif action == "del" and id:
        company = get_object_or_404(Company, pk=id)
        company.delete()
        return redirect('company_list')
    
    return redirect('company_list')
        
        

@login_required
def sectors(request, sector_id=None):    
    sector_name = ""
    s = Sector.objects.all()
    
    # The form has been used
    search = SearchSectorForm()
    if request.method == 'POST':
        search = SearchSectorForm(request.POST, request.FILES)
        if search.is_valid():
            name = search.cleaned_data['name']
            s = s.filter(name__icontains=name)        
            
    # We are selecting a sector
    if sector_id:
        s = s.filter(parent__id=sector_id)
        sector_name = Sector.objects.get(id=sector_id).name
    else:
        s = s.filter(parent=None)
    table = SectorsTable(s, order_by=request.GET.get('sort'))
    table.paginate(page=request.GET.get('page', 1), per_page=25)
        
    return render_to_response('sectors.html', 
                              {'form':search, 'sector_name': sector_name, 'table':table}, 
                              context_instance=RequestContext(request)) 

@login_required
def contacts(request):  
    if request.method == 'POST':
        search = SearchContactForm(request.POST, request.FILES)
        if search.is_valid():
            # Filter people
            found_people = Person.objects.select_related().all()
            if search.cleaned_data['name']:
                found_people = found_people.filter(name__icontains=search.cleaned_data['name'])                
            if search.cleaned_data['company']:
                found_people = found_people.filter(Q(positions__name__icontains=search.cleaned_data['company'])|
                                                   Q(positions__in_group__name__icontains=search.cleaned_data['company']))
            if search.cleaned_data['media']:
                found_people = found_people.filter(positions__media__name__icontains=search.cleaned_data['media'])                                    
            if search.cleaned_data['sector']:
                found_people = found_people.filter(Q(contactposition__media__sectors__id=search.cleaned_data['sector'])|
                                                   Q(contactposition__media__sectors__parent__id=search.cleaned_data['sector']))
            if search.cleaned_data['tipo_medio']:
                found_people = found_people.filter(contactposition__media__type__id=search.cleaned_data['tipo_medio'])
            if search.cleaned_data['section']:
                found_people = found_people.filter(Q(sections__id=search.cleaned_data['section'])|
                                                   Q(sections__parent__id=search.cleaned_data['section']))                
            if search.cleaned_data['carrec']:
                found_people = found_people.filter(contactposition__type=search.cleaned_data['carrec'])            
            if search.cleaned_data['ciutat']:
                found_people = found_people.filter(city__id=search.cleaned_data['ciutat'])
            if search.cleaned_data['provincia']:
                found_people = found_people.filter(region__id=search.cleaned_data['provincia'])  
            if search.cleaned_data['withmail']:
                found_people = found_people.filter(email__isnull=False, email__contains='@')

                
            # Add filtered people to the selected list
            if 'add' in request.POST:
                people = PersonaTable([])
                if 'selected_people' in request.session:
                    new_people = set(list(found_people)) - request.session['selected_people']
                    request.session['selected_people'] |= new_people
                else:
                    request.session['selected_people'] = set(list(found_people))
                return HttpResponseRedirect("/contacts/")                   
            # Show filtered people
            else:
                people = PersonaTable(found_people)
                # Paginem la gent seleccionada  
                people.paginate(page=request.GET.get('page', 1), per_page=25)
           
        else:
            people = PersonaTable([])

    else:
        search = SearchContactForm()
        people = PersonaTable([])
        
    # Mostrem la gent seleccionada    
    search = SearchContactForm(request.POST, request.FILES)
    if 'selected_people' in request.session:
        selection = PersonaTable(request.session['selected_people'], order_by=request.GET.get('sort'))
    else:
        selection = PersonaTable([])
        
    return render_to_response('contacts.html', 
                              {'form':search, 'table':people, 'selection':selection}, 
                              context_instance=RequestContext(request)) 

@login_required
def reset(request):      
    try:  
        del request.session['selected_people']
    except:
        pass
        
    return HttpResponseRedirect("/contacts/") 

@login_required
#TODO: it doesn't work
def unselect(request, pk):      
    try:
        for person in request.session['selected_people']:
            if person.id == int(pk):
                aa = "aa"
                #request.session['selected_people'].remove(person)
                #request.session['selected_people'] = request.session['selected_people'].remove(person)
    except:
        pass
        
    return HttpResponseRedirect("/contacts/") 


@login_required
def export(request):            
    import xlwt
    export_fields = ["Email", "Nombre", "Apellidos", u"Teléfonos", u"Dirección postal", "Cargos", "Secciones"]
    
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=export.xls'
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Contactos')
    
    i = 0
    j = 0
    for field in export_fields:
        ws.write(i, j, field)
        j += 1
        
    i = 1   
    for contact in request.session['selected_people']:
        try:
            ws.write(i, 0, contact.email_set.all()[0].email)
        except:
            pass
        
        try:
            ws.write(i, 1, contact.name)
        except:
            pass
        
        try:
            ws.write(i, 2, contact.cognoms)
        except:
            pass                
                                
        try:
            list = ""
            for phone in contact.phone_set.all():
                list = list + str(phone.number) + ", "
            ws.write(i, 3, list)
        except:
            pass
        
        try:
            list = contact.address + ", (" + contact.postal_code + " " + contact.city.name + ")"  
            ws.write(i, 4, list)
        except:
            pass
        
        try:
            list = ""
            for position in contact.contactposition_set.all():
                list = list + position.type.name + " (" + position.media.name + "), "
            ws.write(i, 5, list)
        except:
            pass

        try:
            list = ""
            for section in contact.sections.all():
                list = list + section.name + ", "
            ws.write(i, 6, list)
        except:
            pass        
        i += 1
        

    wb.save(response)
    return response

      