class Intro():
    pepe = 'hola'
    def __init__(self, valor):
        self.valor = valor

    def segundo(self):
        print('Segundo')

    def tercero(self):
        print('Tercero')

class pepe():
    def saludar(self):
        print('Hola soy pepe')

pepe1 = pepe

dato = Intro('Valor')

'''
datof = dir(dato)

for i in datof:
    print(i)
'''

#print(isinstance(dato, Intro))
#print(isinstance(dato, pepe))

print(hasattr(dato,'pepe'))