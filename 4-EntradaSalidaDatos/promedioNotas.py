print('Ingrese notas de los alumnos:')
P1 = float(input('Ingrese el valor de primera practica: '))
P2 = float(input('Ingrese el valor de segunda practica: '))
P3 = float(input('Ingrese el valor de tercer practica:'))
EP = float(input('Ingrese el valor de Examen parcial:'))
EF = float(input('Ingrese el valor de Examen Final:'))

PP = ( P1 + P2 +P3 ) / 3
PROM = ( PP + 2*EP + 3*EF ) / 6

print(PROM)