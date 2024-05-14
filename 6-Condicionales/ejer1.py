letra = input('Porfavor ingresar un vocal: ')

'''
if letra.lower() == 'a':
    print('Esta vocal es la A')
elif letra.lower() == 'e':
    print('Esta vocal es la E')
elif letra.lower() == 'i':
    print('Esta vocal es la I')
elif letra.lower() == 'o':c
    print('Esta vocal es la O')
elif letra.lower() == 'u':
    print('Esta vocal es la u')
else:
    letra = input('Porfavor ingresar un vocal, la letra ingresada no lo era: ') 
'''

''' Metodo #2 mas eficiente'''

if letra.lower() in "aeiou":
    print("La letra", letra , "Es una vocal")
else:
    print("La letra", letra , "NO es una vocal")
