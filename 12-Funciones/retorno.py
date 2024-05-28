def entero():
    print('Este es un numero entero')
    return 10

def decimal():
    print('Este es un numero decimal')
    return 99.99

def frase():
    return 'Mi nombre es Juan'

def asignacion():
    return 1,2,3,4,5

print(entero())
print(decimal())
print(frase())

a , b ,c ,d , e = asignacion()

print(a)
print(b)
print(c)
print(d)
print(e)