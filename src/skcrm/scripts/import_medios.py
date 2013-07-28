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

fd = open("/Users/whats/Documents/empreses/orbyce/aplicacio/20130702_BDD_ORBYCE_srAB_Dani_medios.csv", 'rb')
buff = csv.reader(fd, delimiter=',', quotechar='|')

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
for nombre, caca_web, tipo_medio, caca_periodicidad, caca_ambito, caca_sec1, caca_sec2, caca_sec3, caca_sec4, caca_sec5, empresa, caca_descri, direccion, cp, provincia, ciudad, telf_fijo, telf_mobil  in buff:
	secciones = []
	
	if i < 3:
		i += 1
		continue
# 	print "Seccions"
# 	for s in (sec1, sec2, sec3, sec4, sec5, sec6, sec7):
# 		if s != "":
# 			if len(Section.objects.filter(name=s)) == 0:
# 				if s.strip() not in falten_sections:
# 					falten_sections.append(s.strip())
# 					print s.strip()
	
	nombre = unicode(nombre).strip().title()
	tipo_medio = unicode(tipo_medio).strip().title()	
	empresa = unicode(empresa).strip()
	# direccion
	# cp
	# telf fijo
	# telf mobil
	
	
 	s = tipo_medio
	if s != "":
		s = unicode(s).strip().title().replace('/A', '/a')
		select = MediaType.objects.filter(name__icontains=s)
		if len(select) == 0:
			if s not in falten_carrecs:
				falten_carrecs.append(s)
				p = MediaType(name=s)
				p.save()
				media_type = p
				print p
		else:
			media_type = select[0]
	else:
		media_type = None

  	
 	s = provincia
	if s != "":
		s = unicode(s).strip().title().replace('/A', '/a')
		select = Region.objects.filter(name__icontains=s)
		if len(select) == 0:
			if s not in falten_provincies:
				falten_provincies.append(s)
				c = Region(name=s)
				c.save()
				region = c
				print c
		else:
			region = select[0]
	else:
		region = None


 	j = 0
 	s = ciudad
	if s != "":
		s = unicode(s).strip().title().replace('/A', '/a')
		select = City.objects.filter(name__icontains=s)
		if len(select) == 0:
			if s not in falten_ciutats:
				falten_ciutats.append(s)
				c = City(name=s, region=region)
				try:
					c.save()
				except Exception, e:
					city = None
					print e
				city = c
				print c
		else:
			city = select[0]
		j += 1
	else:
		city = None


 	s = empresa
 	if s != "":
	 	s = unicode(s).strip().title().replace('/A', '/a')
		select = Company.objects.filter(name__icontains=s)
		if len(select) == 0:
				c = Company(name=s)
				c.save()
				company = c
				print c
		else:
			company = select[0]
	else:
		company = None

 	medios = []
 	s = nombre
	s = unicode(s).strip().title().replace('/A', '/a')
	select = Media.objects.filter(name__icontains=s)
	if len(select) == 0:
		if s not in medio:
			medio.append(s)
			m = Media(name=s)
			m.save()
			medios.append(m)
			print m
	else:
		m = select[0]
		
	i += 1

	if media_type:
		m.type = media_type
		m.save()
	if company:
		m.company = company
		m.save()
	if direccion != "" or cp != "" or region or city:
		c = ContactData(media=m, type_id=3, telf_static=telf_fijo, telf_movile=telf_mobil, address=unicode(direccion), postal_code=cp, region=region, city=city)
		try:
			c.save()
		except Exception, e:
			print e
	print m
	
