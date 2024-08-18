import re

#mi_patron = re.compile('\d\d\d')
#
#print(mi_patron.search('Ta122za').group())

if re.search(r'\AA[0-9].*(end|fin)$', 'A4 es una marca de fin'):
    print('Se encontró un patrón...')
else:
    print('No se encontró ningún patrón')

#patron busqueda#