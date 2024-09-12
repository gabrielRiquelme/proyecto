def generaPares(limit):
    num=1
    miLista=[]
    while num<limit:
        miLista.append(num*2)
        num=num+1
    return miLista

print(generaPares(10))
#CON GENERADORES#
def generaPares(limit):
    num=1
    miLista=[]
    while num<limit:
        yield num*2
        num=num+1

devuelvePAres = generaPares(10)
print(devuelvePAres)
print(next(devuelvePAres))
#CON MAP#
numeros = [2,3,4,5,6,67,7,88,9,9,23,50]
i=map(lambda x:x*2,numeros)
print(list(i))

#CON LAMBDA#
doblar = lambda numero:numero*2
print(doblar(10))