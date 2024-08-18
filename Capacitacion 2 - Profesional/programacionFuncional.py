def lower(elementos):return elementos.lower()

lista = ['MARIA','JuaN','Si']

print(list(map(lower,lista)))

print([i.lower() for i in lista])