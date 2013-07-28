import csv
import sys
import os

# paths = ['/Users/whats/Documents/code/skcrm/src/skcrm/skcrm', '/Users/whats/Documents/code/skcrm/src/skcrm/']
# 
# for path in paths:
# 	if path not in sys.path:
# 		sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'skcrm.settings'

from skcrm.models import Person, Company, Media, Section, PositionTypes, City, ContactTreatment, Region, ContactData

fd = open("20130702_BDD_ORBYCE_srAB_Dani.csv", 'rb')
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
for sec1, sec2, sec3, sec4, sec5, sec6, sec7, tratamiento, nombre, apellidos, nacimiento, observaciones, advertencias, \
	desc1, empresa1, medio1, cargo1, dir1, cp1, provincia1, ciudad1, merda, fijo1, mobil1, fax1, mail1_1, mail1_2, mailing1, \
	desc2, empresa2, medio2, cargo2, dir2, cp2, provincia2, ciudad2,  fijo2, mobil2, fax2, mail2_1, mail2_2, mailing2, \
	desc3, empresa3, medio3, cargo3, dir3, cp3, provincia3, ciudad3,  fijo3, mobil3, fax3, mail3_1, mail3_2, mailing3 in buff:
	secciones = []
	
	if i == 0:
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
	apellidos = unicode(apellidos).strip().title()	
	tratamiento = unicode(tratamiento).strip()
	select = ContactTreatment.objects.filter(name__icontains=tratamiento) 
	if len(select) == 0:
		if tratamiento != "":
			
			if tratamiento not in tratamientos:
				tratamientos.append(tratamiento)
				c = ContactTreatment(name=tratamiento)
				c.save()
				t = c
				print tratamiento
	else:
		t = select[0]
 	
 	positions = []
 	for s in (cargo1, cargo2, cargo3):
 		if s != "":
 			s = unicode(s).strip().title().replace('/A', '/a')
 			select = PositionTypes.objects.filter(name__icontains=s)
 			if len(select) == 0:
 				if s not in falten_carrecs:
 					falten_carrecs.append(s)
 					p = PositionTypes(name=s)
 					p.save()
 					positions.append(p)
 					print p
 			else:
 				positions.append(select[0])
 
  	 	else:
  	 		positions.append(None)
  	regiones = []
 	for s in (provincia1, provincia2, provincia3):
 		if s != "":
 			s = unicode(s).strip().title().replace('/A', '/a')
 			select = Region.objects.filter(name__icontains=s)
 			if len(select) == 0:
 				if s not in falten_provincies:
 					falten_provincies.append(s)
 					c = Region(name=s)
 					c.save()
 					regiones.append(c)
 					print c
 			else:
 				regiones.append(select[0])
 		else:
 			regiones.append(None)
 
 
 	ciudades = []
 	j = 0
 	for s in (ciudad1, ciudad2, ciudad3):
 		if s != "":
 			s = unicode(s).strip().title().replace('/A', '/a')
 			select = City.objects.filter(name__icontains=s)
 			if len(select) == 0:
 				if s not in falten_ciutats:
 					try:
 						if not regiones[j]:
 							break;
 					except:
 						break
 					falten_ciutats.append(s)
 					c = City(name=s, region=regiones[j])
 					c.save()
 					ciudades.append(c)
 					print c
 			else:
 				ciudades.append(select[0])
 			j += 1
 		else:
 			ciudades.append(None)
 
 	empresas = []
 	for s in (empresa1, empresa2, empresa3):
 		if s != "":
			s = unicode(s).strip().title().replace('/A', '/a')
			select = Company.objects.filter(name__icontains=s)
 			if len(select) == 0:
 				if s not in empresa:
 					empresa.append(s)
 					c = Company(name=s)
 					c.save()
 					empresas.append(c)
 					print c
  			else:
  				empresas.append(select[0])
   		else:
   			empresas.append(None)
 
 	medios = []
 	for s in (medio1, medio2, medio3):
 		if s != "":
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
 				medios.append(select[0])
 		else:
 			medios.append(None)

 	secciones = []
 	for s in (sec1, sec2, sec3, sec4, sec5, sec6, sec7):
 		if s != "":
 			s = unicode(s).strip().title().replace('/A', '/a')
 			select = Section.objects.filter(name__icontains=s)
 			if len(select) == 0:
 				if s not in falten_sections:
 					falten_sections.append(s)
 					m = Section(name=s)
 					m.save()
 					secciones.append(m)
 					print m
 			else:
 				secciones.append(select[0])
 		else:
 			secciones.append(None)
	i += 1


	select = Person.objects.filter(name__icontains=nombre, cognoms__icontains=apellidos) 
	if len(select) == 0:
		if tratamiento != "":
			p = Person(name=nombre, cognoms=apellidos, info_text=observaciones, warning_text=advertencias, treatment=t)
			p.save()
			print p, nacimiento
				
# 	else:
# 		p = select[0]
			for seccion in secciones:
				if seccion:
					p.sections.add(seccion)
			try:		
				c = ContactData(person=p, description=desc1, company=empresas[0], media=medios[0], position=positions[0], address=dir1, postal_code=cp1,
					region=regiones[0], city=ciudades[0], telf_static=fijo1, telf_movile=mobil1, fax=fax1, email=mail1_1, email_alt=mail1_2, mailing=mailing1,
					type_id=1)
				c.save()
			except Exception, e:
				print e
			try:					
				if dir2 or fijo2 or mobil2 or mail2_1 or mail2_2:
					c = ContactData(person=p, description=desc2, company=empresas[1], media=medios[1], position=positions[1], address=dir2, postal_code=cp2,
							region=regiones[1], city=ciudades[1], telf_static=fijo2, telf_movile=mobil2, fax=fax2, email=mail2_1, email_alt=mail2_2, mailing=mailing2,
							type_id=1)
					c.save()
			except Exception, e:
				print e
			try:		
				if dir3 or fijo3 or mobil3 or mail3_1 or mail3_2:
					c = ContactData(person=p, description=desc3, company=empresas[2], media=medios[2], position=positions[2], address=dir3, postal_code=cp3,
							region=regiones[2], city=ciudades[2], telf_static=fijo3, telf_movile=mobil3, fax=fax3, email=mail3_1, email_alt=mail3_2, mailing=mailing3,
							type_id=1)
					c.save()		
			except Exception, e:
				print e
	
			print p
	


print "Carrecs"
print falten_carrecs
print
print "Ciutats"
print falten_ciutats
print
print "Tratamientos"
print tratamientos
print
print "Empresas"
print empresa
print
print "Mitjans"
print medio