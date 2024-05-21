num=int(input('Ingrese un numero para calcular su tabla: '))

i = 0
nm = 0

while i <= 12:
     nm = num * i
     i +=1
     print(num, 'X' , i, "=" , nm)