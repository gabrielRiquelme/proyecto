#Escriba un programa que lea dos números por teclado y determine con un valor booleano de True o False
#  estos ejemplos:
#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero

a = int(input('Ingrese un numero: '))
b = int(input('Ingrese un numero: '))

print('Los numeros son iguales?',a == b)
print('Los numeros son DESiguales?',a != b)
print('El primer numero ingresado es mayor?', a>b)
print('El segundo numero ingresado es mayor?', a<b)