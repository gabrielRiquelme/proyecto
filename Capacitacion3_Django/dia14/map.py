def doblar(numero):
    return numero*2

numeros = [2,3,4,5,6,67,7,88,9,9,23,50]

#i=map(doblar,numeros)
#print(list(i))

i=map(lambda x:x*2,numeros)
print(list(i))


#Segundo ejeemplo#
a =[1,2,3,4,5]
b=[6,7,8,9,10]

y = map(lambda x,y: x*y, a,b)
print(list(y))