class Persona ():
    nacionalidad = 'Argentina' #Variable de clase#
    def __init__(self,nombre,edad): #variable de instancia#
        self.nombre = nombre
        self.edad = edad

    def correr(self):
        print('Estoy Corriendo...')

print(Persona.nacionalidad)

persona1 = Persona('Juan',20)
persona1.correr()

