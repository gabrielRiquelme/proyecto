personas = {'Martin':'Martinez','Jorge':'Alvarez','Maria':'Gomez'}

print(personas.get('Jorge'))
print(personas.get('Maria'))

print(personas.keys())
print(personas.values())
print(personas.items())

#for clave,valor in personas.items():
#    print(clave,valor)

personas.pop('Martin')
print(personas)
personas.clear()
print(personas)