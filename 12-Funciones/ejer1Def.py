lista = []

listaPares = []

listaImpares = []

largoLista = 0

def pedirNums():
    cantidadAIngersar = 0
    cantidadAIngersar = int(input('Ingrese la cantidad de numeros que desea ingresar: '))
    for i in range(cantidadAIngersar):
        a = int(input('Ingrse un numero: '))
        lista.append(a)

def ordenPares(largoLista,lista):
    for i in lista:
        if i % 2 == 0:
            listaPares.append(i)
        else:
            listaImpares.append(i)

largoLista = len(lista)
pedirNums()
ordenPares(largoLista,lista)

print(lista)
print(listaPares)
print(listaImpares)