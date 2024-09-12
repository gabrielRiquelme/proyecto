def devuelve_paises(*paises):
    for elemento in paises:
        for subelemento in elemento:
            yield subelemento


paises = devuelve_paises('Mex','Arg','Bra','Per')
print(next(paises))
print(next(paises))#Cada linea imprime un nuevo pais#