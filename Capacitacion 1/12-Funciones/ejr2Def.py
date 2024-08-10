def factorial(num):
    if num < 0:
        return "Factorial no definido para números negativos"
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
        print(resultado)
    
num = int(input('Ingrese un numero para calcular su factorial: '))    
factorial(num)

