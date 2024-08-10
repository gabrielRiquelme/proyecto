print('Ingrese el valor de los numeros a resolver en A B C :')
a = int(input('Ingrese el valor de A:'))
b = int(input('Ingrese el valor de B:'))
c = int(input('Ingrese el valor de C:'))

resultado = (-b + (b**2 - 4*a*c)**0.5) / (2*a)

print(resultado)