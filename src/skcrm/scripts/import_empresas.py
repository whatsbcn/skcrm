import csv
import sys
import os

# paths = ['/Users/whats/Documents/code/skcrm/src/skcrm/skcrm', '/Users/whats/Documents/code/skcrm/src/skcrm/']
# 
# for path in paths:
# 	if path not in sys.path:
# 		sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'skcrm.settings'

from skcrm.models import Person, Company, Media, Section, PositionTypes, City, ContactTreatment, Region, ContactData, MediaType

fd = open("/Users/whats/Documents/empreses/orbyce/aplicacio/20130702_BDD_ORBYCE_srAB_Dani_grupo.csv", 'rb')
buff = csv.reader(fd, delimiter='\t', quotechar='|')

# TODO: Falten les observacions

i = 0
falten_sections = []
falten_carrecs = []
falten_ciutats = []
falten_provincies = []
provincies = []
medio = []
empresa = []
tratamientos = []
for nombre_fiscal, nombre_comercial, nif, web, es_grupo, grupo_padre in buff:
	secciones = []
		
	if i < 3:
		i += 1
		continue

	nombre_fiscal = unicode(nombre_fiscal).strip().title()
	nombre_comercial = unicode(nombre_comercial).strip().title()	
	grupo_padre = unicode(grupo_padre).strip()
	
	grupo = None
	if es_grupo == "No":
	 	s = grupo_padre
	 	if s != "":
		 	s = unicode(s).strip().title().replace('/A', '/a')
			select = Company.objects.filter(name__icontains=s)
			if len(select) == 0:
					c = Company(name=s)
					c.save()
					grupo = c
					print c
			else:
				grupo = select[0]
		else:
			grupo = None


	select = Company.objects.filter(name__icontains=nombre_fiscal)
	if len(select) == 0:
			c = Company(name=s)
			c.save()
			company = c
			print c
	else:
		company = select[0]
	
	if nombre_comercial != "":
		company.comercial_name = nombre_comercial
		
	if grupo:
		company.in_group = grupo
		
	print es_grupo
	if es_grupo == "Si":
		company.is_group = True
		
	if nif:
		company.NIF_CIF = nif
		
	if web:
		company.website = web
	
	company.save()
	
	print company
