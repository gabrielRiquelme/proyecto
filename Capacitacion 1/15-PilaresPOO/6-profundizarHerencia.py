class Animales(): #Clase padre#
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre) #Palabra para heredar metodo de clase padre#
        self.sonido = sonido

perro = Perro('Goku', 'guau!')

print(perro.nombre)

