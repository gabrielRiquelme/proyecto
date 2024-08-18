from functools import reduce

numeros = (1,2,3,4)

def sumar (x,y):
    return x + y

sumar = reduce(sumar,numeros)
print(sumar)