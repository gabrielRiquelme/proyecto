palabra1 = input('Ingrese una palabra: ')
palabra2= input('Ingrese una palabra que rime con la anterior: ')

if len(palabra1) < 3 or len(palabra2) < 3:
    print('LAS PALABRAS TIENEN MENOS DE 3 CARACTERES, NO RIMAN')
elif palabra1[-3:] == palabra2[-3:]:
    print('Ultimos digitos coinciden, por lo que riman', palabra1[-3:])
elif palabra1[-2:] == palabra2[-2:]:
    print('Ultimos 2 digitos coinciden, por lo que riman a medias', palabra1[-2:])
else:
    print('Las Palabras no riman')