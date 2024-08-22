#Escriba un programa que almacene la cadena de caracteres contraseña en una variable,
#para luego preguntarle al usuario por la contraseña.
# Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con la guardada en variable.

passwords = ['Boca1234','Riber1234','10987654321','12345678910','a']

contraIngresada = input('Ingrese una contraseña para validar si es correcta: ')

val = False

for i in passwords:
    if i == contraIngresada:
        val = True
        break

if val:
    print('La contraseña es correcta.')
else:
    print('Contraseña incorrecta')
