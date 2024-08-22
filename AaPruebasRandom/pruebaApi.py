import requests
import json
'''
#requests simple - prueba#

url = 'https://rickandmortyapi.com/api/character/2'
rest = requests.get(url)
ajson = rest.json()
print(ajson.keys())

#Muestra nombre y estado de personajes conectado a la api#
i = 1
while i < 5:
    url = f'https://rickandmortyapi.com/api/character/2{i}'
    rest = requests.get(url)
    ajson = rest.json()
    name = ajson['name']
    status = ajson['status']
    print(f'El personaje {name} se encuentra en estado: {status}')
    i += 1
print('*'*20)
'''
#request a episodio #
url = 'https://rickandmortyapi.com/api/episode/1'
rest = requests.get(url)
ajson = rest.json()
personajes = ajson['characters']
listnamesHuman=list()
list_others  = list()

for personaje in personajes:
    req = requests.get(personaje)
    js = req.json()
    name = js['name']
    if js['species'] == 'Human':
        listnamesHuman.append(name)
    else:
        list_others.append(name)

print(f'Los humanos son: {listnamesHuman}\n Y los no humanos son: {list_others}')
