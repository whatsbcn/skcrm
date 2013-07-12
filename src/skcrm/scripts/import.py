import csv
import sys
import os

# paths = ['/Users/whats/Documents/code/skcrm/src/skcrm/skcrm', '/Users/whats/Documents/code/skcrm/src/skcrm/']
# 
# for path in paths:
# 	if path not in sys.path:
# 		sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'skcrm.settings'

from skcrm.models import Person, Company, Media, Section, PositionTypes, City, ContactTreatment

fd = open("20130702_BDD_ORBYCE_srAB_Dani.csv", 'rb')
buff = csv.reader(fd, delimiter=',', quotechar='|')

# TODO: Falten les observacions

i = 0
falten_sections = []
falten_carrecs = []
falten_ciutats = []
provincies = []
medio = []
empresa = []
tratamientos = []
for sec1, sec2, sec3, sec4, sec5, sec6, sec7, tratamiento, nombre, apellidos, nacimiento, observaciones, advertencias, \
	desc1, empresa1, medio1, cargo1, dir1, cp1, provincia1, ciudad1, merda, fijo1, mobil1, fax1, mail1_1, mail1_2, mailing1, \
	desc2, empresa2, medio2, cargo2, dir2, cp2, provincia2, ciudad2,  fijo2, mobil2, fax2, mail2_1, mail2_2, mailing2, \
	desc3, empresa3, medio3, cargo3, dir3, cp3, provincia3, ciudad3,  fijo3, mobil3, fax3, mail3_1, mail3_2, mailing3 in buff:
	secciones = []
# 	print "Seccions"
# 	for s in (sec1, sec2, sec3, sec4, sec5, sec6, sec7):
# 		if s != "":
# 			if len(Section.objects.filter(name=s)) == 0:
# 				if s.strip() not in falten_sections:
# 					falten_sections.append(s.strip())
# 					print s.strip()




	if len(ContactTreatment.objects.filter(name__contains=tratamiento)) == 0:
		if tratamiento != "":
			if tratamiento not in tratamientos:
				tratamientos.append(tratamiento.strip())
		
	for s in (cargo1, cargo2, cargo3):
		if s != "":
			if len(PositionTypes.objects.filter(name__contains=s)) == 0:
				if s.strip().title() not in falten_carrecs:
					falten_carrecs.append(s.strip().title())
					#print s.strip()


	for s in (ciudad1, ciudad2, ciudad3):
		if s != "":
			if len(City.objects.filter(name__contains=s)) == 0:
				if s.strip() not in falten_ciutats:
					falten_ciutats.append(s.strip())
					#print s.strip()


	for s in (empresa1, empresa2, empresa3):
		if s != "":
			if len(Company.objects.filter(name__contains=s)) == 0:
				if s.strip() not in empresa:
					empresa.append(s.strip())

	for s in (medio1, medio2, medio3):
		if s != "":
			if len(Company.objects.filter(name__contains=s)) == 0:
				if s.strip() not in medio:
					medio.append(s.strip())

	i += 1

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