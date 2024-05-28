def  mayMen ():
    print('Funcion para determinar mayor o menor.')
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese otro numero: '))
    if a > b:
        return 1
    elif b > a:
         return -1
    else:
        return 0
    
print(mayMen())