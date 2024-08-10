from math import sqrt

a = int(input('Ingrese el valor de A: '))
b = int(input('Ingrese el valor de B: '))
c = int(input('Ingrese el valor de C: '))
x1=0
x2=0

if ((b**2)-(4*a*c)) < 0:
    print('No se puede realizar dado que no podemos calcular raiz de un numero negativo.')
else:
    x1 = (-b + sqrt(((b**2)-(4*a*c))))/(2*a)
    x2 = (-b - sqrt(((b**2)-(4*a*c))))/(2*a)

print("La solucion es: \nx1=",x1,"\nx2=",x2)