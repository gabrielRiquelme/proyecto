num1 = int(input('Ingrese un numero para calcular el rango: '))
num2 =int(input('Ingrese un numero para calcular el rango, con el numero anterior: '))

for i in range(num1,num2+1,1):
    if i % 2 == 0:
        continue
    print(i)