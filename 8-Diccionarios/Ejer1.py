dic = {"Guatemala": "Ciudad de Guatemala","El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input('Porfavor Ingrese un Pais: ')
letra = pais.title() in dic

if letra:
    print(dic[pais.title()])
else:
    print('Pais no encontrado, disculpe')