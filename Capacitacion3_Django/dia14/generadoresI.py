'''
def generaPares(limit):
    num=1
    miLista=[]
    while num<limit:
        miLista.append(num*2)
        num=num+1
    return miLista

print(generaPares(10))

'''
def generaPares(limit):
    num=1
    miLista=[]
    while num<limit:
        yield num*2
        num=num+1

devuelvePAres = generaPares(10)
print(next(devuelvePAres))
print(next(devuelvePAres))
print(next(devuelvePAres))