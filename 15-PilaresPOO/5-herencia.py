class Animales(): #Clase padre#
    def habla(self):
        print('Yo soy un animal')

    def descripcion(self):
        print('Yo soy un {}'.format(self.animal))

class Perro(Animales): #Clase heredada#
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.habla()  #Objeto desde clase padre#

perro = Perro() #Objeto desde clase perro#
perro.habla()   #Ejecuto METODO de clase padre HEREDADA#

abeja = Abeja('Abeja')

abeja.descripcion()