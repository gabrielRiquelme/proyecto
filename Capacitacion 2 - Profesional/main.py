class Persona ():
    edad = 20 #Variable de clase#
    def __init__(self,nombre,nacionalidad): #variable de instancia#
        self.nombre = nombre
        self.nacionalidad = nacionalidad


persona1 = Persona('Juan','Argentina')

print(persona1.nombre)

        
    